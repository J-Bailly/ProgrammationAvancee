from django.urls import path
from .import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/<param>", views.home_param, name="home_param"),
    path("ContactUs", views.contact_us, name="contact_us"),
    path("AboutUs", views.about_us, name="about_us"),
]