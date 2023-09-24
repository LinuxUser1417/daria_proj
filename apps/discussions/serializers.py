from rest_framework import serializers
from .models import Category, Discussion, Comment, Like, DisLike


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DiscussionSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()

    class Meta:
        model = Discussion
        fields = '__all__'
        read_only_fields = ('id', 'user', 'rating')

    def get_likes(self, obj):
        return Like.objects.filter(discussion=obj).count()

    def get_dislikes(self, obj):
        return DisLike.objects.filter(discussion=obj).count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'user')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ('id', 'user')



class DisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisLike
        fields = '__all__'
        read_only_fields = ('id', 'user')
