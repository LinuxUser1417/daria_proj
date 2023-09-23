from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customusers', views.CustomUserViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customusers/', views.CustomUserListCreateView.as_view(), name='customuser-list-create'),
    path('customusers/<int:pk>/', views.CustomUserDetailView.as_view(), name='customuser-detail'),
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('customusers/<int:pk>/update/', views.CustomUserViewSet.as_view({'put': 'update'}), name='customuser-update'),
    path('users/<int:pk>/update/', views.UserViewSet.as_view({'put': 'update'}), name='user-update'),
]
