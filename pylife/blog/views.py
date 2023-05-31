from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.objects.order_by('-created')[:10]

    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)
