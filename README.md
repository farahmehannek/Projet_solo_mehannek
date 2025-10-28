# Getting Started with Create React App
 Projet SOLO — Catalogue Cyberpunk

Mehannek Farah
Date de dépôt : 28/10/2025

Description du projet
Projet Individuel 

Ce projet a été réalisé dans le cadre du Master Data & Intelligence Artificielle.
Il s’agit d’une application web complète combinant un backend Django et un frontend React, permettant de gérer et visualiser des données produits à travers une interface ergonomique.

 Technologies utilisées

Backend : Django (Python 3.10+)

Frontend : React.js (JavaScript ES6)

Base de données : SQLite3

Gestion de version : Git & GitHub

Environnement : Visual Studio Code

 Structure du projet
projet_individuel_farah/
│
├── backend/ ou boutique/   → application Django principale
│   ├── manage.py
│   ├── db.sqlite3
│   ├── produits/           → app Django gérant les produits
│   └── templates/          → pages HTML Django (si nécessaires)
│
├── frontend/               → application React
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── build/
│
└── README.md



Backend :

cd backend
pip install -r requirements.txt


Frontend :

cd frontend
npm install

Lancement du serveur Django

Depuis le dossier du backend :

python manage.py runserver

 Lancement du serveur React

Depuis le dossier du frontend :

npm start




 Description des pages
 Page 1 – Accueil

Présente une vue d’ensemble de l’application.

Contient une brève description du projet et un lien vers la liste des produits.

 Page 2 – Liste des produits

Affiche la liste complète des produits extraits de la base de données via l’API Django.

Permet de visualiser les détails de chaque produit.

Intégration React avec requêtes HTTP vers le backend.

Page 3 – Ajout / gestion des produits

Permet d’ajouter, modifier ou supprimer un produit.

Formulaire dynamique côté frontend, synchronisé avec l’API REST du backend.

Validation des champs avant envoi.

Fonctionnalités principales

Application web full-stack (frontend + backend).

API Django REST pour la communication entre les deux couches.

Gestion CRUD complète sur les produits.

Interface utilisateur réactive développée avec React.

Base de données légère (SQLite).

Commandes principales utilisées
 Django
django-admin startproject boutique
python manage.py startapp produits
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

 Git / GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/farahmehannek/projet_solo_mehannek.git
git push -u origin main

 React
npx create-react-app frontend
npm install axios react-router-dom
npm start
npm run build
