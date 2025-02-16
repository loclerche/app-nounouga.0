from django.db import models

# Modèle pour stocker les offres d'emploi
class Offre(models.Model):
    titre = models.CharField(max_length=255)  # Titre de l'offre
    duree_contrat = models.CharField(max_length=100)  # Durée du contrat
    description = models.TextField()  # Description de l'offre
    nom_employeur = models.CharField(max_length=255)  # Nom de l'employeur
    localisation = models.CharField(max_length=255)  # Localisation de l'offre
    telephone = models.CharField(max_length=20)  # Numéro de téléphone de l'employeur
    mail = models.EmailField()  # Email de contact

    def __str__(self):
        return self.titre

# Modèle pour stocker les informations des postulants
class Postulant(models.Model):
    nom = models.CharField(max_length=255)  # Nom du postulant
    description = models.TextField()  # Description du postulant
    localisation = models.CharField(max_length=255)  # Localisation du postulant
    telephone = models.CharField(max_length=20)  # Numéro de téléphone du postulant
    mail = models.EmailField()  # Email du postulant
    metier = models.CharField(max_length=255)  # Métier du postulant

    def __str__(self):
        return self.nom
