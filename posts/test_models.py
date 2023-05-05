from django.test import TestCase
from django.utils import timezone

from .models import Post, Tag

class ModelTests(TestCase):

  def test_post_can_be_created_with_properties(self):
    post = Post(
      title="The King in Yellow",
      content="https://www.gutenberg.org/files/8492/8492-h/8492-h.htm",
      creation_date=timezone.now(),
      type=Post.PostTypes.LINK
    )

    self.assertIs(post.title, "The King in Yellow")
    self.assertIs(post.content, "https://www.gutenberg.org/files/8492/8492-h/8492-h.htm")
    self.assertIs(post.creation_date.day, timezone.now().day)
    self.assertIs(post.type, Post.PostTypes.LINK)

class TagTests(TestCase):

  def test_can_be_created_with_properties(self):
    tag = Tag(
      name="Fiction",
      creation_date=timezone.now(),
    )

    self.assertIs(tag.name, "Fiction")
    self.assertIs(tag.creation_date.day, timezone.now().day)
