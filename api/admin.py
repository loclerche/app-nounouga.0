from django.contrib import admin
from .models import Parent, JobOffer, Application


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour le modèle Parent.
    """
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email', 'phone', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour le modèle JobOffer.
    """
    list_display = ('title', 'parent', 'location', 'salary', 'created_at')
    list_filter = ('created_at', 'location')
    search_fields = ('title', 'description', 'parent__username')
    ordering = ('-created_at',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour le modèle Application.
    """
    list_display = ('name', 'applicant_email', 'job', 'applied_at')
    list_filter = ('applied_at', 'job__title')
    search_fields = ('name', 'applicant_email', 'job__title')
    ordering = ('-applied_at',)
