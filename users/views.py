""" Profile Views """
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile
# Forms
from users.forms import ProfileForm, SignupForm


# Create your views here.
class UserDetailView(LoginRequiredMixin, DetailView):
    """Clase para vista de detalle (Otra manera de trabajar vistas)"""
    template_name = 'users/detail.html'
    # Parametro de busqueda en el query (valor unico o pk)
    slug_field = 'username'
    # Parametro de la Url que recive
    slug_url_kwarg = 'username'
    # Nombre de parametro de acceso al objeto enviado en esta vista
    context_object_name = 'user'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        """Agregar a la vista del detalle del usuario sus posts"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created_at')
        return context


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
            url = reverse('users:detail', kwargs={
                'username': request.user.username
            })
            return redirect(url)
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
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {
        'form': form,
    })


@login_required
def logout_view(request):
    """Logout View"""
    logout(request)
    return redirect('users:login')
