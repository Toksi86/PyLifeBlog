from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            title='Заголовок тестового поста',
            author=cls.user,
            body='Текст тестового поста',
            status='draft',
        )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        post = PostModelTest.post
        field_verboses = {
            'title': 'Заголовок',
            'author': 'Автор',
            'body': 'Текст',
            'slug': 'Адрес страницы',
            'status': 'Статус',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).verbose_name, expected_value)
