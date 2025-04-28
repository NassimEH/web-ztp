# Utilisation

## Premiers pas

### Connexion à l'interface

1. Accédez à l'interface web :
```
http://localhost:8000
```

2. Connectez-vous avec vos identifiants :
- Utilisateur : admin
- Mot de passe : (celui défini lors de l'installation)

### Configuration initiale

1. Configurez le serveur DHCP :
   - Accédez à "Configuration" > "Serveur DHCP"
   - Définissez les plages d'adresses IP
   - Configurez les options DHCP

2. Définissez les templates de configuration :
   - Accédez à "Configuration" > "Templates"
   - Créez des templates pour vos équipements

## Gestion des équipements

### Ajout d'un équipement

1. Accédez à "Équipements" > "Ajouter"
2. Remplissez les informations :
   - Nom de l'équipement
   - Modèle
   - Adresse MAC
   - Template de configuration

3. Cliquez sur "Enregistrer"

### Configuration automatique (ZTP)

1. Branchez le nouvel équipement au réseau
2. L'équipement recevra automatiquement :
   - Une adresse IP via DHCP
   - Sa configuration via TFTP
   - Les paramètres réseau nécessaires

3. Vérifiez le statut dans "Équipements" > "Statut"

## Gestion du réseau

### Surveillance

1. Tableau de bord :
   - Vue d'ensemble des équipements
   - Statut des configurations
   - Alertes en temps réel

2. Logs :
   - Accédez à "Monitoring" > "Logs"
   - Filtrez par type d'événement
   - Exportez les logs si nécessaire

### Maintenance

1. Mise à jour des configurations :
   - Modifiez les templates
   - Appliquez aux équipements concernés
   - Vérifiez les changements

2. Sauvegarde :
   - Exportez les configurations
   - Sauvegardez la base de données
   - Archivez les logs

## Fonctionnalités avancées

### API REST

1. Authentification :
```bash
curl -X POST http://localhost:8000/api/token/
  -H "Content-Type: application/json"
  -d '{"username":"admin","password":"votre_mot_de_passe"}'
```

2. Exemple d'utilisation :
```bash
# Récupérer la liste des équipements
curl -H "Authorization: Bearer votre_token" http://localhost:8000/api/equipment/

# Ajouter un équipement
curl -X POST http://localhost:8000/api/equipment/
  -H "Authorization: Bearer votre_token"
  -H "Content-Type: application/json"
  -d '{"name":"switch1","model":"Cisco","mac_address":"00:11:22:33:44:55"}'
```

### Automatisation

1. Scripts Python :
```python
from web_ztp.client import WebZTPClient

client = WebZTPClient(api_url="http://localhost:8000/api/")
client.authenticate("admin", "mot_de_passe")

# Ajouter un équipement
equipment = {
    "name": "switch1",
    "model": "Cisco",
    "mac_address": "00:11:22:33:44:55"
}
client.add_equipment(equipment)
```

2. Intégration avec d'autres outils :
   - Ansible
   - Puppet
   - Chef

## Dépannage

### Problèmes courants

1. Équipement non détecté :
   - Vérifiez la connexion réseau
   - Confirmez l'adresse MAC
   - Vérifiez les logs DHCP

2. Configuration non appliquée :
   - Vérifiez le template
   - Confirmez les permissions TFTP
   - Consultez les logs système

### Support

1. Documentation :
   - Guide d'utilisation
   - FAQ
   - Exemples de configuration

2. Assistance :
   - Forum communautaire
   - Tickets de support
   - Documentation en ligne