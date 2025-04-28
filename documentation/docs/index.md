# WEB-ZTP

<p align="center">
    <img src="https://raw.githubusercontent.com/Chadi-Mangle/web-ztp/refs/heads/main/logo.png" align="center" width="30%">
</p>

## Bienvenue dans la documentation de WEB-ZTP

WEB-ZTP est une interface web complète intégrant un serveur DHCP développé en interne, ainsi qu'une implémentation personnalisée de la fonctionnalité Zero Touch Provisioning (ZTP). Cette plateforme permet aux utilisateurs d'ajouter et de configurer des appareils de manière automatisée via une interface intuitive et ergonomique.

### Fonctionnalités principales

- **Dashboard** : Vue d'ensemble des configurations en place
- **Configuration d'appareils** : Ajout et configuration automatisée d'appareils
- **Serveur DHCP intégré** : Gestion complète des adresses IP
- **ZTP (Zero Touch Provisioning)** : Configuration automatique des équipements
- **Interface intuitive** : Navigation fluide et ergonomique

### Dernières mises à jour

- Migration vers PostgreSQL pour la production
- Amélioration de la sécurité avec HTTPS
- Optimisation des performances du serveur DHCP

### Commencer rapidement

```bash
# Installation avec Docker
docker compose up --build -d

# Installation manuelle
python manage.py migrate
python manage.py loaddata dhcp_config.json
python manage.py runserver
```

### Auteurs

- Nassim El Haddad
- Chadi Manglé
- Ilyes Belkhir
- Lucas Dréano

---

Ce projet est réalisé dans le cadre du cursus ingénieur à Télécom SudParis.