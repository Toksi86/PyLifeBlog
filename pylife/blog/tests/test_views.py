from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from blog.models import Post

User = get_user_model()


class TaskPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Post.objects.create(
            title='Заголовок тестового поста',
            author=User.objects.create_user(username='Автор'),
            body='Текст тестового поста',
            status='draft',
            slug='test-slug'
        )

    def setUp(self):
        self.user = User.objects.create_user(username='Auth')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_pages_names = {
            'blog/index.html': reverse('blog:index'),
            'blog/post_detail.html': (
                reverse('blog:post_detail', kwargs={'slug': 'test-slug'})
            ),
            'blog/new_post.html': reverse('blog:new_post'),

        }
        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
