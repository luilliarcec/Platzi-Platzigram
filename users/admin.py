# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Models
from users.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Vista de Profile en la vista admin de django"""
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'phone_number')
    list_filter = ('user__is_active', 'user__is_staff', 'created_at', 'updated_at')

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            )
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                'biography'
            )
        }),
        ('Metadatos', {
            'fields': (
                ('created_at', 'updated_at'),
            )
        })
    )

    readonly_fields = ('created_at', 'updated_at')


class ProfileInLine(admin.StackedInline):
    """Vista Profile In Line que usa mi modelo Profile para agregar a User de Django en el admin"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Agregar al User de Django en el admin el Profile In Line"""
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


# Desregistra la Vista original de User Django del Admin
admin.site.unregister(User)
# Registra la vista de User modificad con nuestro Profile In Line en el admin
admin.site.register(User, UserAdmin)
