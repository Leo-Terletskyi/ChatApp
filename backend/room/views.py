from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer, MessageSerializer


class RoomRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'name'


