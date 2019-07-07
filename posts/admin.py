# Django
from django.contrib import admin

# Models
from posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Vista de Posts en la vista admin de django"""
    list_display = ('pk', 'title', 'user', 'photo', 'created_at')
    list_display_links = ('pk', 'title', 'user')
    search_fields = ('user__username', 'user__email', 'title')
    list_filter = ('created_at', 'updated_at')
