from django.test import TestCase
from django.utils import timezone

from .models import Post, Tag, Tagging


class PostTests(TestCase):
    def setUp(self):
        self.post = Post(
            title="The King in Yellow",
            content="https://www.gutenberg.org/files/8492/8492-h/8492-h.htm",
            creation_date=timezone.now(),
            type=Post.PostTypes.LINK,
        )
        self.post.save()

        self.tag = Tag(
            name="Fiction",
            creation_date=timezone.now(),
        )
        self.tag.save()

    def test_post_can_be_created_with_properties(self):
        self.assertIs(self.post.title, "The King in Yellow")
        self.assertIs(
            self.post.content, "https://www.gutenberg.org/files/8492/8492-h/8492-h.htm"
        )
        self.assertIs(self.post.creation_date.day, timezone.now().day)
        self.assertIs(self.post.type, Post.PostTypes.LINK)

    def test_post_has_tags(self):
        self.post.tags.add(self.tag, through_defaults={"manual": False})

        self.assertEqual(self.post.tags.get(id=1).name, "Fiction")


class TagTests(TestCase):
    def setUp(self):
        self.post = Post(
            title="The King in Yellow",
            content="https://www.gutenberg.org/files/8492/8492-h/8492-h.htm",
            creation_date=timezone.now(),
            type=Post.PostTypes.LINK,
        )
        self.post.save()

        self.tag = Tag(
            name="Fiction",
            creation_date=timezone.now(),
        )
        self.tag.save()

    def test_can_be_created_with_properties(self):
        self.assertIs(self.tag.name, "Fiction")
        self.assertIs(self.tag.creation_date.day, timezone.now().day)

    def test_tag_has_post(self):
        self.post.tags.add(self.tag, through_defaults={"manual": False})

        self.assertEqual(self.tag.post_set.get(id=1).title, "The King in Yellow")


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
            type=Post.PostTypes.LINK,
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
