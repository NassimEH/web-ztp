FROM python:3.9-slim

WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Exposition du port pour le serveur web Django
EXPOSE 8000

# Commande de démarrage
CMD ["/bin/sh", "entrypoint.sh"]