from django.shortcuts import render

# Create your views here.

from django.http import Http404, HttpResponse, JsonResponse
from .models import Produit, Categorie, Rayon, Status

def home(request):
    if request.GET and request.GET["test"]:
        raise Http404
    return HttpResponse("Bonjour Monde!")

def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

def ma_vue(request):
    return JsonResponse({'foo': 'bar'})

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
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})
    # prdts = Produit.objects.all()
    # liste = "<ul>"
    # for produit in prdts:
    #     liste += f"""<li> {produit.intituleProd} </li>"""
    # liste += "</ul>"
    # return HttpResponse(liste)

def ListCategories(request):
    ctgrs = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html',{'ctgrs': ctgrs})
    # liste = "<ul>"
    # for categorie in ctgrs:
    #     liste += f"""<li> {categorie.nomCat} </li>"""
    # liste += "</ul>"
    # return HttpResponse(liste)

def ListStatut(request):
    status = Status.objects.all()
    return render(request, 'monApp/list_status.html',{'statuts': status})
    # liste = "<ul>"
    # for produit in prdts:
    #     liste += f"""<li> {produit.status.lbStatus} </li>"""
    # liste += "</ul>"
    # return HttpResponse(liste)

def ListRayons(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html',{'rayons': rayons})