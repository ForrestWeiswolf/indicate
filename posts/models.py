from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField()

class Post(models.Model):
    class PostTypes(models.TextChoices):
        LINK = "Link"

    tags = models.ManyToManyField(Tag, through="Tagging")

    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2048)
    creation_date = models.DateTimeField()
    type = models.CharField(max_length=16, choices=PostTypes.choices)

class Tagging(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    manual = models.BooleanField()
    creation_date = models.DateTimeField(default=timezone.now)
    class Meta:
        unique_together = ("post", "tag")
