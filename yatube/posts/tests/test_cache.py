from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import Client, TestCase
from django.urls import reverse

from posts.models import Post

User = get_user_model()


class TestCache(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')

    def setUp(self) -> None:
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_index_cache(self) -> None:
        """Проверка доступности кеша index."""
        new_post = Post.objects.create(
            author=self.user,
            text='1',
        )
        response_before_deleting = self.authorized_client.get(
            reverse('posts:index'),
        )
        new_post.delete()
        response_after_deleting = self.authorized_client.get(
            reverse('posts:index'),
        )
        self.assertEqual(
            response_before_deleting.content,
            response_after_deleting.content,
        )
        cache.clear()
        response_after_cleaning_cahe = self.authorized_client.get(
            reverse('posts:index'),
        )
        self.assertNotEqual(
            response_after_deleting.content,
            response_after_cleaning_cahe.content,
        )
