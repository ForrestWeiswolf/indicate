from django.db import models


class Post(models.Model):
    class PostTypes(models.TextChoices):
        LINK = "Link"

    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2048)
    pub_date = models.DateTimeField()
    type = models.CharField(max_length=16, choices=PostTypes.choices)
