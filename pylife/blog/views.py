from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    return render(request, template)


def get_post(request, slug):
    return HttpResponse(f'Пост со слагом: {slug}')
