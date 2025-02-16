from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OffreViewSet, PostulantViewSet

# Création du routeur DRF
router = DefaultRouter()
router.register(r'offres', OffreViewSet)
router.register(r'postulants', PostulantViewSet)

# Définition des URLs de l'application job_api
urlpatterns = [
    path('', include(router.urls)),  # Inclusion des routes API
]
