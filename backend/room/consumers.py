import json
from urllib.parse import parse_qs

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from .models import Room, Message

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        query_params = parse_qs(self.scope['query_string'].decode('utf-8'))
        self.user2 = query_params.get('user2', [])[0]
        self.chat_room = await self.get_or_create_room()
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
        
        await self.save_message(username, room, message)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room,
            }
        )
    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room,
        }))
    
    @sync_to_async
    def save_message(self, username, room, message):
        sender = User.objects.prefetch_related('followers', 'following').get(username=username)
        room = Room.objects.prefetch_related('users').get(name=room)
        
        Message.objects.create(sender=sender, room=room, message=message)
    
    @sync_to_async
    def get_or_create_room(self):
        try:
            return Room.objects.prefetch_related('users').get(name=self.room_name)
        except ObjectDoesNotExist:
            room = Room.objects.create(name=self.room_name)
            user = User.objects.prefetch_related('followers', 'following').get(username=self.scope['user'])
            user2 = User.objects.prefetch_related('followers', 'following').get(username=self.user2)
            room.users.add(user, user2)
        return room
