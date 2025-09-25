from django.shortcuts import render

# Create your views here.

from django.http import Http404, HttpResponse, JsonResponse
from .models import Produit, Categorie, Rayon, Status
from django.views.generic import *


def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

def ma_vue(request):
    return JsonResponse({'foo': 'bar'})


def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

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

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        return context
    
class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['titreh1'] = "Contact us..."
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

class HomeParamView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        param = self.kwargs.get('param', 'Guest')  
        context['titreh1'] = "Hello " + param + " !"
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
    
class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"

    def get_queryset(self ) :
        return Produit.objects.order_by("prixUnitaireProd")
    
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
    
class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context

class CategorieListView(DetailView):
    model = Categorie
    template_name = "monApp/list_categorie.html"
    context_object_name = "ctgr"
    
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des catégories"
        return context
    
class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "ctgr"

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        return context
    

class StatusListView(DetailView):
    model = Status
    template_name = "monApp/list_status.html"
    context_object_name = "status"

    def get_context_data(self, **kwargs):
        context = super(StatusListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des statuts"
        return context
    
class StatusDetailView(DetailView):
    model = Status
    template_name = "monApp/detail_status.html"
    context_object_name = "status"

    def get_context_data(self, **kwargs):
        context = super(StatusDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        return context
    

class RayonListView(DetailView):
    model = Rayon
    template_name = "monApp/list_rayon.html"
    context_object_name = "rayon"

    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des rayons"
        return context
    
class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        return context