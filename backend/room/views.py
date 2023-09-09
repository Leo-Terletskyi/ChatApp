from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer


class RoomMessagesListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    lookup_field = 'name'
    
    def get_queryset(self):
        queryset = Message.objects.select_related('room', 'sender').filter(room__name=self.kwargs.get('name'))
        return queryset

