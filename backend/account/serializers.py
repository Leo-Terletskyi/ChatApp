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
            'first_name',
            'last_name',
            'email',
            'photo',
            'is_online',
            'birthday',
            'phone',
            'following',
            'followers'
        ]


class UserSimpleSerializer(serializers.ModelSerializer):
    photo = VersatileImageFieldSerializer(sizes='user_photo')
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'photo',
            'is_online',
            'birthday',
            'phone',
        ]


class UserContactsSerializer(serializers.ModelSerializer):
    photo = VersatileImageFieldSerializer(sizes='user_photo')
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'photo',
            'is_online',
        ]


class UserContactStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'is_online']
