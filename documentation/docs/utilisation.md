<!-- filepath: /home/udach/web-ztp/documentation/docs/utilisation.md -->
# Utilisation

## Premiers pas

### Connexion à l'interface

1. Accédez à l'interface web :
```
https://localhost
```
ou utilisez l'adresse IP du serveur où Web-ZTP est installé.

2. Connectez-vous avec vos identifiants :
- Utilisateur : admin
- Mot de passe : (celui fourni par votre administrateur)

### Dashboard

Le dashboard est la page d'accueil de Web-ZTP. Il vous donne un aperçu rapide de :

- Le nombre total d'appareils configurés
- L'état des appareils (configurés, en attente, erreur)
- Les activités récentes du système

## Configuration ZTP

### Création de templates

1. Accédez à **Configuration** dans le menu principal
2. Cliquez sur **Ajouter un template**
3. Donnez un nom à votre template
4. Téléchargez ou créez votre fichier de configuration
5. Enregistrez le template

Les templates peuvent contenir des variables qui seront remplacées par les valeurs spécifiques à chaque appareil lors du provisionnement. Par exemple :

```
hostname {{hostname}}
ip address {{ip}} {{subnet_mask}}
ip default-gateway {{default_gateway}}
username {{username}} privilege 15 secret {{password}}
```

### Configuration du serveur DHCP

1. Accédez à **Configuration** dans le menu principal
2. Configurez la plage d'adresses IP pour le serveur DHCP
3. Enregistrez la configuration

## Gestion des appareils

### Ajout d'un appareil

1. Accédez à **Appareils** dans le menu principal
2. Cliquez sur **Ajouter un appareil**
3. Saisissez les informations requises :
   - Numéro de série de l'appareil
   - Adresse IP
   - Nom d'hôte
   - Sélectionnez un template (optionnel)
4. Pour les paramètres avancés, configurez :
   - Masque de sous-réseau
   - Passerelle par défaut
   - Nom d'utilisateur
   - Mot de passe
5. Cliquez sur **Enregistrer**

### Provisionnement d'un appareil

Une fois l'appareil ajouté dans le système, le processus de provisionnement est entièrement automatique :

1. Connectez l'appareil au réseau
2. L'appareil démarre et demande une adresse IP via DHCP
3. Le serveur DHCP fournit une adresse IP et les options ZTP
4. L'appareil télécharge et applique automatiquement sa configuration
5. Le statut de l'appareil est mis à jour dans l'interface Web-ZTP

### Suivi des appareils

Le dashboard de Web-ZTP vous permet de suivre en temps réel l'état de vos appareils :

- **Configuré** : L'appareil a été configuré avec succès
- **En attente** : L'appareil est enregistré mais n'a pas encore été configuré
- **Erreur** : Un problème est survenu lors de la configuration

## Sécurité

Pour garantir la sécurité de votre installation Web-ZTP, suivez ces bonnes pratiques :

1. Changez régulièrement le mot de passe administrateur
2. Limitez l'accès au serveur Web-ZTP aux adresses IP autorisées
3. Vérifiez régulièrement les journaux d'activité
