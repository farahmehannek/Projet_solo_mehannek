from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Produit, Categorie


# 🏠 Page d'accueil
def accueil(request):
    """Affiche la page d'accueil"""
    return render(request, 'produits/accueil.html')


# 🛒 Catalogue avec filtres
def catalogue(request):
    """Affiche le catalogue avec filtres"""
    categorie_id = request.GET.get('categorie')
    prix_max = request.GET.get('prix_max')

    produits = Produit.objects.all()
    if categorie_id:
        produits = produits.filter(categorie_id=categorie_id)
    if prix_max:
        produits = produits.filter(prix__lte=prix_max)

    categories = Categorie.objects.all()
    return render(request, 'produits/catalogue.html', {
        'produits': produits,
        'categories': categories,
    })


# 🔍 Page détail produit
def produit_detail(request, id):
    """Page détail d'un produit"""
    produit = get_object_or_404(Produit, id=id)
    return render(request, 'produits/detail.html', {'produit': produit})


# 🧠 API REST pour React
def api_produits(request):
    """Renvoie la liste des produits au format JSON pour le frontend React"""
    produits = list(Produit.objects.values('id', 'nom', 'prix', 'image', 'categorie_id'))
    return JsonResponse(produits, safe=False)


def api_categories(request):
    """Renvoie la liste des catégories au format JSON pour le frontend React"""
    categories = list(Categorie.objects.values('id', 'nom'))
    return JsonResponse(categories, safe=False)

