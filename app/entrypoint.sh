#!/bin/bash

function database_ready() {
    python3 database_check.py
}

until database_ready; do
  echo "The database is not available - waiting..."
  sleep 1
done
echo "The database is ready!"

echo "Running migrations..."
python3 manage.py migrate

# echo "Loading fixtures..."
# python3 manage.py loaddata dhcp_config.json

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Creating superuser..."
python3 manage.py createsuperuser --noinput 

echo "Starting Django server..."
gunicorn --bind 0.0.0.0:8000 webZtp.wsgi:application
