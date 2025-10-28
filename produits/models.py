from django.db import models

class Categorie(models.Model):
    """Catégorie de produits (ex : ordinateurs, téléphones, accessoires)"""
    nom = models.CharField(max_length=50, verbose_name="Nom de la catégorie")

    def __str__(self):
        return self.nom


class Produit(models.Model):
    """Produit disponible dans le catalogue"""
    nom = models.CharField(max_length=100, verbose_name="Nom du produit")
    description = models.TextField(blank=True, null=True, verbose_name="Description du produit")  # ✅ champ optionnel
    prix = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix (€)")
    image = models.URLField(blank=True, null=True, verbose_name="Image (URL)")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name="Catégorie")

    def __str__(self):
        return self.nom
