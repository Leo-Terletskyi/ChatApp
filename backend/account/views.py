from django.db.models import Q
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from .models import User
from .permissions import IsOwner
from .serializers import UserSerializer, UserSimpleSerializer, UserContactsSerializer, UserContactStatusSerializer


class UserListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSimpleSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = UserSerializer
    lookup_field = 'username'
    
    def get_queryset(self):
        queryset = User.objects.prefetch_related('following', 'followers').filter(username=self.kwargs['username'])
        return queryset


class UserProfileRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = UserSimpleSerializer
    lookup_field = 'username'
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = UserSimpleSerializer
    queryset = User.objects.all()
    lookup_field = 'username'


class UserNewFollowView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
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
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
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


class UserContactManagementListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserContactsSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(following=user)
        return queryset


class UserContactListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserContactsSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(following=user, followers=user)
        return queryset


class UserContactStatusListAPIView(UserContactListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserContactStatusSerializer


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def search_users(request):
    query = request.data.get('query', '')
    if query:
        users = User.objects.exclude(id=request.user.id).filter(
            Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)
    return Response({'users': []})
