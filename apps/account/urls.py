from django.urls import path, include
from rest_framework import routers

from .views import LoginAPIView, RegistrationAPIView, ProfileUpdateAPIView, DeleteUserAPIView, UserListView, UserProfileView


urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('me/', UserProfileView.as_view(), name='user-profile'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('update/', ProfileUpdateAPIView.as_view(), name='update'),
    path('delete/', DeleteUserAPIView.as_view(), name='delete')
    
]
