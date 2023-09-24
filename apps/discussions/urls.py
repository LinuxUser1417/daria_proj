from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView,
    DiscussionListView, DiscussionDetailView,
    CommentListView, CommentDetailView,
    LikeCreateView, DisLikeCreateView
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    
    # Discussion URLs
    path('discussions/', DiscussionListView.as_view(), name='discussion-list'),
    path('discussions/<int:pk>/', DiscussionDetailView.as_view(), name='discussion-detail'),
    
    # Comment URLs
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    
    # Like and Dislike URLs
    path('like/', LikeCreateView.as_view(), name='like-create'),
    path('dislike/', DisLikeCreateView.as_view(), name='dislike-create'),
]