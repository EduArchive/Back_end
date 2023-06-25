from rest_framework import generics
from .serializers import *
from .models import *


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'name'


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'name'


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'name'


class BlogCreateAPIView():
    pass


class BlogListAPIView():
    pass


class BlogRetrieveAPIView():
    pass


class BlogUpdateAPIView():
    pass


class BlogDestroyAPIView():
    pass