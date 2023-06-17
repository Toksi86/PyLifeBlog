from http import HTTPStatus
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from blog.models import Post

User = get_user_model()


class PostURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.post = Post.objects.create(
            title='Заголовок тестового поста',
            author=User.objects.create_user(username='Автор'),
            body='Текст тестового поста',
            status='draft',
            slug='test-slug'
        )

    def setUp(self):
        self.user = User.objects.create_user(username='auth')
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_home_url_is_available_for_any_user(self):
        """Страница / доступна любому пользователю."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_posts_slug_url_is_available_for_any_user(self):
        """Страница /posts/slug/ доступна любому пользователю."""
        response = self.guest_client.get('/posts/test-slug/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_new_posts_url_is_not_available_for_any_user(self):
        """Страница /posts/new_post/ не доступна любому пользователю."""
        response = self.guest_client.get('/posts/new_post/')
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            'blog/index.html': '/',
            'blog/post_detail.html': '/posts/test-slug/',
            'blog/new_post.html': '/new_post/',
        }
        for template, address in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)
