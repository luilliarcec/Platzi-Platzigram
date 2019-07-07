"""Forms Posts"""
# Django
from django import forms
# Models
from posts.models import Post


class PostForm(forms.ModelForm):
    """Forms basado en Modelo"""
    class Meta:
        """Configuraciones del form"""
        model = Post
        fields = ('user', 'profile', 'title', 'photo')
