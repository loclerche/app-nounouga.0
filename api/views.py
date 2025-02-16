from rest_framework import viewsets
from .models import Offre, Postulant
from .serializers import OffreSerializer, PostulantSerializer

# ViewSet pour gérer les offres
class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()  # Récupérer toutes les offres
    serializer_class = OffreSerializer  # Utiliser le sérialiseur correspondant

# ViewSet pour gérer les postulants
class PostulantViewSet(viewsets.ModelViewSet):
    queryset = Postulant.objects.all()  # Récupérer tous les postulants
    serializer_class = PostulantSerializer  # Utiliser le sérialiseur correspondant
