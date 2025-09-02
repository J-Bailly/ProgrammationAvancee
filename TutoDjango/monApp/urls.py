from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ContactUs", views.home, name="contact_us"),
    path("AboutUs", views.home, name="about_us"),
]