from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

class LargeResultsSetPagination(PageNumberPagination):
  page_size = 5
  page_query_param = 'page_size'
  max_page_size = 100

class PostViewset(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  pagination_class = LargeResultsSetPagination

class CommentViewset(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer