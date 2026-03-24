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
- Mouhamet THIAM → Authentification & Sécurité
- Mael Maela KOUTOGLO → Module Students
- Régine GAO TAO Fouka → Module Teachers
- Hilly Maryse OKANA → Module Courses
- Reine Sandra SEH → Dashboard & UI

---

## Fonctionnalités
### Authentification & Sécurité
Le module Auth permet de sécuriser l’accès à l’application et de contrôler les actions des utilisateurs.
- Inscription utilisateur : Permet de créer un nouveau compte utilisateur.
- Authentification (Connexion / Déconnexion) : Permet à un utilisateur d’accéder ou de quitter l’application en toute sécurité.
- Gestion des rôles : Chaque utilisateur possède un rôle : Administrateur ou Utilisateur
- Gestion de session avec expiration automatique : La session expire automatiquement après une période d’inactivité.
- Protection des routes (login_required) : Certaines pages nécessitent que l’utilisateur soit connecté.
- Gestion des accès ( admin_required) : Certaines actions sont réservées à l’administrateur comme la suppression d’étudiant
---
### Gestion des étudiants
Le module Students permet une gestion complète des étudiants avec des fonctionnalités avancées visant à améliorer l’expérience utilisateur et la qualité des données.
Le module Students permet de gérer les étudiants et leurs informations au sein de l’application.
- Liste des étudiants : Permet d’afficher tous les étudiants avec une interface claire et paginée.
- Ajout d’un étudiant : Permet de créer un étudiant avec validation de l’email (user@domaine.extension) et génération automatique d’un identifiant unique.
- Modification d’un étudiant : Permet de modifier les informations (nom, email) avec vérification des doublons et validation des données.
- Suppression d’un étudiant : Permet de supprimer un étudiant (action réservée à l’administrateur) avec confirmation.
- Recherche d’étudiant : Permet de rechercher un étudiant par son nom.
- Pagination : Permet de limiter l’affichage à 3 étudiants par page avec une navigation entre les pages.
- Gestion du statut : Permet de définir un étudiant comme actif ou inactif et de modifier son statut.
- Consultation des cours : Permet de voir les cours associés à un étudiant.
- Gestion des images : Permet d’ajouter une photo via une URL ou de générer automatiquement un avatar.
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
### Dashboard et UI
- Créer les interfaces: Mise en place des différentes interfaces de l’application à l’aide de templates HTML et de Tailwind CSS. Création d’un layout global avec base.html  incluant une sidebar pour la navigation et une topbar affichant l’utilisateur connecté. Développement des pages principales (dashboard, listes, formulaires) avec un design cohérent. Utilisation de url_for pour la gestion des liens entre les différentes routes de l’application.
- Nombre total d’étudiants:Calcul et affichage dynamique du nombre total d’étudiants à partir des données stockées dans l’application, puis intégration de cette valeur dans le dashboard sous forme de carte statistique.
- Nombre total d’enseignants: Récupération du nombre total d’enseignants et affichage dans le dashboard via une carte dédiée.
- Nombre total de cours:Calcul du nombre total de cours enregistrés et affichage dans le dashboard.
- Statistiques avancées: Mise en place de calculs supplémentaires à partir des données existantes, notamment: identification du cours ayant le plus d’étudiants, détermination de l’enseignant ayant le plus de cours assignés

---

## Architecture du projet
edu_crm/
│
├── .venv/
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
Ensuite, modifier les valeurs dans le fichier `.env` selon la configuration.
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
