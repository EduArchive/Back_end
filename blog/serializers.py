from rest_framework import serializers
from .models import Subject, Post, User

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    uploader = serializers.StringRelatedField()
    downloaders = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)
    uploaded_posts = PostSerializer()
    downloaded_posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
