from django.db import models
from utils.jinja_utils import extract_jinja_variables


class Template(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="conf/", null=True)
    variables = models.JSONField(
        default=list,
        blank=True,
        help_text="Variables extraites automatiquement du template Jinja2",
    )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        """Override save pour extraire automatiquement les variables du template"""
        super().save(*args, **kwargs)

        if self.file:
            try:
                self.file.seek(0)  # Retourne au début du fichier
                template_content = self.file.read().decode("utf-8")
                variables = list(extract_jinja_variables(template_content))

                if self.variables != variables:
                    self.variables = variables
                    super().save(update_fields=["variables"])
            except Exception as e:
                print(f"Erreur lors de l'extraction des variables : {e}")
                self.variables = []


class Device(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    ip = models.GenericIPAddressField(unique=True, null=True, blank=True)
    hostname = models.CharField(max_length=255, unique=True)
    configured = models.BooleanField(default=False)
    template = models.ForeignKey(
        Template,
        on_delete=models.SET_NULL,
        null=True,
        related_name="devices",
    )

    # Stockage des valeurs des variables du template en JSON
    template_variables = models.JSONField(
        default=dict, blank=True, help_text="Valeurs des variables du template associé"
    )

    # Anciens champs ZTP - peuvent être supprimés plus tard
    subnet_mask = models.CharField(max_length=255, null=True, blank=True)
    default_gateway = models.GenericIPAddressField(null=True, blank=True)
    login = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.hostname} ({self.serial_number})"


class DHCPConfig(models.Model):
    """This model is used to store the DHCP server configuration.
    Only one instance of this model should exist in the database (Singleton).

    The save method ensures that only one instance can be created
    and overwritten the previous one.
    """

    subnet = models.GenericIPAddressField()
    min_ip_pool = models.GenericIPAddressField()
    max_ip_pool = models.GenericIPAddressField()

    def save(self, *args, **kwargs):
        if self.__class__.objects.exists() and not self.pk:
            existing = self.__class__.objects.first()
            self.pk = existing.pk
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        return cls.objects.first()
