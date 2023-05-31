from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index),
    path('posts/<slug>/', views.post_detail),
    path('auth/', include('django.contrib.auth.urls')),
]
