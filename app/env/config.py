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

HOSTNAME = os.getenv("HOSTNAME")
