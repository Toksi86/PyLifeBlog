from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.order_by('-created')[:10]

    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
        'slug': slug,
    }
    return render(request, 'blog/post_detail.html', context)


class PostView(CreateView):
    form_class = PostForm

    template_name = 'blog/new_post.html'

    success_url = '/thankyou/'
