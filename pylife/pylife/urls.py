from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
]
