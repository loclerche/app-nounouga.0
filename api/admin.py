from django.contrib import admin
from .models import Offre, Postulant

# Enregistrer les modèles pour qu'ils apparaissent dans l'admin
@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'nom_employeur', 'localisation', 'duree_contrat')  # Colonnes affichées
    search_fields = ('titre', 'nom_employeur')  # Recherche possible par titre et employeur
    list_filter = ('duree_contrat', 'localisation')  # Filtres disponibles

@admin.register(Postulant)
class PostulantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'metier', 'localisation', 'telephone')  # Colonnes affichées
    search_fields = ('nom', 'metier')  # Recherche par nom et métier
    list_filter = ('metier', 'localisation')  # Filtres disponibles
