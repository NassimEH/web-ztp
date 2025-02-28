#!/bin/sh

echo "Exécution des migrations..."
python manage.py migrate

echo "Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

echo "Démarrage du serveur Django..."
gunicorn --bind 0.0.0.0:8000 webZtp.wsgi:application
