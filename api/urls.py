from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterParentView,
    ParentListCreateView,
    ParentRetrieveUpdateDestroyView,
    JobOfferListCreateView,
    JobOfferRetrieveUpdateDestroyView,
    ApplicationListCreateView,
    ApplicationRetrieveUpdateDestroyView,
)



urlpatterns = [
    # Authentification
    path("auth/register/", RegisterParentView.as_view(), name="parent-register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    # Parents
    path("parents/", ParentListCreateView.as_view(), name="parent-list-create"),
    path("parents/<int:pk>/", ParentRetrieveUpdateDestroyView.as_view(), name="parent-detail"),

    # Job Offers
    path("job-offers/", JobOfferListCreateView.as_view(), name="joboffer-list-create"),
    path("job-offers/<int:pk>/", JobOfferRetrieveUpdateDestroyView.as_view(), name="joboffer-detail"),

    # Applications
    path("applications/", ApplicationListCreateView.as_view(), name="application-list-create"),
    path("applications/<int:pk>/", ApplicationRetrieveUpdateDestroyView.as_view(), name="application-detail"),
]
