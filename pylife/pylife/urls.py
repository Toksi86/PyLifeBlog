from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('users/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('about/', include('about.urls', namespace='about')),
]

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'
