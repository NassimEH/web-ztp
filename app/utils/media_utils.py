from django.conf import settings

def get_site_url():
    domain = settings.ALLOWED_HOSTS[0]
    protocol = "https" if not settings.DEBUG else "http"

    return f"{protocol}://{domain}"
