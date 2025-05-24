Mode Sombre
==========

Le mode sombre est une fonctionnalité qui permet de basculer entre un thème clair et un thème sombre pour une meilleure expérience utilisateur, particulièrement dans des environnements peu éclairés.

Activation
---------

Le mode sombre peut être activé de deux façons :

1. En cliquant sur l'icône de lune dans le coin supérieur droit de l'interface
2. En utilisant le raccourci clavier ``Ctrl + D`` (à venir)

La préférence de thème est sauvegardée dans le localStorage du navigateur et persiste entre les sessions.

Fonctionnalités
-------------

* Basculement instantané entre les thèmes clair et sombre
* Persistance de la préférence entre les sessions
* Adaptation automatique de tous les éléments de l'interface
* Transitions fluides entre les thèmes
* Optimisation des contrastes pour une meilleure lisibilité
* Support des préférences système (à venir)

Éléments adaptés
--------------

Le mode sombre affecte tous les éléments de l'interface :

* Navigation latérale
  * Fond et bordures
  * Textes et icônes
  * Effets de survol
  * Indicateurs d'état

* Cartes et tableaux
  * Arrière-plans
  * Bordures
  * Ombres
  * Textes et en-têtes

* Formulaires et boutons
  * Champs de saisie
  * Boutons d'action
  * Labels et placeholders
  * Messages d'erreur

* Textes et icônes
  * Couleurs principales
  * Couleurs secondaires
  * Opacités
  * Tailles et poids

* Bordures et ombres
  * Couleurs des bordures
  * Intensité des ombres
  * Rayons de bordure
  * Effets de profondeur

Personnalisation
--------------

Les couleurs du thème sombre sont définies à l'aide de variables CSS, ce qui permet une personnalisation facile :

.. code-block:: css

   body.dark-theme {
       /* Couleurs principales */
       --bg-color: #121212;
       --text-color: #E0E0E0;
       --card-bg: #1E1E1E;
       --border-color: #2D2D2D;
       
       /* Navigation */
       --nav-bg: #1A1A1A;
       --nav-text: #E0E0E0;
       --nav-hover: #4A90E2;
       
       /* Formulaires */
       --input-bg: #2D2D2D;
       --input-border: #3A3A3A;
       --input-placeholder: #A0A0A0;
       
       /* Tableaux */
       --table-header: #2D2D2D;
       --table-row: #1E1E1E;
       --table-hover: #2D2D2D;
       
       /* Transitions */
       --transition-speed: 0.3s;
   }

Pour personnaliser le thème sombre, modifiez simplement les valeurs des variables CSS correspondantes.

Accessibilité
------------

Le mode sombre a été conçu en respectant les normes d'accessibilité :

* Contraste suffisant pour la lisibilité
  * Ratio de contraste minimum de 4.5:1 pour le texte normal
  * Ratio de contraste minimum de 3:1 pour les grands textes
  * Ratio de contraste minimum de 3:1 pour les éléments d'interface

* Adaptation des couleurs pour les daltoniens
  * Utilisation de contrastes suffisants
  * Indicateurs visuels supplémentaires
  * Textes explicatifs

* Support des lecteurs d'écran
  * Attributs ARIA appropriés
  * Textes alternatifs
  * Structure sémantique

* Transitions douces
  * Durée de transition de 300ms
  * Fonction d'accélération appropriée
  * Prévention des flashs lumineux

Bonnes pratiques
--------------

Pour une expérience optimale avec le mode sombre :

1. Évitez les contrastes trop élevés qui peuvent causer de la fatigue visuelle
2. Utilisez des couleurs sombres mais pas complètement noires
3. Maintenez une hiérarchie visuelle claire
4. Testez régulièrement l'accessibilité
5. Vérifiez la lisibilité sur différents écrans

Dépannage
--------

Problèmes courants et solutions :

* Le thème ne persiste pas entre les sessions
  * Vérifiez que le localStorage est activé
  * Effacez le cache du navigateur

* Transitions saccadées
  * Désactivez les animations système
  * Vérifiez les performances du navigateur

* Éléments mal contrastés
  * Signalez le problème
  * Utilisez temporairement le mode clair 