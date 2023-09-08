from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('', views.UserListAPIView.as_view()),
    path('users/search/', views.search_users),
    path('contacts/', views.UserContactListAPIView.as_view()),
    path('contacts/online-status/', views.UserContactStatusListAPIView.as_view()),
    path('contact-management/', views.UserContactManagementListAPIView.as_view()),
    path('<str:username>/', views.UserRetrieveUpdateDestroyAPIView.as_view()),
    path('<str:username>/new-follow/', views.UserNewFollowView.as_view()),
    path('<str:username>/unfollow/', views.UserUnfollowView.as_view()),
    
]
