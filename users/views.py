""" Profile Views """
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Exceptions
from django.db.utils import IntegrityError
# Models
from django.contrib.auth.models import User
from users.models import Profile
# Forms
from users.forms import ProfileForm


# Create your views here.
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
        data = request.POST

        if data['password'] != data['password_confirmation']:
            return render(request, 'users/signup.html', {
                'error': 'Su contraseñas no coinciden'
            })

        try:
            user = User.objects.create_user(username=data['username'], password=data['password'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.save()

            profile = Profile(user=user)
            profile.save()
        except IntegrityError:
            return render(request, 'users/signup.html', {
                'error': 'El username especificado ya existe'
            })

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """Logout View"""
    logout(request)
    return redirect('login')
