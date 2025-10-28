# produits/admin.py
# =================
# Ce fichier permet d'afficher les modèles (tables) dans le panneau d'administration.

from django.contrib import admin
from .models import Produit, Categorie

# On enregistre les modèles pour qu'ils soient visibles dans l'interface d'administration
admin.site.register(Categorie)
admin.site.register(Produit)
