# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Forms
from posts.forms import PostForm


# Create your views here.
@login_required
def create_posts(request):
    """Crear un nuevo posts"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'posts/new.html', {
        'form': form
    })
