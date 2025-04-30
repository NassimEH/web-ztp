# Configuration

## Configuration de base

### Fichier .env

Le fichier `.env` contient les variables d'environnement essentielles :

```env
# Django
DJANGO_SECRET_KEY=votre_clé_secrète
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de données
DATABASE_URL=postgres://user:password@localhost:5432/web_ztp

# DHCP
DHCP_SERVER=192.168.1.1
DHCP_PORT=67
```

### Configuration Django

Les paramètres Django principaux sont dans `web_ztp/settings.py` :

```python
# Configuration de la base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web_ztp',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## Configuration du serveur DHCP

### Fichier dhcpd.conf

Le fichier de configuration DHCP se trouve dans `dhcp/dhcpd.conf` :

```conf
# Configuration globale
option domain-name "example.com";
option domain-name-servers 8.8.8.8, 8.8.4.4;

default-lease-time 600;
max-lease-time 7200;

# Sous-réseau
subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.100 192.168.1.200;
    option routers 192.168.1.1;
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.1.255;
}
```

### Options DHCP personnalisées

Pour ajouter des options DHCP personnalisées :

```conf
# Option personnalisée pour le serveur TFTP
option tftp-server-name code 150 = string;
option tftp-server-name "192.168.1.2";

# Option pour le fichier de configuration
option config-file code 67 = string;
option config-file "config.txt";
```

## Configuration des équipements

### Templates de configuration

Les templates sont stockés dans `templates/` :

```jinja
# Template pour switch Cisco
hostname {{ hostname }}
!
interface {{ interface }}
 description {{ description }}
 switchport mode access
 switchport access vlan {{ vlan }}
!
```

### Variables d'environnement

Les variables d'environnement pour les équipements sont définies dans `equipment/models.py` :

```python
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=17)
    configuration = models.TextField()
```

## Sécurité

### Configuration SSL/TLS

Pour activer HTTPS, modifiez `web_ztp/settings.py` :

```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### Authentification

Configuration de l'authentification dans `web_ztp/settings.py` :

```python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'
```

## Monitoring

### Configuration des logs

Les logs sont configurés dans `web_ztp/settings.py` :

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

### Configuration des alertes

Les alertes sont configurées dans `monitoring/settings.py` :

```python
ALERT_SETTINGS = {
    'email': {
        'enabled': True,
        'recipients': ['admin@example.com'],
    },
    'slack': {
        'enabled': False,
        'webhook_url': 'your-webhook-url',
    },
}
```