from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    photo = VersatileImageFieldSerializer(sizes='user_photo')
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'photo',
            'is_online',
            'birthday',
            'phone',
            'following',
            'followers'
        ]

