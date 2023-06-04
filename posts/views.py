from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-creation_date")
    serializer_class = PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by("-creation_date")
    serializer_class = TagSerializer
