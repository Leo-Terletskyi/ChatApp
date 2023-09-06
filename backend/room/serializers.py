from rest_framework import serializers
from .models import Message, Room


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'message', 'timestamp']


class RoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'messages']
