from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'status',)
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('body',)
    list_filter = ('created', 'status',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created',)
    search_fields = ('body',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
