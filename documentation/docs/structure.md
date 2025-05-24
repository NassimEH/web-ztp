# Structure du projet

## Architecture globale

Web-ZTP est structuré autour de quatre composants principaux, chacun s'exécutant dans son propre conteneur Docker :

1. **Application Web Django** : Interface utilisateur et logique métier
2. **Serveur DHCP dédié** : Gestion des adresses IP et des options de configuration
3. **Proxy Caddy** : Sécurisation des communications HTTPS
4. **Base de données PostgreSQL** : Stockage des configurations et des données

Cette architecture en microservices permet une grande flexibilité et facilite la maintenance.

## Composants principaux

### Application Web

L'application Web Django est le cœur du système, elle gère :

- L'interface utilisateur avec des formulaires et tableaux de bord
- La gestion des templates de configuration ZTP
- L'administration des appareils réseau
- L'authentification des utilisateurs

### Serveur DHCP

Le serveur DHCP est responsable de :

- L'attribution automatique d'adresses IP aux équipements
- La configuration des options DHCP spécifiques à ZTP
- La redirection des appareils vers les fichiers de configuration appropriés

### Proxy Caddy

Le proxy inverse Caddy fournit :

- Support HTTPS automatique avec certificats auto-signés ou Let's Encrypt
- Protection contre certaines attaques web courantes
- Redirection du trafic vers l'application Django

### Base de données PostgreSQL

La base de données stocke :

- Les informations sur les équipements réseau
- Les templates de configuration
- Les paramètres du serveur DHCP
- Les données utilisateurs

## Structure des fichiers

Le projet est organisé de la façon suivante :

```
web-ztp/
├── app/                      # Application Django principale
│   ├── templates/            # Templates HTML pour l'interface web
│   ├── views/                # Vues Django (contrôleurs)
│   ├── models.py             # Modèles de données
│   ├── forms.py              # Formulaires web
│   └── formset.py            # Formsets pour les formulaires complexes
├── dhcp_server/              # Serveur DHCP personnalisé
│   └── dhcp_server.py        # Implémentation du serveur DHCP
├── webZtp/                   # Configuration du projet Django
├── docker-compose.yml        # Configuration des conteneurs Docker
├── Dockerfile                # Configuration du conteneur de l'application web
├── Dockerfile.dhcp           # Configuration du conteneur du serveur DHCP
└── Caddyfile                 # Configuration du proxy Caddy
```

## Flux de travail typique

Le fonctionnement typique de Web-ZTP suit le processus suivant :

1. L'administrateur crée un template de configuration via l'interface web
2. L'administrateur enregistre un nouvel équipement avec ses paramètres spécifiques
3. L'équipement est connecté au réseau et démarre pour la première fois
4. Le serveur DHCP attribue une adresse IP à l'équipement et lui fournit les options ZTP
5. L'équipement télécharge sa configuration personnalisée
6. L'équipement applique automatiquement la configuration