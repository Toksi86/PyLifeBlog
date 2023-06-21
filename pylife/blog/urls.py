from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug>/comment/', views.add_comment, name='add_comment'),
]
