from dataclasses import field
from django.contrib.auth.models import User, Group
from posts.models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content"]
