"""Users Forms"""
# Django
from django import forms
from django.contrib.auth.models import User
from django.core import validators
# Models
from users.models import Profile


class ProfileForm(forms.ModelForm):
    """Formulario y validación de Profile"""
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(validators=[
        validators.RegexValidator(
            regex=r'^\d+$',
            message='Solo se permiten números',
            code='invalid_phone_number'
        ),
    ], min_length=10, max_length=20)
    # Cuando se usa una Base View de update ya valida
    # si existe ese campo en la base de datos y no lo vuelve a reuquerir
    picture = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['website', 'biography', 'phone_number', 'picture']


class SignupForm(forms.Form):
    """Formulario y validacion signup"""
    username = forms.CharField(min_length=4, max_length=20)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.EmailField(min_length=6, max_length=70)

    def clean_username(self):
        """Username unico"""
        username = self.cleaned_data['username']
        result = User.objects.filter(username=username).exists()
        if result:
            raise forms.ValidationError('El nombre de usuario ya existe')
        return username

    def clean_email(self):
        """Email único"""
        email = self.cleaned_data['email']
        result = User.objects.filter(email=email).exists()
        if result:
            raise forms.ValidationError('Este email ya se encuentra registrado')
        return email

    def clean(self):
        """Verificar password"""
        data = super().clean()
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')
        if password != password_confirmation:
            msg = 'Las contraseñas no coinciden'
            self.add_error('password', msg)
            self.add_error('password_confirmation', msg)
        return data

    def save(self):
        """Crear un nuevo usuario y perfil"""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
