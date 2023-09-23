from rest_framework import serializers
from .models import User, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['ID', 'first_name', 'last_name', 'discussions', 'liked_discussions', 'rating']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number']