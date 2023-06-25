from django.urls import path
from . import views

urlpatterns = [
    path('users/create/', views.UserCreateAPIView.as_view(), name='user-create'),
    path('posts/create/', views.PostCreateAPIView.as_view(), name='post-create'),
    path('posts/download/', views.PostDownloadAPIView.as_view(), name='post-download'),
    path('users/<int:user_id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/<int:user_id>/subjects/<int:subject_id>/uploads/', views.UserSubjectUploadsView.as_view(), name='user-subject-uploads'),
    path('users/<int:user_id>/subjects/<int:subject_id>/downloads/', views.UserSubjectDownloadsView.as_view(), name='user-subject-downloads'),
    path('subjects/<int:subject_id>/posts/', views.SubjectPostsView.as_view(), name='subject-posts'),
]
