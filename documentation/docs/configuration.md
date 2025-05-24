# Configuration

## Présentation générale

La configuration de Web-ZTP se fait entièrement via l'interface web. Aucune modification manuelle de fichiers n'est nécessaire après l'installation Docker. Toutes les fonctionnalités sont accessibles à travers des formulaires intuitifs dans l'interface utilisateur.

## Configuration initiale

Après la première connexion à l'interface web, suivez ces étapes pour configurer votre environnement Web-ZTP :

1. Créez un compte administrateur si ce n'est pas déjà fait
2. Configurez les paramètres du serveur DHCP dans la section Configuration
3. Créez des templates de configuration pour vos équipements

## Configuration du serveur DHCP

Le serveur DHCP intégré peut être configuré directement depuis l'interface web :

1. Naviguez vers la section **Configuration** du menu principal
2. Configurez les paramètres du sous-réseau (plage d'adresses, passerelle par défaut)
3. Enregistrez les modifications

Les paramètres DHCP seront automatiquement appliqués au serveur DHCP conteneurisé.

## Configuration des équipements

La configuration des équipements réseau se fait en deux étapes principales :

1. **Création de templates** : Définissez les modèles de configuration que vous souhaitez appliquer
2. **Ajout d'appareils** : Enregistrez vos appareils avec leurs paramètres spécifiques

### Ajout d'un nouvel équipement

Pour ajouter un nouvel équipement à provisionner :

1. Accédez à la section **Appareils** dans le menu principal
2. Cliquez sur **Ajouter un appareil**
3. Remplissez les informations requises :
   - Numéro de série
   - Adresse IP
   - Nom d'hôte
   - Template de configuration (optionnel)
4. Pour les paramètres avancés, configurez :
   - Masque de sous-réseau
   - Passerelle par défaut
   - Nom d'utilisateur
   - Mot de passe
5. Cliquez sur **Enregistrer**