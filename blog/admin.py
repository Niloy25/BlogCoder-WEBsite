from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from blog.models import Post, BlogComment

class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
    list_display = ['title', 'author']

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['comment'[0:15], 'user']

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment, BlogPostAdmin)