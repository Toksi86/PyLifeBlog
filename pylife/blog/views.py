from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.order_by('-created')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def get_post(request, slug):
    return HttpResponse(f'Пост со слагом: {slug}')
