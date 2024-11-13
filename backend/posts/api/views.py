# from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from ..models import Post
from rest_framework import generics


# class PostViewSet(ModelViewSet):
#     queryset = Post.objects.all().order_by("number").values()
#     serializer_class = PostSerializer
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("number").values()
    serializer_class = PostSerializer
