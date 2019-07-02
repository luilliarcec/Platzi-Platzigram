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
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')

        response = self.get_response(request)
        return response
