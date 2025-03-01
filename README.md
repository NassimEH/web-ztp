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

- [ Présentation ](#-overview)
- [ Fonctionnalités ](#-features)
- [ Structure du projet ](#-project-structure)
- [ Commencer](#-getting-started)
  - [ Prérequis ](#-prerequisites)
  - [ Installation](#-installation)
  - [ Utilisation](#-usage)
- [ Auteurs ](#-contributing)
- [ Informations ](#-acknowledgments)

---

##  Présentation

<code>❯ Notre projet propose une interface web complète intégrant un serveur DHCP que nous avons développé nous-mêmes, ainsi qu’une implémentation personnalisée de la fonctionnalité Zero Touch Provisioning (ZTP). Cette plateforme permet aux utilisateurs d’ajouter et de configurer des appareils de manière automatisée, en renseignant les paramètres requis via des formulaires dédiés. L’ensemble a été conçu pour offrir une expérience utilisateur optimale, avec une interface intuitive, épurée et ergonomique, garantissant une gestion efficace des équipements et une mise en réseau simplifiée.</code>

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
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── generator
    │   ├── management
    │   ├── migrations
    │   ├── models.py
    │   ├── static
    │   ├── templates
    │   ├── templatetags
    │   ├── tests.py
    │   ├── url.py
    │   ├── utils
    │   └── views
    ├── dhcp_server
    │   ├── __init.py__
    │   ├── dhcp_db.py
    │   ├── dhcp_server.py
    │   ├── django_setup.py
    │   └── requirements.txt
    ├── docker-compose-exemple.yml
    ├── docker-compose.yml
    ├── entrypoint.py
    ├── manage.py
    ├── requirements.txt
    └── webZtp
        ├── __init__.py
        ├── asgi.py
        ├── log_views.html
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

---
##  Commencer

###  Pré-requis

Vous aurez besoin de ces technologies :

- **Technologie de conteneurisation:** Docker


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

### Alternative 

On a remarqué que le docker compose ne fonctionne pas sur Windows (fonctionne sur Linux et pas Windows). on essaiera de corriger ce problème de compatibilité pour le S6. En attendant, si vous testez sur Windows et que le docker-compose ne fonctionne pas, une fois dans le bon répertoire, exécutez votre PowerShell avec les droits administrateurs et faites : 

```sh
❯ python manage.py runserver
```
```sh
❯ python manage.py migrate
```
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
