FROM python:3.9-slim

WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Exposition du port pour le serveur web Django
EXPOSE 8000

# Commande de démarrage
CMD ["/bin/sh", "entrypoint.sh"]