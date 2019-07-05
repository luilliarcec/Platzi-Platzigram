"""Platzigram URL Views """
# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Models
from posts.models import Post


# Create your views here.
@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/feed.html', {
        'posts': posts,
    })
