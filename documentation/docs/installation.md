# Installation

## Prérequis

- Docker et Docker Compose installés
- Python 3.8 ou supérieur
- PostgreSQL 12 ou supérieur
- Git

## Installation avec Docker (Recommandé)

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-username/WEB-ZTP.git
cd WEB-ZTP
```

2. Configurez les variables d'environnement :
```bash
cp .env.example .env
# Modifiez les valeurs dans .env selon votre configuration
```

3. Lancez les conteneurs :
```bash
docker-compose up -d
```

4. Accédez à l'interface web :
```
http://localhost:8000
```

## Installation manuelle

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-username/WEB-ZTP.git
cd WEB-ZTP
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Configurez la base de données :
```bash
python manage.py migrate
```

5. Créez un superutilisateur :
```bash
python manage.py createsuperuser
```

6. Lancez le serveur :
```bash
python manage.py runserver
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