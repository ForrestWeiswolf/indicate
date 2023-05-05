from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.CharField(max_length=2048)
  pub_date = models.DateTimeField()