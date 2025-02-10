from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import Parent, JobOffer, Application

class ParentSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Parent.
    """


    class Meta:
        model = Parent
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "address",
           
        ]




class JobOfferSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle JobOffer.
    """
    parent = serializers.StringRelatedField()  # Affiche le `username` du parent dans la réponse

    class Meta:
        model = JobOffer
        fields = [
            "id",
            "parent",
            "title",
            "description",
            "duree",
            "salary",
            "location",
            "created_at",
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Application.
    """
    job = serializers.StringRelatedField()  # Affiche le titre de l'offre dans la réponse

    class Meta:
        model = Application
        fields = [
            "id",
            "job",
            "name",
            "applicant_email",
            "adresse",
            "tel",
            "photo",
            "message",
            "applied_at",
        ]
