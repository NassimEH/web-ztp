# Web-ZTP

<p align="center">
    <img src="img/logo.png" align="center" width="30%" alt="Logo Web-ZTP">
</p>

## Bienvenue dans la documentation de Web-ZTP

Web-ZTP est une solution simple et efficace permettant la configuration automatique des équipements réseau Cisco (routeurs et switches) dès leur premier démarrage. Grâce à son interface web intuitive et son serveur DHCP intégré, Web-ZTP permet aux administrateurs réseau d'économiser du temps et d'éliminer les erreurs de configuration manuelle.

### À propos de Zero Touch Provisioning

Le Zero Touch Provisioning (ZTP) est une fonctionnalité qui permet aux équipements réseau d'être automatiquement configurés lors de leur première mise sous tension, sans nécessiter d'intervention manuelle sur chaque appareil.

### Fonctionnalités principales

- **Interface web intuitive** : Formulaires simples pour la configuration des équipements
- **Dashboard** : Vue d'ensemble des équipements en un coup d'œil
- **Serveur DHCP intégré** : Configuration automatique des adresses IP
- **Templates de configuration** : Création et gestion de modèles pour standardiser vos configurations
- **Sécurité HTTPS** : Communications sécurisées via le proxy Caddy

### Pour qui est conçu Web-ZTP ?

- Administrateurs réseau cherchant à automatiser la configuration d'équipements
- Techniciens déployant régulièrement de nouveaux équipements Cisco
- Entreprises souhaitant gagner du temps sur la mise en place de leur infrastructure réseau

### Commencer rapidement

Installation rapide avec Docker :

```bash
# Installation en une commande
docker compose up -d
```

Accès à l'application :
- URL : `https://localhost` ou l'adresse IP du serveur
- Connectez-vous avec les identifiants fournis par votre administrateur

### Architecture

Web-ZTP est basé sur une architecture moderne en conteneurs Docker comprenant :

- Une application web Django pour l'interface utilisateur
- Un serveur DHCP dédié pour la gestion des adresses IP
- Un proxy Caddy pour sécuriser les communications
- Une base de données PostgreSQL pour le stockage des configurations

### Parcourez la documentation

- **[Fonctionnalités](features.md)** : Découvrez les capacités de Web-ZTP
- **[Installation](installation.md)** : Comment installer et déployer l'application
- **[Configuration](configuration.md)** : Configurer Web-ZTP selon vos besoins
- **[Structure du projet](structure.md)** : Comprendre l'architecture technique