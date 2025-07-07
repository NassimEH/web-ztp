# Structure du projet

## Architecture globale

Web-ZTP est structuré autour de quatre composants principaux, chacun s'exécutant dans son propre conteneur Docker :

1. **Application WebZTP Django** : Interface utilisateur et logique métier
2. **Serveur DHCP dédié** : Gestion des adresses IP et des options de configuration
3. **Proxy Caddy** : Sécurisation des communications HTTPS
4. **Base de données PostgreSQL** : Stockage des configurations et des données

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
- Sert les fichiers statiques vers l'utilisateurs
- Redirection du trafic vers l'application Django

### Base de données PostgreSQL

La base de données stocke :

- Les informations sur les équipements réseau
- Les templates de configuration
- Les paramètres du serveur DHCP
- Les données utilisateurs

## Structure des fichiers

Le projet est organisé de la façon suivante :

```bash
web-ztp/
├── .env                  # Fichier d’environnement
├── docker-compose.yml    # Lancement des conteneurs
├── app/
│   ├── core/             # Pages générales (dashboard, privacy, etc.)
│   ├── device/           # Gestion des devices et templates
│   ├── dhcp_server/      # Script ZTP DHCP simulé
│   ├── user/             # Gestion des utilisateurs
│   ├── webZtp/           # Paramètres Django (settings, urls, etc.)
│   ├── templates/        # HTML génériques et partiels
│   ├── env/              # Configuration Python
│   ├── monitoring/       # Healthcheck de l’application
│   ├── utils/            # Fonctions utilitaires (DHCP, formulaires, devices)
├── caddy/                # Reverse proxy avec Caddy
├── exemple_dhcp_discover/   # Script de test DHCP
├── exemple_ztp_config/      # Script de debug ZTP

```
