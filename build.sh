#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r app/requirements.txt

# Change to app directory
cd app

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
