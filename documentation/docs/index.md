# Web-ZTP

<p align="center">
    <img src="img/logo.png" align="center" width="30%" alt="Logo Web-ZTP">
</p>

# Bienvenue sur le projet ZTP

ZTP, ou **Zero Touch Provisioning**, est une méthode d'automatisation du déploiement de périphériques réseau. Elle permet de configurer automatiquement les équipements sans intervention humaine dès leur mise sous tension.

## Contexte du projet

Ce projet a été réalisé dans le cadre d'un travail étudiant par :

- **Chadi MANGLE-DJIRO**
- **Nassim EL HADDAD**
- **Lucas DREANO**
- **Ilyes BELKHIR**

Il s'agit d'une plateforme web de gestion de configurations réseau automatisées via DHCP et templates.

## À qui s’adresse le projet ?

Ce projet s’adresse :

- Aux **étudiants** et **enseignants** souhaitant explorer le déploiement ZTP
- Aux **administrateurs réseau** ou **DevOps** désirant tester des scénarios ZTP
- Aux **développeurs** voulant s’inspirer d’une architecture Django + Docker

## Utilisation rapide

```bash
# Cloner le projet
git clone <repo-url>
cd web-ztp

# Configurer l'environnement
cp .env.example .env
# Modifier les variables dans .env selon votre configuration

# Lancer les services
docker-compose up --build

# Créer les migrations
docker-compose exec web python manage.py migrate

# Créer un superutilisateur
docker-compose exec web python manage.py createsuperuser
```
