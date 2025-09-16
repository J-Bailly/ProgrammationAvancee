from datetime import date
from django.db import models

class Categorie(models.Model):
    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=100)

    def __str__(self):
        return self.nomCat

class Status(models.Model):
    idStatus = models.AutoField(primary_key=True)
    lbStatus = models.CharField(max_length=100)

class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    # Relation CIF : chaque produit appartient à 1 catégorie (0,N côté catégorie 1,1 côté produit)→
    dateFabProd = models.DateField(default=date.today)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="categorie",null=True, blank=True)
    rayons = models.ManyToManyField(
        "Rayon",
        through="Contenir",
        blank=True
    )
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status", null=True, blank=True)
    def __str__(self):
        return self.intituleProd
    
class Rayon(models.Model):
    idRayon = models.AutoField(primary_key=True)
    nomRayon = models.CharField(max_length=100)
    produits = models.ManyToManyField(
        "Produit",
        through="Contenir",
        blank=True
    )

class Contenir(models.Model):
    Rayon = models.ForeignKey(Rayon, on_delete=models.CASCADE, related_name="rayon")
    Produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="produit")
    Qte = models.IntegerField()

