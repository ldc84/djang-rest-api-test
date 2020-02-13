from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
  image = serializers.ImageField(use_url=True)
  comments = CommentSerializer(many=True, read_only=True)

  class Meta:
    model = Post
    fields = ('title', 'text', 'image', 'comments')