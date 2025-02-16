from rest_framework import serializers
from .models import Offre, Postulant

# Sérialiseur pour les offres
class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = '__all__'  # Inclure tous les champs du modèle

# Sérialiseur pour les postulants
class PostulantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulant
        fields = '__all__'  # Inclure tous les champs du modèle
