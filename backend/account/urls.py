from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('', views.UserListAPIView.as_view()),
    path('<str:username>/', views.UserRetrieveAPIView.as_view()),
    
]
