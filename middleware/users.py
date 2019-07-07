# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Middleware completar el perfil de usuario
    Asegurar que el usuario haya completado toda su información
    antes de poder hacer uso de la aplicación.
    """

    def __init__(self, get_response):
        """Inicializa middleware"""
        self.get_response = get_response

    def __call__(self, request):
        """Funcion que será ejecutada para cada request antes que la vista sea llamada"""
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('users:update'), reverse('users:logout')]:
                    return redirect('users:update')

        response = self.get_response(request)
        return response


class RedirectFeedUserForLoginActiveMiddleware:
    """Redirije al usuario al feed
    si ya existe una sesión activa y bloquea
    el acceso a singup
    """

    def __init__(self, get_response):
        """Inicializa middleware"""
        self.get_response = get_response

    def __call__(self, request):
        """Funcion que será ejecutada para cada request antes que la vista sea llamada"""
        if not request.user.is_anonymous:
            if request.path == reverse('users:signup'):
                return redirect('feed')

        response = self.get_response(request)
        return response
