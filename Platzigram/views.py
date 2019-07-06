"""Platzigram URL Views """
# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render
# Models
from posts.models import Post


# Create your views here.
class PostsFeedView(LoginRequiredMixin, ListView):
    """Clase para presentar listar todos los posts"""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created_at',)
    paginate_by = 2
    context_object_name = 'posts'

# @login_required
# def list_posts(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'posts/feed.html', {
#         'posts': posts,
#     })
