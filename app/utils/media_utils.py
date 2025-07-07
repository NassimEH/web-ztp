from django.conf import settings
import env.config as cfg


def get_internal_url():
    protocol = "http" if not settings.DEBUG else "http"

    return f"{protocol}://{cfg.PRIVATE_IP}:{cfg.HTTP_PORT}"
