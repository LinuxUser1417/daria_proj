from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import Category, Discussion, Comment, Like, DisLike
from .serializers import CategorySerializer, DiscussionSerializer, CommentSerializer, LikeSerializer, DisLikeSerializer


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Получить список всех категорий", operation_summary="Список категорий")
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(operation_description="Создать новую категорию", operation_summary="Создание категории")
    def post(self, request):
        return super().post(request)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Получить детали категории по ID", operation_summary="Детали категории")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Обновить категорию по ID", operation_summary="Обновление категории")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Удалить категорию по ID", operation_summary="Удаление категории")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class DiscussionListView(generics.ListCreateAPIView):
    queryset = Discussion.objects.all().order_by('-rating')
    serializer_class = DiscussionSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Получить список всех обсуждений", operation_summary="Список обсуждений")
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(operation_description="Создать новое обсуждение", operation_summary="Создание обсуждения")
    def post(self, request):
        return super().post(request)


class DiscussionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Получить детали обсуждения по ID", operation_summary="Детали обсуждения")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Обновить обсуждение по ID", operation_summary="Обновление обсуждения")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Удалить обсуждение по ID", operation_summary="Удаление обсуждения")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Получить список всех комментариев", operation_summary="Список комментариев")
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(operation_description="Создать новый комментарий", operation_summary="Создание комментария")
    def post(self, request):
        return super().post(request)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Получить детали комментария по ID", operation_summary="Детали комментария")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Обновить комментарий по ID", operation_summary="Обновление комментария")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Удалить комментарий по ID", operation_summary="Удаление комментария")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Добавить или удалить лайк к обсуждению", operation_summary="Добавление или удаление лайка")
    def post(self, request):
        user = self.request.user
        discussion_id = request.data.get("discussion")

        # Проверяем, существует ли уже лайк от этого пользователя к этому обсуждению
        like_exists = Like.objects.filter(discussion_id=discussion_id, user=user).exists()
        
        if like_exists:
            # Если лайк уже есть, удаляем его
            Like.objects.filter(discussion_id=discussion_id, user=user).delete()
            return Response({"status": "like removed"}, status=status.HTTP_200_OK)
        else:
            # Иначе, добавляем новый лайк
            return super().post(request)


class DisLikeCreateView(generics.CreateAPIView):
    queryset = DisLike.objects.all()
    serializer_class = DisLikeSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Добавить или удалить дизлайк к обсуждению", operation_summary="Добавление или удаление дизлайка")
    def post(self, request):
        user = self.request.user
        discussion_id = request.data.get("discussion")

        # Проверяем, существует ли уже дизлайк от этого пользователя к этому обсуждению
        dislike_exists = DisLike.objects.filter(discussion_id=discussion_id, user=user).exists()
        
        if dislike_exists:
            # Если дизлайк уже есть, удаляем его
            DisLike.objects.filter(discussion_id=discussion_id, user=user).delete()
            return Response({"status": "dislike removed"}, status=status.HTTP_200_OK)
        else:
            # Иначе, добавляем новый дизлайк
            return super().post(request)