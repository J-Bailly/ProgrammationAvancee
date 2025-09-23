from django.urls import path
from .import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/<param>", views.home_param, name="home_param"),
    path("contactUs", views.contact_us, name="contact_us"),
    path("aboutUs", views.about_us, name="about_us"),
    path("listeProduits/",views.ListProduits, name="liste_produit"),
    path("listeCategories/",views.ListCategories, name="liste_categorie"),
    path("listeStatus/",views.ListStatut, name="liste_statut"),
    path("listeRayons/",views.ListRayons, name="liste_rayon"),
]