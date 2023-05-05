from django.test import TestCase
from django.utils import timezone

from .models import Post, Tag, Tagging

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

  def test_post_has_tags(self):
    tag = Tag(
      name="Fiction",
      creation_date=timezone.now(),
    )
    tag.save()

    post = Post(
      title="The King in Yellow",
      content="https://www.gutenberg.org/files/8492/8492-h/8492-h.htm",
      creation_date=timezone.now(),
      type=Post.PostTypes.LINK
    )
    post.save()

    post.tags.add(tag, through_defaults={"manual": False})

    self.assertEqual(post.tags.get(id=1).name, "Fiction")


class TagTests(TestCase):

  def test_can_be_created_with_properties(self):
    tag = Tag(
      name="Fiction",
      creation_date=timezone.now(),
    )

    self.assertIs(tag.name, "Fiction")
    self.assertIs(tag.creation_date.day, timezone.now().day)

  def test_tag_has_post(self):
    post = Post(
      title="The King in Yellow",
      content="https://www.gutenberg.org/files/8492/8492-h/8492-h.htm",
      creation_date=timezone.now(),
      type=Post.PostTypes.LINK
    )
    post.save()

    tag = Tag(
      name="Fiction",
      creation_date=timezone.now(),
    )
    tag.save()

    post.tags.add(tag, through_defaults={"manual": False})

    self.assertEqual(tag.post_set.get(id=1).title, "The King in Yellow")

class TaggingTests(TestCase):

  def test_can_be_created_with_properties(self):
    tagging = Tagging(
      manual=True,
      creation_date=timezone.now(),
    )

    self.assertTrue(tagging.manual)
    self.assertIs(tagging.creation_date.day, timezone.now().day)

  def test_tag_has_post_via_tagging(self):
    post = Post(
      title="The King in Yellow",
      content="https://www.gutenberg.org/files/8492/8492-h/8492-h.htm",
      creation_date=timezone.now(),
      type=Post.PostTypes.LINK
    )
    post.save()

    tag = Tag(
      name="Fiction",
      creation_date=timezone.now(),
    )
    tag.save()

    post.tags.add(tag, through_defaults={"manual": False})

    tagging = Tagging.objects.get(post=post, tag=tag)
    self.assertIs(tagging.creation_date.day, timezone.now().day)
