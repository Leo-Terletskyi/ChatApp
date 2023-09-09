from rest_framework import generics
from rest_framework import permissions
from .models import Message
from .serializers import MessageSerializer

from .permissions import IsMemberOfRoom


class RoomMessagesListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsMemberOfRoom]
    serializer_class = MessageSerializer
    lookup_field = 'name'
    
    def get_queryset(self):
        queryset = Message.objects.select_related('room', 'sender').filter(room__name=self.kwargs.get('name'))
        return queryset

