"""Environment variables for all Django projects."""

import os
from django.core.management.utils import get_random_secret_key

# Django settings
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_secret_key())
IS_PRODUCTION = os.getenv("IS_PRODUCTION")

# Database configuration
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")

HOSTNAME = os.getenv("DJANGO_HOSTNAME", "localhost")

HTTPS_PORT = os.getenv("HTTPS_PORT", "443")
HTTP_PORT = os.getenv("HTTP_PORT", "80")
ALLOWED_HOSTS_LIST = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
