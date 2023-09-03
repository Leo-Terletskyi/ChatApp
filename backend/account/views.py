from django.db.models import Q
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserNewFollowView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def create(self, request, *args, **kwargs):
        current_user = self.request.user
        follower_user = User.objects.get(id=request.data.get('following_id'))

        if follower_user != current_user:
            if follower_user not in current_user.following.all():
                current_user.following.add(follower_user)
                current_user.save()
                serializer = self.get_serializer(current_user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail': 'You are already following this user.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)


class UserUnfollowView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    
    def create(self, request, *args, **kwargs):
        current_user = self.request.user
        user_to_unfollow = User.objects.get(id=request.data.get('unfollow_id'))
        
        if user_to_unfollow != current_user:
            if user_to_unfollow in current_user.following.all():
                current_user.following.remove(user_to_unfollow)
                current_user.save()
                serializer = self.get_serializer(current_user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail': 'You are already following this user.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def search_users(request):
    query = request.data.get('query', '')
    if query:
        users = User.objects.exclude(id=request.user.id).filter(
            Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)
    return Response({'users': []})


