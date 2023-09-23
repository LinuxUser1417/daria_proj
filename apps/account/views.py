from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema

from .serializers import LoginSerializer, UserRegistrationSerializer, UserSerializer
from .models import CustomUser


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class RegistrationAPIView(APIView):
    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        phone_number = request.data.get("phone_number")
        password = request.data.get("password")
        
        user = CustomUser.objects.filter(phone_number=phone_number).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

class ProfileUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=UserSerializer)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=UserSerializer)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class UserListCreateView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     @swagger_auto_schema(
#         operation_summary="Создать нового пользователя",
#         operation_description="Создать нового пользователя с помощью данного эндпоинта.",
#         request_body=UserSerializer,
#     )
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     @swagger_auto_schema(
#         operation_summary="Получить информацию о пользователе",
#         operation_description="Получить информацию о пользователе по ID.",
#     )
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
