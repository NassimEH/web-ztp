'''Pour attentre que la bd se lance avant l'execution de Django'''
import os
import time
import psycopg2

DB_NAME = os.getenv("POSTGRES_DB", "webztp_db")
DB_USER = os.getenv("POSTGRES_USER", "webztp_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "webztp_password")
DB_HOST = "db"
DB_PORT = 5432

def wait_for_db():
    """Attend que la base de données PostgreSQL soit prête."""
    print("⏳ Attente de la base de données...")
    while True:
        try:
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
            conn.close()
            print("✅ Base de données prête !")
            break
        except psycopg2.OperationalError:
            print("⏳ Base non disponible, nouvelle tentative dans 2 secondes...")
            time.sleep(2)

if __name__ == "__main__":
    wait_for_db()

    print("🔄 Exécution des migrations...")
    os.system("python manage.py migrate")

    print("📦 Collecte des fichiers statiques...")
    os.system("python manage.py collectstatic --noinput")

    print("🚀 Démarrage du serveur Django...")
    os.system("gunicorn --bind 0.0.0.0:8000 webZtp.wsgi:application")
