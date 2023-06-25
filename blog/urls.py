from django.urls import path
from .views import UserCreateAPIView, UserListCreateView, UserDetailView, \
    SubjectListCreateView, SubjectDetailView, PostListCreateView, PostDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
]
