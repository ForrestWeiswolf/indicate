import pdb
from django.test import TestCase

from .models import Post, Tag


class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        posts = [
            Post.objects.create(
                title="When William Came",
                content="https://www.gutenberg.org/cache/epub/14540/pg14540-images.html",
                type=Post.PostTypes.LINK,
            ),
            Post.objects.create(
                title="Django Rest Framework",
                content="https://www.django-rest-framework.org/",
                type=Post.PostTypes.LINK,
            ),
        ]
        posts[0].tags.add(Tag.objects.create(name="Fiction"), through_defaults={"manual": True})
        posts[1].tags.add(Tag.objects.create(name="Software"), through_defaults={"manual": True})
        posts[1].tags.add(Tag.objects.create(name="Django"), through_defaults={"manual": True})

    def test_view_posts(self):
        response = self.client.get("/posts/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Django Rest Framework")
        self.assertEqual(
            response.data[0]["content"],
            "https://www.django-rest-framework.org/",
        )
        self.assertEqual(
            response.data[0]["tags"],
            ["http://testserver/posts/tags/2/", "http://testserver/posts/tags/3/"]
        )
        self.assertEqual(response.data[1]["title"], "When William Came")
        self.assertEqual(
            response.data[1]["content"],
            "https://www.gutenberg.org/cache/epub/14540/pg14540-images.html",
        )
        self.assertEqual(
            response.data[1]["tags"],
            ["http://testserver/posts/tags/1/"]
        )



class TagListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        posts = [
            Post.objects.create(
                title="When William Came",
                content="https://www.gutenberg.org/cache/epub/14540/pg14540-images.html",
                type=Post.PostTypes.LINK,
            ),
            Post.objects.create(
                title="Django Rest Framework",
                content="https://www.django-rest-framework.org/",
                type=Post.PostTypes.LINK,
            ),
        ]
        posts[0].tags.add(Tag.objects.create(name="Fiction"), through_defaults={"manual": True})
        posts[1].tags.add(Tag.objects.create(name="Software"), through_defaults={"manual": True})

    def test_view_tags(self):
        response = self.client.get("/posts/tags/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["name"], "Software")
        self.assertEqual(response.data[1]["name"], "Fiction")

    def test_view_single_tag(self):
        response = self.client.get("/posts/tags/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Fiction")

    def test_view_posts_by_tag(self):
        response = self.client.get("/posts/tags/1/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "When William Came")
