from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('about/', include('about.urls', namespace='about')),
    path('admin/', admin.site.urls),
]
