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

# User의 정보를 보여주는데 Uplaoded, Downloaded는 제외
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['exclude_fields'] = ['uploaded_posts', 'downloaded_posts']
        # 요청받은 User의 정보 중 Uploaded_post와 downloaded_post를 제외한 정보들을 show
        return context

# User와 subject에 해당하는 모든 Uploaded_posts의 ID와 name를 return한다.
class UserSubjectUploadsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        subject_id = self.kwargs['subject_id']
        # 특정 User의 해당 Subject의 Upload_Post들 가져오기
        posts = Post.objects.filter(uploader__id=user_id, subject__id=subject_id)
        return posts.values('id', 'name')


# User와 subject에 해당하는 모든 downloaded_posts의 ID와 이름을 보여준다.
class UserSubjectDownloadsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        subject_id = self.kwargs['subject_id']
        # 특정 User의 해당 Subject의 download_Post들 Show
        return Post.objects.filter(downloaders__id=user_id, subject__id=subject_id)

# subject에 해당하는 모든 posts들의 ID와 이름들만을 보여준다.
class SubjectPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        posts = Post.objects.filter(subject__id=subject_id)
        post_data = [{'id': post.id, 'name': post.name} for post in posts]  # Extracting the IDs and names of the posts
        return post_data



#입력받은 Post의 ID에 해당하는 Post의 모든 정보들을 보여준다.
class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        # Retrieve the specific post based on the received post ID
        return Post.objects.filter(id=post_id)
