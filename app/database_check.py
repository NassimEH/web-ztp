"""Check if the database is ready and if environment variables are working."""

import sys
import psycopg2

import env.config as cfg

try:
    psycopg2.connect(
        dbname=cfg.DB_NAME, user=cfg.DB_USER, password=cfg.DB_PASSWORD, host=cfg.DB_HOST
    )
except psycopg2.OperationalError:
    sys.exit(-1)

sys.exit(0)
