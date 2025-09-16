from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Produit, Categorie

def home(request):
    return HttpResponse("<h1>Bonjour !</h1>")
def home_param(request, param):
    return HttpResponse("<h1>Bonjour " + param + " !</h1>")
def contact_us(request):
    return HttpResponse(
        "<h1>Contact Us!</h1>" \
        "<form> Test </form>")

def about_us(request):
    return HttpResponse(
        "<h1>About Us!</h1>" \
        "<p>Test</p>"
    )

def ListProduits(request):
    prdts = Produit.objects.all()
    liste = "<ul>"
    for produit in prdts:
        liste += f"""<li> {produit.intituleProd} </li>"""
    liste += "</ul>"
    return HttpResponse(liste)

def ListCategories(request):
    ctgrs = Categorie.objects.all()
    liste = "<ul>"
    for categorie in ctgrs:
        liste += f"""<li> {categorie.nomCat} </li>"""
    liste += "</ul>"
    return HttpResponse(liste)

def ListStatut(request):
    prdts = Produit.objects.all()
    liste = "<ul>"
    for produit in prdts:
        liste += f"""<li> {produit.status.lbStatus} </li>"""
    liste += "</ul>"
    return HttpResponse(liste)