from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView

from .models import Post, Comment
from .forms import PostForm


def index(request):
    posts = Post.objects.all().order_by('-created')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'slug': slug,
        'comments': comments,
    }
    return render(request, 'blog/post_detail.html', context)


def authorized_only(func):
    """Декоратор: доступ к view только для авторизированных пользователей."""
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('/auth/login/')
    return check_user


@authorized_only
def some_view(request):
    pass


class PostView(CreateView):
    form_class = PostForm

    template_name = 'blog/new_post.html'

    success_url = '/thankyou/'
