from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-creation_date")
    serializer_class = PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by("-creation_date")
    serializer_class = TagSerializer

    @action(detail=True)
    def posts(self, request, *args, **kwargs):
        tag = self.get_object()
        posts = tag.post_set.all()
        posts_json = PostSerializer(posts, many=True, context={'request': request}).data
        return Response(posts_json)
