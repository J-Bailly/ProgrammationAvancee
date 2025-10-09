from django.urls import path
from .import views
from . import forms
from django.views.generic import *

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("home/<param>", views.HomeParamView.as_view(), name="home_param"),

    path("emailsent/", views.EmailSentView.as_view(), name="email-sent"),

    path("contact/", views.ContactView, name="contact_us"),

    path("about/", views.AboutView.as_view(), name="about_us"),

    path("listeProduits/",views.ProduitListView.as_view(),name="lst_prdts"),
    path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
    path("produit/",views.ProduitCreateView.as_view(), name="crt_prdt"),
    path("produit/<pk>/update/",views.ProduitUpdateView.as_view(), name="chng_prdt"),
    path("produit/<pk>/delete/",views.ProduitDeleteView.as_view(), name="dlt_prdt"),

    path("listeCategories/",views.CategorieListView.as_view(), name="lst_ctgrs"),
    path("categorie/<pk>/",views.CategorieDetailView.as_view(), name="dtl_ctgr"),
    path("categorie/",views.CategorieCreateView.as_view(), name="crt_ctgr"),
    path("categorie/<pk>/update/",views.CategorieUpdateView.as_view(), name="chng_ctgr"),
    path("categorie/<pk>/delete/",views.CategorieDeleteView.as_view(), name="dlt_ctgr"),

    path("listeStatus/",views.StatusListView.as_view(), name="lst_status"),
    path("status/<pk>/",views.StatusDetailView.as_view(), name="dtl_status"),
    path("status/",views.StatusCreateView.as_view(), name="crt_status"),
    path("status/<pk>/update/",views.StatusUpdateView.as_view(), name="chng_status"),
    path("status/<pk>/delete/",views.StatusDeleteView.as_view(), name="dlt_status"),

    path("listeRayons/",views.RayonListView.as_view(), name="lst_rayons"),
    path("rayon/<pk>/",views.RayonDetailView.as_view(), name="dtl_rayon"),
    path("rayon/",views.RayonCreateView.as_view(), name="crt_rayon"),
    path("rayon/<pk>/update/",views.RayonUpdateView.as_view(), name="chng_rayon"),
    path("rayon/<pk>/delete/",views.RayonDeleteView.as_view(), name="dlt_rayon"),

    path("home", TemplateView.as_view(template_name="monApp/page_home.html")),

    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
]