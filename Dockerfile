# Dockerfile
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

# Collect static files si nécessaire
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "ztp_project.wsgi:application", "--bind", "0.0.0.0:8000"]
