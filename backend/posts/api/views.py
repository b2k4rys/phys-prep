# from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from ..models import Post
from rest_framework import generics


# class PostViewSet(ModelViewSet):
#     queryset = Post.objects.all().order_by("number").values()
#     serializer_class = PostSerializer
class PostListAPIView(generics.ListAPIView):

    serializer_class = PostSerializer

    def get_queryset(self):
        set = self.kwargs["set"]
        section = self.kwargs["section"]
        return Post.objects.filter(
            topic__set_number=int(set), topic__section__value=int(section)
        ).all()
