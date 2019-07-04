# Django
from django import forms


class ProfileForm(forms.Form):
    """Formulario y validación de Profile"""
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.DecimalField(max_digits=20, decimal_places=0, required=True)
    picture = forms.ImageField(required=True)
