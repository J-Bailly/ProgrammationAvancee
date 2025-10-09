from itertools import count
from django.forms import BaseModelForm
from django.shortcuts import render

# Create your views here.

from django.http import Http404, HttpResponse, JsonResponse
from django.urls import reverse_lazy

from .forms import ContactUsForm, ProduitForm, CategorieForm, RayonForm, StatusForm
from .models import Produit, Categorie, Rayon, Status
from django.views.generic import *
from django.contrib.auth.views import *
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.db.models import Count


def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

def ma_vue(request):
    return JsonResponse({'foo': 'bar'})

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

def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monprojet.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html",{'titreh1':titreh1, 'form':form})

class EmailSentView(TemplateView):
    template_name = "monApp/page_email_sent.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmailSentView, self).get_context_data(**kwargs)
        context['message'] = "Votre email a bien été envoyé !"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)

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

    # def get_queryset(self ) :
    #     return Produit.objects.order_by("prixUnitaireProd")
    
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
    
def ProduitCreate(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            prdt = form.save()
            return redirect('dtl_prdt', prdt.refProd)
    else:
        form = ProduitForm()
    return render(request, "monApp/create_produit.html", {'form': form})

class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

class ProduitUpdateView(UpdateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/update_produit.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

def ProduitUpdate(request, pk):
    prdt = Produit.objects.get(refProd=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=prdt)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('dtl_prdt', prdt.refProd)
    else:
        form = ProduitForm(instance=prdt)
    return render(request,'monApp/update_produit.html', {'form': form})

class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')

def produit_delete(request, pk):
    prdt = Produit.objects.get(refProd=pk) # nécessaire pour GET et pour POST
    if request.method == 'POST':
        # supprimer le produit de la base de données
        prdt.delete()
        # rediriger vers la liste des produit
        return redirect('dlt_prdt')
    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    return render(request, 'monApp/delete_produit.html', {'object': prdt})             

class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "ctgrs"
    
    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('categorie'))
    
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories"
        return context
    
class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "ctgr"

    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('categorie'))
    
    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['prdts'] = self.object.categorie.all()
        return context

def CategorieCreate(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            ctgr = form.save()
            return redirect('dtl_ctgr', ctgr.idCat)
    else:
        form = ProduitForm()
    return render(request, "monApp/create_categorie.html", {'form': form})

class CategorieCreateView(CreateView):
    model = Categorie
    form_class= CategorieForm
    template_name = "monApp/create_categorie.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ctgr = form.save()
        return redirect('dtl_ctgr', ctgr.idCat)

class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/update_categorie.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ctgr = form.save()
        return redirect('dtl_ctgr', ctgr.idCat)

def CategorieUpdate(request, pk):
    ctgr = Categorie.objects.get(idCat=pk)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=ctgr)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('dtl_ctgr', ctgr.idCat)
    else:
        form = CategorieForm(instance=ctgr)
    return render(request,'monApp/update_categorie.html', {'form': form})

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_ctgrs')

def categorie_delete(request, pk):
    ctgr = Categorie.objects.get(idCat=pk) # nécessaire pour GET et pour POST
    if request.method == 'POST':
        # supprimer le produit de la base de données
        ctgr.delete()
        # rediriger vers la liste des produit
        return redirect('dlt_ctgr')
    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    return render(request, 'monApp/delete_categorie.html', {'object': ctgr})





class StatusListView(ListView):
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
    
def StatusCreate(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save()
            return redirect('dtl_status', status.idStatus)
    else:
        form = StatusForm()
    return render(request, "monApp/create_status.html", {'form': form})

class StatusCreateView(CreateView):
    model = Status
    form_class= StatusForm
    template_name = "monApp/create_status.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        status = form.save()
        return redirect('dtl_status', status.idStatus)

class StatusUpdateView(UpdateView):
    model = Status
    form_class=StatusForm
    template_name = "monApp/update_status.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        status = form.save()
        return redirect('dtl_status', status.idStatus)

def StatusUpdate(request, pk):
    status = Status.objects.get(idStatus=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('dtl_status', status.idStatus)
    else:
        form = StatusForm(instance=status)
    return render(request,'monApp/update_status.html', {'form': form})

class StatusDeleteView(DeleteView):
    model = Status
    template_name = "monApp/delete_status.html"
    success_url = reverse_lazy('lst_status')

def status_delete(request, pk):
    status = Status.objects.get(idStatus=pk) # nécessaire pour GET et pour POST
    if request.method == 'POST':
        # supprimer le produit de la base de données
        status.delete()
        # rediriger vers la liste des produit
        return redirect('dlt_status')
    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    return render(request, 'monApp/delete_status.html', {'object': status})





class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"

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

def RayonCreate(request):
    if request.method == 'POST':
        form = RayonForm(request.POST)
        if form.is_valid():
            rayon = form.save()
            return redirect('dtl_rayon', rayon.idRayon)
    else:
        form = RayonForm()
    return render(request, "monApp/create_rayon.html", {'form': form})

class RayonCreateView(CreateView):
    model = Rayon
    form_class= RayonForm
    template_name = "monApp/create_rayon.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)

class RayonUpdateView(UpdateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/update_rayon.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)

def RayonUpdate(request, pk):
    rayon = Rayon.objects.get(idRayon=pk)
    if request.method == 'POST':
        form = RayonForm(request.POST, instance=rayon)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('dtl_rayon', rayon.idRayon)
    else:
        form = RayonForm(instance=rayon)
    return render(request,'monApp/update_rayon.html', {'form': form})

class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rayons')

def rayon_delete(request, pk):
    rayon = Rayon.objects.get(idRayon=pk) # nécessaire pour GET et pour POST
    if request.method == 'POST':
        # supprimer le produit de la base de données
        rayon.delete()
        # rediriger vers la liste des produit
        return redirect('dlt_rayon')
    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    return render(request, 'monApp/delete_rayon.html', {'object': rayon})





class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'
    
    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')

class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')

class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)