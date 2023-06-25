from rest_framework.serializers import ModelSerializer
from .models import User, Blog

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'