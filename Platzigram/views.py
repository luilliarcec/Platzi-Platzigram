"""Platzigram URL Views """
# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Models
from posts.models import Post


# Create your views here.
class PostsFeedView(LoginRequiredMixin, ListView):
    """Clase para presentar listar todos los posts"""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created_at',)
    paginate_by = 30
    context_object_name = 'posts'
