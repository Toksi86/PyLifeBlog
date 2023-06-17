from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.PostView.as_view(), name='new_post'),
    # TODO: Do action new_comment
    path('posts/<slug>/', views.post_detail, name='post_detail'),
]
