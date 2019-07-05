""" Profile Views """
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Models
from django.contrib.auth.models import User
from users.models import Profile
# Forms
from users.forms import ProfileForm, SignupForm


# Create your views here.
@login_required
def update_profile(request):
    """Update profile View"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

    else:
        form = ProfileForm()

    return render(request, 'users/update-profile.html', {
        'profile': profile,
        'form': form
    })


def login_view(request):
    """Login View"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {
                'error': 'Credenciales incorrectas'
            })

    return render(request, 'users/login.html')


def signup(request):
    """Signup View"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {
        'form': form,
    })


@login_required
def logout_view(request):
    """Logout View"""
    logout(request)
    return redirect('login')
