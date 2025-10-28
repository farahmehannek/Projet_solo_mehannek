# produits/urls.py
# ==================
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('produit/<int:id>/', views.produit_detail, name='produit_detail'),

    # --- API pour React ---
    path('api/produits/', views.api_produits, name='api_produits'),
    path('api/categories/', views.api_categories, name='api_categories'),
]
