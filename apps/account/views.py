from rest_framework import generics
from .models import CustomUser, User
from .serializers import CustomUserSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema

class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @swagger_auto_schema(
        operation_summary="Создать нового пользователь",
        operation_description="Создать нового пользователя с помощью данного эндпоинта.",
        request_body=CustomUserSerializer,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Получить информацию о пользователе",
        operation_description="Получить информацию о пользователе по ID.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_summary="Создать нового пользователя",
        operation_description="Создать нового пользователя с помощью данного эндпоинта.",
        request_body=UserSerializer,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_summary="Получить информацию о пользователе",
        operation_description="Получить информацию о пользователе по ID.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Обновить информацию о пользователе",
        operation_description="Обновить информацию о пользователе с помощью данного эндпоинта.",
        request_body=CustomUserSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_summary="Обновить информацию о пользователе",
        operation_description="Обновить информацию о пользователе с помощью данного эндпоинта.",
        request_body=UserSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
