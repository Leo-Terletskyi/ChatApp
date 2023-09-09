from rest_framework import permissions
from .models import Room


class IsMemberOfRoom(permissions.BasePermission):
    def has_permission(self, request, view):
        room_name = view.kwargs.get('name')
       
        try:
            room = Room.objects.get(name=room_name)
            return request.user in room.users.all()
        except Room.DoesNotExist:
            return False
