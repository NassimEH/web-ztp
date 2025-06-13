<p align="center">
    <img src="https://raw.githubusercontent.com/Chadi-Mangle/web-ztp/refs/heads/main/logo.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">WEB-ZTP</h1></p>
<p align="center">
    <em><code>❯ Fait par : Chadi, Nassim, Ilyes, Lucas</code></em>
</p>
<p align="center">
    <img src="https://img.shields.io/github/last-commit/Chadi-Mangle/web-ztp?style=default&logo=git&logoColor=white&color=0080ff" alt="Dernier commit">
    <img src="https://img.shields.io/github/languages/top/Chadi-Mangle/web-ztp?style=default&color=0080ff" alt="Langage principal">
    <img src="https://img.shields.io/github/languages/count/Chadi-Mangle/web-ztp?style=default&color=0080ff" alt="Nombre de langages">
</p>
<p align="center">
</p>
<p align="center">
</p>
<br>

##  Sommaire

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Structure du projet](#structure-du-projet)
- [Commencer](#commencer)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
  - [Utilisation](#utilisation)
- [Auteurs](#auteurs)
- [Informations](#informations)

---

##  Présentation

<code>❯ Notre projet propose une interface web complète intégrant un serveur DHCP que nous avons développé nous-mêmes, ainsi qu’une implémentation personnalisée de la fonctionnalité Zero Touch Provisioning (ZTP) day 0. Cette plateforme permet aux utilisateurs d’ajouter et de configurer des appareils de manière automatisée, en renseignant les paramètres requis via des formulaires dédiés. L’ensemble a été conçu pour offrir une expérience utilisateur optimale, avec une interface intuitive, épurée et ergonomique, garantissant une gestion efficace des équipements et une mise en réseau simplifiée.</code>

---

##  Fonctionnalités

<code>❯ Notre site web propose une navigation structurée à travers plusieurs menus, offrant une expérience fluide et intuitive. Parmi ces menus, on retrouve un **dashboard** central qui fournit une vue d’ensemble sur l’ensemble des configurations en place, permettant ainsi un suivi efficace et une gestion optimisée des équipements. Une **page "Configurer un appareil"** est également disponible, offrant aux utilisateurs la possibilité d’ajouter de nouveaux dispositifs en sélectionnant les configurations adaptées via une interface dédiée. Enfin, une **page d’aide** regroupe diverses informations et ressources essentielles pour accompagner les utilisateurs dans l’utilisation de la plateforme et la compréhension des fonctionnalités implémentées.</code>

---

##  Structure du projet

```sh
└── web-ztp/
    ├── .github
    │   └── workflows
    ├── Dockerfile
    ├── app
    │   ├── .dockerignore
    │   ├── Dockerfile
    │   ├── database_check.py
    │   ├── entrypoint.sh
    │   ├── manage.py
    │   ├── requirements.txt
    │   ├── core
    │   │    ├── templates
    │   │    │    └── core
    │   │    │        └── landing_page.html  
    │   │    ├── __init__.py
    │   │    ├── apps.Py
    │   │    ├── urls.py
    │   │    └── views.Py       
    │   ├── device
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py  
    │   ├── env
    │   │   ├── __init__.py
    │   │   └── config.py
    │   ├── monitoring
    │   │   ├── views
    │   │   │   └── healthcheck_views.py
    │   │   ├── __init__.py
    │   │   ├── apps.Py
    │   │   └── urls.py
    │   ├── static
    │   │   ├── css
    │   │   │     └── device_dashboards.css
    │   │   │          ├── me.css
    │   │   │          └── style.css
    │   │   ├── img
    │   │   │   └── favicon.png
    │   │   └── js
    │   │       ├── dhcp_slider.js
    │   │       └── me.js          
    │   ├── template
    │   │   ├── cotton
    │   │   │   ├── crispy_auth_form.html 
    │   │   │   ├── crispy_file_form.html
    │   │   │   ├── crispy_form.html
    │   │   │   └── device_row.html
    │   │   ├── 403.html
    │   │   ├── 404.html
    │   │   ├── 429.html
    │   │   ├── 500.html
    │   │   └── base.html                     
    │   ├── user
    │   │   ├── migrations
    │   │       ├── 0001_inital.py    
    │   │       └── __init__.py
    │   │   ├── templates/user
    │   │       ├── login.html
    │   │       ├── me.html
    │   │       └── signup.html
    │   │   ├── views
    │   │   │   ├── custom_auth_views.py
    │   │   │   └── profile_views.py
    │   │   ├── __init__.py
    │   │   ├── _forms.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   └── urls.Py   
    │   └── webZtp
    │       ├── __init__.py
    │       ├── asgi.py
    │       ├── settings.Py
    │       ├── urls.py
    │       └── wsgi.py  
    ├── caddy
    │   ├── Caddyfile.tmpl
    │   └── Dockerfile
    ├── exemple_ztp_config
        └── ztp-debug.py
    ├── .env-example
    ├── .gitignore
    ├── README.md
    └──  docker-compose.yml

```

---
##  Commencer

###  Pré-requis

Vous aurez besoin de ces technologies :

- **Technologie de conteneurisation:** Docker
- **Système de gestion:** Git
- **Langage de programmation:** Python (Version recommandée >3.10)  


###  Installation

Installer le projet :

1. Clonez le dépôt :

```sh
❯ git clone https://github.com/Chadi-Mangle/web-ztp
```

2. Allez dans le bon dossier :
```sh
❯ cd web-ztp
```

###  Utilisation

**En utilisant `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker compose up --build -d
```

### Information

On a remarqué que le docker compose ne fonctionne pas sur Windows ni sur Alma Linux (fonctionne sur Linux et pas Windows). on essaiera de corriger ce problème de compatibilité pour le S6. En attendant, si vous êtes sur Windows ou Alma Linux utilisez WSL. Si vous êtes sur Linux, le docker fonctionne.

### Alternative

Vous pouvez aussi utiliser les commandes suivantes pour run l'application : 

```sh
❯ python manage.py migrate
```
```sh
❯ python manage.py loaddata dhcp_config.json
```
```sh
❯ python manage.py runserver
```
Si vous voulez charger des configs ZTP depuis Windows, exécutez cette commande en admin :
```sh
❯ python manage.py rundhcp
```

## Auteurs

- Nassim El Haddad
- Chadi Manglé
- Ilyes Belkhir
- Lucas Dréano

---

##  Information

- Ce projet est réalisé dans le cadre de notre cursus ingénieur à Télécom SudParis

---
