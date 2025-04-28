Introduction
============

WebZTP est une application web moderne pour la gestion de la configuration Zero Touch Provisioning (ZTP) des équipements réseau.

Fonctionnalités principales
--------------------------

* Gestion des appareils réseau
* Configuration automatique via ZTP
* Interface utilisateur intuitive
* Support multi-utilisateurs
* Mode sombre/clair
* Documentation complète

Architecture
-----------

L'application est construite avec :

* Django comme framework backend
* Bootstrap 5 pour l'interface utilisateur
* PostgreSQL comme base de données
* Sphinx pour la documentation

Qu'est-ce que le ZTP ?
---------------------

Le Zero Touch Provisioning (ZTP) est un processus qui permet aux équipements réseau de se configurer automatiquement lorsqu'ils sont connectés au réseau pour la première fois. Cela élimine le besoin d'une configuration manuelle initiale, réduisant ainsi les erreurs et le temps de déploiement.

.. panels::
   :container: container-lg
   :column: col-lg-4
   :card: +shadow

   .. panel:: Gestion des appareils
      :link: usage/devices
      :link-type: doc

      Configuration et suivi des équipements réseau avec une interface intuitive.

   .. panel:: Templates
      :link: usage/templates
      :link-type: doc

      Création et gestion de templates de configuration pour différents types d'appareils.

   .. panel:: Profils
      :link: usage/profiles
      :link-type: doc

      Gestion des profils utilisateurs et des permissions.

   .. panel:: API REST
      :link: api/index
      :link-type: doc

      Interface API complète pour l'intégration avec d'autres systèmes.

   .. panel:: Monitoring
      :link: usage/monitoring
      :link-type: doc

      Suivi en temps réel des déploiements et des états des appareils.

   .. panel:: Sécurité
      :link: configuration/security
      :link-type: doc

      Fonctionnalités de sécurité avancées pour protéger votre infrastructure.

Architecture
-----------

.. mermaid::
   :align: center

   graph TD
      A[Client] --> B[ZTP Manager]
      B --> C[DHCP Server]
      B --> D[TFTP Server]
      B --> E[Database]
      B --> F[API Gateway]
      F --> G[Microservices]

Commencer
---------

Pour commencer à utiliser ZTP Manager, suivez notre guide d'installation :doc:`installation`.

Besoin d'aide ?
--------------

Si vous avez des questions ou rencontrez des problèmes, consultez notre :doc:`faq` ou contactez notre équipe de support. 