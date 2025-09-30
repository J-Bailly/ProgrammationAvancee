from django.urls import path
from .import views
from django.views.generic import *

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("home/<param>", views.HomeParamView.as_view(), name="home_param"),

    path("emailsent/", views.EmailSentView.as_view(), name="email-sent"),

    path("contact/", views.ContactView, name="contact_us"),

    path("about/", views.AboutView.as_view(), name="about_us"),

    path("listeProduits/",views.ProduitListView.as_view(),name="lst_prdts"),
    path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),

    path("listeCategories/",views.CategorieListView.as_view(), name="lst_ctgrs"),
    path("categorie/<pk>/",views.CategorieDetailView.as_view(), name="dtl_ctgr"),

    path("listeStatus/",views.StatusListView.as_view(), name="lst_status"),
    path("status/<pk>/",views.StatusDetailView.as_view(), name="dtl_status"),

    path("listeRayons/",views.RayonListView.as_view(), name="lst_rayons"),
    path("rayon/<pk>/",views.RayonDetailView.as_view(), name="dtl_rayon"),

    path("home", TemplateView.as_view(template_name="monApp/page_home.html")),

    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
]