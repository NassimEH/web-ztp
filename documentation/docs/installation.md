# Installation

## Prérequis

L'ins## Accès à l'application

Une fois l'installation terminée, vous pouvez accéder à l'interface web de Web-ZTP :

- **URL par défaut** : https://localhost (en local) ou l'adresse IP du serveur
- **Identifiants** : Les identifiants doivent être définis lors de l'installation initialeion de Web-ZTP est très simple grâce à Docker. Vous aurez besoin de :

- Docker et Docker Compose installés sur votre système
- Un accès réseau pour que les équipements puissent communiquer avec le serveur Web-ZTP
- Environ 500 Mo d'espace disque libre

## Installation avec Docker

L'installation complète du système Web-ZTP se fait en une seule commande :

```bash
docker compose up -d
```

Cette commande va démarrer les quatre conteneurs Docker qui composent l'application :

1. **Application Web Django** : L'interface utilisateur web
2. **Serveur DHCP** : Pour l'attribution automatique des adresses IP
3. **Caddy** : Serveur proxy inverse qui fournit le support HTTPS
4. **PostgreSQL** : Base de données pour stocker les configurations et les informations des appareils

## Vérification de l'installation

Après le démarrage des conteneurs, vous pouvez vérifier que tout fonctionne correctement :

```bash
docker compose ps
```

Tous les services devraient être à l'état "Up".

## Accès à l'application

Une fois l'installation terminée, vous pouvez accéder à l'interface web de Web-ZTP :

- **URL par défaut** : `https://localhost` (en local) ou l'adresse IP du serveur
- **Identifiants par défaut** : Admin / (demandez le mot de passe à votre administrateur)

## Mise à jour de l'application

Pour mettre à jour Web-ZTP vers la dernière version :

```bash
docker compose pull
docker compose up -d
```

## Configuration

### Variables d'environnement

Les variables d'environnement importantes à configurer :

- `DJANGO_SECRET_KEY` : Clé secrète pour Django
- `DATABASE_URL` : URL de connexion à la base de données
- `DEBUG` : Mode debug (désactiver en production)
- `ALLOWED_HOSTS` : Liste des hôtes autorisés

### Configuration du serveur DHCP

1. Modifiez le fichier `dhcp/dhcpd.conf` selon vos besoins
2. Redémarrez le service DHCP :
```bash
sudo systemctl restart dhcpd
```

## Mise à jour

Pour mettre à jour une installation existante :

1. Récupérez les dernières modifications :
```bash
git pull
```

2. Mettez à jour les dépendances :
```bash
pip install -r requirements.txt
```

3. Appliquez les migrations :
```bash
python manage.py migrate
```

4. Redémarrez les services :
```bash
docker-compose restart  # Si installation Docker
# ou
python manage.py runserver  # Si installation manuelle
```