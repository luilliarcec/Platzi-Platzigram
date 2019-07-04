# Django
from django import forms
from django.core import validators


class ProfileForm(forms.Form):
    """Formulario y validación de Profile"""
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=True)
    # phone_number = forms.DecimalField(max_digits=20, decimal_places=0, required=True)
    phone_number = forms.CharField(validators=[
        validators.RegexValidator(
            regex=r'^\d+$',
            message='Solo se permiten números',
            code='invalid_phone_number'
        ),
    ], min_length=10, max_length=20)
    picture = forms.ImageField(required=True)
