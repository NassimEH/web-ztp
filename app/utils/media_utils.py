from django.conf import settings

def get_site_url():
    domain = settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS else "127.0.0.1:8000"
    protocol = "https" if not settings.DEBUG else "http"
    
    return f"{protocol}://{domain}"
