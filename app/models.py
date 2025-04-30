from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# A voir si on garde parce qu'on a qu'un seul template
class Template(models.Model):
    """Modèle de données pour un template de configuration ZTP"""

    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="conf/", null=True)

    def __str__(self):
        return str(self.name)


class Device(models.Model):
    """Modèle de données pour une machine à configurer"""

    serial_number = models.CharField(max_length=255, unique=True)
    ip = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=255, null=True, blank=True)
    configured = models.BooleanField(default=False)
    template = models.ForeignKey(
        Template, on_delete=models.SET_NULL, null=True, related_name="devices"
    )

    # Variables pour les templates Jinja
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    subnet_mask = models.CharField(max_length=255, null=True, blank=True)
    default_gateway = models.GenericIPAddressField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.hostname} ({self.ip})"


class DHCPConfig(models.Model):
    """Modèle de données pour une configuration DHCP"""

    subnet = models.GenericIPAddressField()
    min_ip_pool = models.GenericIPAddressField()
    max_ip_pool = models.GenericIPAddressField()

    def save(self, *args, **kwargs):
        if not self.subnet:
            self.subnet = "255.255.255.0"
        if not self.min_ip_pool:
            self.min_ip_pool = "192.168.0.100"
        if not self.max_ip_pool:
            self.max_ip_pool = "192.168.0.200"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"DHCP: {self.subnet}"

class Action(models.Model):
    ACTION_CHOICES = [
        ('add', 'Add'),
        ('delete', 'Delete'),
        ('modify', 'Modify'),
    ]
    
    action_type = models.CharField(max_length=10, choices=ACTION_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.get_action_type_display()} on {self.created_at}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'Profil de {self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)
    instance.profile.save()
