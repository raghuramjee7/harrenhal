from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.user = get_user_model().objects.create_user(
            username = "testUser",
            email = "test@test.com",
            password = "secret"
        )

        cls.post = Post.objects.create(
            title = "new post",
            author = cls.user,
            body = "Body content"
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "new post")
        self.assertEqual(self.post.body, "Body content")
        self.assertEqual(self.post.author.username, "testUser")
        self.assertEqual(str(self.post), "new post")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
