from rest_framework import serializers
from .models import Subject, Post, User

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    uploaded_posts = PostSerializer(many=True, read_only=True)
    downloaded_posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
