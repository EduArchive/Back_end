from rest_framework import generics
from .models import User, Subject, Post
from .serializers import UserSerializer, SubjectSerializer, PostSerializer

#User create
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Post create
class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #User의 Uploaded Post에 추가
    def perform_create(self, serializer):
        # 입력받은 정보로 Post를 create하고, 만든 Post를 해당 User의 Uploaded Post로 추가하기
        post = serializer.save()
        user = self.request.user
        user.uploaded_posts = post
        user.save()


# 특정 Post를 download한 user의 Downloaded Post로 추가하기
class PostDownloadAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):

        post = serializer.save()
        user = self.request.user
        user.downloaded_posts.add(post)

# 입력받은 User ID에 해당하는 User의 uploaded_post와 downloaded_post의 정보를 제외하고 보여준다
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        return User.objects.filter(id=user_id).exclude(uploaded_posts__isnull=False, downloaded_posts__isnull=False).first()


# User와 subject에 해당하는 모든 Uploaded_posts의 ID와 name를 return한다.
class UserSubjectUploadsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        subject_id = self.kwargs['subject_id']
        # 요청받은 User와 입력받은 Subject에 해당하는 모든 Uploaded_posts를 반환
        return User.objects.get(id=user_id).uploaded_posts.filter(subject__id=subject_id)



# User와 subject에 해당하는 모든 downloaded_posts를 보여준다.
class UserSubjectDownloadsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        subject_id = self.kwargs['subject_id']
        # User와 Subject에 해당하는 모든 downloaded_posts를 반환
        return User.objects.get(id=user_id).downloaded_posts.filter(subject__id=subject_id)


# subject에 해당하는 모든 posts들을 보여준다.
class SubjectPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        # 특정 과목에 해당하는 모든 자료들을 show
        return Post.objects.filter(subject__id=subject_id)



