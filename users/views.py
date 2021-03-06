""" Profile Views """
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
# Models
from django.contrib.auth.models import User
from posts.models import Post
# Forms
from users.forms import ProfileForm, SignupForm


# Create your views here.
class UserDetailView(LoginRequiredMixin, DetailView):
    """Clase Based View para mostrar el detalle de un usuario"""
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


class UserSignupView(FormView):
    """Clase Based View para crear una cuenta"""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Guardar los datos del formulario"""
        form.save()
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Clase Based View para actualizar una cuenta"""
    template_name = 'users/update-profile.html'
    form_class = ProfileForm

    def get_object(self, queryset=None):
        """Regresa el perfil del usuario"""
        return self.request.user.profile

    def get_success_url(self):
        """Retornar al perfil del usuario"""
        username = self.object.user.username
        return reverse_lazy('users:detail', kwargs={
            'username': username
        })


class LoginView(auth_views.LoginView):
    """Clase Based View para logear un usuario"""
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Clase Based View para logout un usuario"""
    pass
