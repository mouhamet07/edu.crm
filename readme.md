# Edu.CRM – Application de gestion scolaire (Flask)
## Description
**Edu.CRM** est une application web développée avec le framework **Flask** dans le cadre d’un projet académique.  
Elle permet de gérer les informations liées aux **étudiants**, **enseignants** et **cours**, tout en intégrant un système d’**authentification sécurisé** et un **dashboard statistique interactif**.
L’objectif principal du projet est de concevoir une application web modulaire, claire et maintenable en appliquant les bonnes pratiques de développement avec Flask.
Grâce à cette application, un utilisateur peut :
- gérer les étudiants (ajouter, modifier, supprimer, consulter)
- gérer les enseignants et leurs spécialités
- créer et organiser les cours
- attribuer des enseignants à des cours
- inscrire des étudiants à des cours
- consulter des statistiques globales via un tableau de bord
- accéder aux fonctionnalités selon son rôle (admin ou utilisateur)
- utiliser une application sécurisée avec gestion de session

---

## Concepts techniques utilisés
### Application Factory
Le projet utilise le design pattern **Application Factory**, qui consiste à créer l’application Flask via une fonction dédiée.
Ce principe permet :
- de configurer facilement l’application
- de séparer la création de l’application de son exécution
- de rendre le projet plus flexible
- de faciliter les tests
- d’enregistrer les modules (blueprints) de manière organisée
---
### Blueprints
L’application est organisée en plusieurs modules appelés **Blueprints**, chacun représentant une fonctionnalité spécifique.
Chaque module possède ses propres routes, templates et logique métier.
#### Exemple de modules :
- **auth** :  gestion de l’authentification
- **students** : gestion des étudiants
- **teachers** : gestion des enseignants
- **courses** : gestion des cours
- **dashboard** : statistiques
#### Avantages :
- meilleure organisation du code
- séparation claire des fonctionnalités
- maintenance plus simple
- développement en équipe facilité
---
### Séparation des responsabilités (Routes / Services)
Le projet applique le principe de séparation des responsabilités afin de rendre le code plus lisible et maintenable.
#### Routes
Les routes définissent les URLs de l’application et gèrent les interactions avec l’utilisateur (formulaires, affichage des pages).
#### Services
Les services contiennent la logique métier :
- traitement des données
- validation
- règles de gestion
- sécurité
#### Avantages :
- code plus structuré
- logique métier réutilisable
- maintenance facilitée
- meilleure lisibilité

---

## Membres du groupe et répartition des tâches
Mouhamet THIAM→ Authentification & Sécurité
Étudiant 2 → Module Students
Régine GAO TAO Fouka → Module Teachers
Hilly Maryse OKANA → Module Courses
Étudiant 5 → Dashboard & UI

---

## Fonctionnalités
### Authentification & Sécurité
Le module Auth permet de sécuriser l’accès à l’application et de contrôler les actions des utilisateurs.
-Inscription utilisateur : Permet de créer un nouveau compte utilisateur.
- Authentification (Connexion / Déconnexion) : Permet à un utilisateur d’accéder ou de quitter l’application en toute sécurité.
- Gestion des rôles : Chaque utilisateur possède un rôle : Administrateur ou Utilisateur
- Gestion de session avec expiration automatique : La session expire automatiquement après une période d’inactivité.
- Protection des routes (login_required) : Certaines pages nécessitent que l’utilisateur soit connecté.
- Gestion des accès ( admin_required) : Certaines actions sont réservées à l’administrateur comme la suppression d’étudiant
---
### Gestion des étudiants
- Liste des étudiants
- Ajout d’un étudiant
- Suppression d’un étudiant
- Modification d’un étudiant
- Recherche par nom
- Statut (actif / inactif)
- Date d’inscription
- Affichage des cours d’un étudiant
---
### Gestion des enseignants
- Liste des enseignants
- Ajout d’un enseignant
- Suppression
- Modification
- Filtrage par spécialité
- Nombre de cours assignés
- Consultation des cours
---
### Gestion des cours
Le module Courses permet de créer et organiser les cours en y affectant des enseignants et des étudiants.
- Liste des cours
- Création d’un cours : Possibilité de créer un cours en l’assignant à un professeur ou non
- Assignation d’un cours à un professeur
- Suppression d’un cours
-Recherche d’un cours
- Modification d’un cours : Possibilité de modifier le titre du cours ou le professeur 
- Assignation d’un étudiant à un cours
- Retrait d’un étudiant à un cours
- Détails d’un cours
- Nombre d’étudiants par cours
- Liste des étudiants inscrits dans un cours
---
### Dashboard
- Nombre total d’étudiants
- Nombre total d’enseignants
- Nombre total de cours
- Statistiques avancées
- Graphiques
- Interface responsive

---

## Architecture du projet
edu_crm/
│
├── app/
│ ├── init.py (Application Factory)
│ ├── auth/ (Blueprint Auth)
│ ├── students/ (Blueprint Students)
│ ├── teachers/ (Blueprint Teachers)
│ ├── courses/ (Blueprint Courses)
│ ├── dashboard/ (Blueprint Dashboard)
│ ├── services/ (Logique métier)
│ ├── templates/ (HTML Jinja2)
│
├── .env.example
├── config.py
├── run.py
├── requirements.txt
└── README.md

---

## Installation et exécution
### 1. Cloner le projet
```bash
git clone https://github.com/mouhamet07/edu-crm.git
cd edu-crm
````
### 2. Créer un environnement virtuel
```bash
python -m venv .venv
```
---
### 3. Activer l’environnement virtuel
#### Windows (PowerShell)
```bash
.venv\Scripts\activate
```
#### Linux / Mac
```bash
source .venv/bin/activate
```
---
### 4. Installer les dépendances
```bash
pip install -r requirements.txt
```
---
### 5. Configurer les variables d’environnement
Copier le fichier exemple :
#### Windows 
```bash
copy .env.example .env
```
#### Linux / Mac
```bash
cp .env.example .env
```
Ensuite, modifier les valeurs dans le fichier `.env` selon votre configuration.
Exemple :
```env
SECRET_KEY=dev
FLASK_ENV=development
PERMANENT_SESSION_LIFETIME=60
```
---
### 6. Lancer l’application
```bash
flask run
```
---
### 7. Accéder à l’application
Ouvrir dans le navigateur :
http://127.0.0.1:5000
---



