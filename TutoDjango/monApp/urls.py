from django.urls import path
from .import views
from django.views.generic import *

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("home/<param>", views.home_param, name="home_param"),
    path("contactUs", views.ContactView.as_view(), name="contact_us"),
    path("aboutUs", views.AboutView.as_view(), name="about_us"),
    path("listeProduits/",views.ListProduits, name="liste_produit"),
    path("listeCategories/",views.ListCategories, name="liste_categorie"),
    path("listeStatus/",views.ListStatut, name="liste_statut"),
    path("listeRayons/",views.ListRayons, name="liste_rayon"),
    path("home", TemplateView.as_view(template_name="monApp/page_home.html")),
]