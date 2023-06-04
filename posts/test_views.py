import pdb
from django.test import TestCase
from django.urls import reverse

from .models import Post


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
                title="The King in Yellow",
                content="https://www.gutenberg.org/files/8492/8492-h/8492-h.htm",
                type=Post.PostTypes.LINK,
            ),
        ]

    def test_view_posts(self):
        response = self.client.get("/posts/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "The King in Yellow")
        self.assertEqual(
            response.data[0]["content"],
            "https://www.gutenberg.org/files/8492/8492-h/8492-h.htm",
        )
        self.assertEqual(response.data[1]["title"], "When William Came")
        self.assertEqual(
            response.data[1]["content"],
            "https://www.gutenberg.org/cache/epub/14540/pg14540-images.html",
        )
