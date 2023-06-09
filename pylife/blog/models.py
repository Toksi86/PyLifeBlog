from django.db import models
from django.contrib.auth import get_user_model

from .validators import validate_not_empty

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=200,
        validators=[validate_not_empty],)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    body = models.TextField(
        'Текст',
        validators=[validate_not_empty])
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        'Адрес страницы',
        max_length=200,
        unique=True)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('hidden', 'Hidden')
    )
    status = models.CharField(
        'Статус',
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='blogs/',
        blank=True
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.body[:200]}...'


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(validators=[validate_not_empty])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.post.title
