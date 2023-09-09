from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListAPIView.as_view()),
    path('users/search/', views.search_users),
    path('contacts/', views.UserContactListAPIView.as_view()),
    path('contacts/online-status/', views.UserContactStatusListAPIView.as_view()),
    path('contact-management/', views.UserContactManagementListAPIView.as_view()),
    path('new-follow/', views.UserNewFollowView.as_view()),
    path('unfollow/', views.UserUnfollowView.as_view()),
    path('<str:username>/', views.UserRetrieveAPIView.as_view()),
    path('<str:username>/profile/', views.UserProfileRetrieveAPIView.as_view()),
    path('<str:username>/update/', views.UserUpdateAPIView.as_view()),

]
