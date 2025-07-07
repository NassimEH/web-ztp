# Installation et configuration

## 1. Prérequis

- Docker
- Docker Compose
- Python 3.9+ (optionnel pour développement local)

## 2. Fichier `.env`

Extrait d’un exemple `.env` :
```bash
  DJANGO_SECRET_KEY=your-secret-key
  DEBUG=True
  ALLOWED_HOSTS=localhost,127.0.0.1
  POSTGRES_DB=ztp
  POSTGRES_USER=ztp_user
  POSTGRES_PASSWORD=ztp_pass
```

## 3. Lancer avec Docker

```bash
  docker-compose up --build
```

## 4. Acceder au site
Interface utilisateur : http://localhost:8080
Interface admin : http://localhost:8080/admin
