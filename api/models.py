from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Parent(AbstractUser):
    """
    Modèle pour les parents (utilisateurs authentifiés).
    Hérite de AbstractUser pour garder les fonctionnalités Django.
    """
    email = models.EmailField(unique=True)  # Identifiant unique pour l'authentification
    phone = models.CharField(max_length=15, blank=True, null=True)  # Numéro de téléphone (optionnel)
    address = models.TextField(blank=True, null=True)  # Adresse (optionnelle)

    groups = models.ManyToManyField(
        Group,
        related_name="parent_groups",  # Ajout d'un related_name unique
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="parent_permissions",  # Ajout d'un related_name unique
        blank=True,
    )

    def __str__(self):
        return self.username



class JobOffer(models.Model):
    """
    Modèle pour une offre d'emploi postée par un parent.
    """
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)  # Lien avec le parent (auteur)
    title = models.CharField(max_length=200)  # Titre de l'offre
    description = models.TextField()  # Détails du poste
    duree = models.TextField()  # Durée du contrat
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Salaire (optionnel)
    location = models.CharField(max_length=255, blank=True, null=True)  # Lieu du travail
    created_at = models.DateTimeField(auto_now_add=True)  # Date de publication automatique

    def __str__(self):
        return f"{self.title} - {self.parent.username}"


class Application(models.Model):
    """
    Modèle pour stocker les candidatures des nounous.
    Elles peuvent postuler sans compte.
    """
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE, related_name='applications')# Offre d'emploi concernée
    name = models.CharField(max_length=100)  # Nom du candidat
    applicant_email = models.EmailField()  # Email de la nounou qui postule
    adresse = models.CharField(max_length=255, blank=True, null=True)  # Adresse (optionnelle)
    tel = models.CharField(max_length=15, blank=True, null=True)  # Numéro de téléphone (optionnel)
    photo = models.ImageField(upload_to='applications/photos/', blank=True, null=True)  # Photo du candidat (optionnelle)
    message = models.TextField()  # Message de motivation
    applied_at = models.DateTimeField(auto_now_add=True)  # Date de candidature automatique

    def __str__(self):
        return f"Candidature {self.applicant_email} pour {self.job.title}"
