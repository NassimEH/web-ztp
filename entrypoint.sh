#!/bin/sh

# Fonction pour attendre que PostgreSQL soit prêt
postgres_ready() {
    python << END
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="webztp_db",
        user="webztp_user",
        password="webztp_password",
        host="db"
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

# Attente que PostgreSQL soit prêt
until postgres_ready; do
  >&2 echo "PostgreSQL n'est pas disponible - attente..."
  sleep 1
done
>&2 echo "PostgreSQL est prêt !"

echo "Exécution des migrations..."
python manage.py migrate

echo "Chargement des modèles..."
python manage.py loaddata dhcp_config.json

echo "Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

echo "Démarrage du serveur Django..."
gunicorn --bind 0.0.0.0:8000 webZtp.wsgi:application
