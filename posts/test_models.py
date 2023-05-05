from django.test import TestCase
from django.utils import timezone

from .models import Post

class PostTests(TestCase):

  def test_can_be_created_with_basic_properties(self):
    post = Post(
      title="The King in Yellow",
      content="https://www.gutenberg.org/files/8492/8492-h/8492-h.htm",
      pub_date=timezone.now(),
      type=Post.PostTypes.LINK
    )

    self.assertIs(post.title, "The King in Yellow")
    self.assertIs(post.content, "https://www.gutenberg.org/files/8492/8492-h/8492-h.htm")
    self.assertIs(post.pub_date.day, timezone.now().day)
    self.assertIs(post.type, Post.PostTypes.LINK)
