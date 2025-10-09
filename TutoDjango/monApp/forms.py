from django import forms
from django.shortcuts import render
from .models import Produit, Categorie, Status, Rayon

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        #fields = '__all__'
        exclude = ('categorie', 'status')

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        #fields = '__all__'
        exclude = ('produit', 'status')


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        #fields = '__all__'
        exclude = ('produit', 'categorie')


class RayonForm(forms.ModelForm):
    class Meta:
        model = Rayon
        #fields = '__all__'
        exclude = ('produit', 'status', 'categorie')