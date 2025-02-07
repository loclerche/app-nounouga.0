from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from .models import Parent, JobOffer, Application
from .serializers import ParentSerializer, JobOfferSerializer, ApplicationSerializer


# -------------------- Authentification --------------------

class RegisterParentView(APIView):
    """
    Vue pour inscrire un nouveau Parent.
    """
    permission_classes = []  # Accessible sans authentification

    def post(self, request):
        data = request.data
        data["password"] = make_password(data.get("password"))  # Hache le mot de passe
        serializer = ParentSerializer(data=data)
        if serializer.is_valid():
            parent = serializer.save()

            # Optionnel : Ajouter le parent à un groupe par défaut
            group, _ = Group.objects.get_or_create(name="Parent")
            parent.groups.add(group)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------- Parent Views --------------------

class ParentListCreateView(generics.ListCreateAPIView):
    """
    API pour lister et créer des Parents.
    Accès restreint aux utilisateurs authentifiés.
    """
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API pour récupérer, mettre à jour ou supprimer un Parent spécifique.
    Accès réservé au Parent authentifié.
    """
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [permissions.IsAuthenticated]


# -------------------- JobOffer Views --------------------

class JobOfferListCreateView(generics.ListCreateAPIView):
    """
    API pour lister et créer des offres d'emploi.
    Accès en lecture pour tous, mais création réservée aux Parents authentifiés.
    """
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Associe automatiquement le Parent connecté comme auteur de l'offre
        serializer.save(parent=self.request.user)


class JobOfferRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API pour récupérer, mettre à jour ou supprimer une offre d'emploi spécifique.
    Accès réservé au Parent propriétaire de l'offre.
    """
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Assure que seul le Parent propriétaire peut modifier l'offre
        if serializer.instance.parent != self.request.user:
            raise PermissionError("Vous n'avez pas la permission de modifier cette offre.")
        serializer.save()


# -------------------- Application Views --------------------

class ApplicationListCreateView(generics.ListCreateAPIView):
    """
    API pour lister et créer des candidatures.
    Accès en lecture pour tous, création ouverte à tout utilisateur.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.AllowAny]


class ApplicationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API pour récupérer, mettre à jour ou supprimer une candidature spécifique.
    Accès réservé au Parent propriétaire de l'offre liée.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Assure que seul le Parent propriétaire de l'offre liée peut modifier
        if serializer.instance.job.parent != self.request.user:
            raise PermissionError("Vous n'avez pas la permission de modifier cette candidature.")
        serializer.save()
