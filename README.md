<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">WEB-ZTP</h1></p>
<p align="center">
    <em><code>❯ Fait par : Chadi, Nassim, Ilyes, Lucas</code></em>
</p>
<p align="center">
    <img src="https://img.shields.io/github/last-commit/Chadi-Mangle/web-ztp?style=default&logo=git&logoColor=white&color=0080ff" alt="Dernier commit">
    <img src="https://img.shields.io/github/languages/top/Chadi-Mangle/web-ztp?style=default&color=0080ff" alt="Langage principal">
    <img src="https://img.shields.io/github/languages/count/Chadi-Mangle/web-ztp?style=default&color=0080ff" alt="Nombre de langages">
</p>
<p align="center">
</p>
<p align="center">
</p>
<br>

##  Sommaire

- [ Présentation ](#-overview)
- [ Fonctionnalités ](#-features)
- [ Structure du projet ](#-project-structure)
  - [ Project Index](#-project-index)
- [ Commencer](#-getting-started)
  - [ Prérequis ](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Auteurs ](#-contributing)
- [ Informations ](#-acknowledgments)

---

##  Overview

<code>❯ Notre projet propose une interface web complète intégrant un serveur DHCP que nous avons développé nous-mêmes, ainsi qu’une implémentation personnalisée de la fonctionnalité Zero Touch Provisioning (ZTP). Cette plateforme permet aux utilisateurs d’ajouter et de configurer des appareils de manière automatisée, en renseignant les paramètres requis via des formulaires dédiés. L’ensemble a été conçu pour offrir une expérience utilisateur optimale, avec une interface intuitive, épurée et ergonomique, garantissant une gestion efficace des équipements et une mise en réseau simplifiée.</code>

---

##  Fonctionnalités

<code>❯ Notre site web propose une navigation structurée à travers plusieurs menus, offrant une expérience fluide et intuitive. Parmi ces menus, on retrouve un **dashboard** central qui fournit une vue d’ensemble sur l’ensemble des configurations en place, permettant ainsi un suivi efficace et une gestion optimisée des équipements. Une **page "Configurer un appareil"** est également disponible, offrant aux utilisateurs la possibilité d’ajouter de nouveaux dispositifs en sélectionnant les configurations adaptées via une interface dédiée. Enfin, une **page d’aide** regroupe diverses informations et ressources essentielles pour accompagner les utilisateurs dans l’utilisation de la plateforme et la compréhension des fonctionnalités implémentées.</code>

---

##  Structure du projet

```sh
└── web-ztp/
    ├── .github
    │   └── workflows
    ├── Dockerfile
    ├── app
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── generator
    │   ├── management
    │   ├── migrations
    │   ├── models.py
    │   ├── static
    │   ├── templates
    │   ├── templatetags
    │   ├── tests.py
    │   ├── url.py
    │   ├── utils
    │   └── views
    ├── dhcp_server
    │   ├── __init.py__
    │   ├── dhcp_db.py
    │   ├── dhcp_server.py
    │   ├── django_setup.py
    │   └── requirements.txt
    ├── docker-compose-exemple.yml
    ├── docker-compose.yml
    ├── entrypoint.py
    ├── manage.py
    ├── requirements.txt
    └── webZtp
        ├── __init__.py
        ├── asgi.py
        ├── log_views.html
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```


<details open>
    <summary><b><code>WEB-ZTP/</code></b></summary>
    <details> <!-- __root__ Submodule -->
        <summary><b>__root__</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/entrypoint.py'>entrypoint.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/manage.py'>manage.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/docker-compose-exemple.yml'>docker-compose-exemple.yml</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/requirements.txt'>requirements.txt</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/docker-compose.yml'>docker-compose.yml</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/Dockerfile'>Dockerfile</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            </table>
        </blockquote>
    </details>
    <details> <!-- .github Submodule -->
        <summary><b>.github</b></summary>
        <blockquote>
            <details>
                <summary><b>workflows</b></summary>
                <blockquote>
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/.github/workflows/semgrep.yml'>semgrep.yml</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    </table>
                </blockquote>
            </details>
        </blockquote>
    </details>
    <details> <!-- webZtp Submodule -->
        <summary><b>webZtp</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/webZtp/settings.py'>settings.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/webZtp/urls.py'>urls.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/webZtp/log_views.html'>log_views.html</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/webZtp/asgi.py'>asgi.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/webZtp/wsgi.py'>wsgi.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            </table>
        </blockquote>
    </details>
    <details> <!-- app Submodule -->
        <summary><b>app</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/tests.py'>tests.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/forms.py'>forms.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/apps.py'>apps.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/admin.py'>admin.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/url.py'>url.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/models.py'>models.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            </table>
            <details>
                <summary><b>templates</b></summary>
                <blockquote>
                    <details>
                        <summary><b>app</b></summary>
                        <blockquote>
                            <table>
                            <tr>
                                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/templateForm.html'>templateForm.html</a></b></td>
                                <td><code>❯ REPLACE-ME</code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/deviceForm.html'>deviceForm.html</a></b></td>
                                <td><code>❯ REPLACE-ME</code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/help.html'>help.html</a></b></td>
                                <td><code>❯ REPLACE-ME</code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/dhcpconfigForm.html'>dhcpconfigForm.html</a></b></td>
                                <td><code>❯ REPLACE-ME</code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/base.html'>base.html</a></b></td>
                                <td><code>❯ REPLACE-ME</code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/devices.html'>devices.html</a></b></td>
                                <td><code>❯ REPLACE-ME</code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/dashboard.html'>dashboard.html</a></b></td>
                                <td><code>❯ REPLACE-ME</code></td>
                            </tr>
                            </table>
                            <details>
                                <summary><b>components</b></summary>
                                <blockquote>
                                    <table>
                                    <tr>
                                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/components/footer.html'>footer.html</a></b></td>
                                        <td><code>❯ REPLACE-ME</code></td>
                                    </tr>
                                    <tr>
                                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/components/deviceDashboard.html'>deviceDashboard.html</a></b></td>
                                        <td><code>❯ REPLACE-ME</code></td>
                                    </tr>
                                    <tr>
                                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/components/card.html'>card.html</a></b></td>
                                        <td><code>❯ REPLACE-ME</code></td>
                                    </tr>
                                    <tr>
                                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/components/deviceRows.html'>deviceRows.html</a></b></td>
                                        <td><code>❯ REPLACE-ME</code></td>
                                    </tr>
                                    <tr>
                                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/components/formResponse.html'>formResponse.html</a></b></td>
                                        <td><code>❯ REPLACE-ME</code></td>
                                    </tr>
                                    <tr>
                                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/components/menu.html'>menu.html</a></b></td>
                                        <td><code>❯ REPLACE-ME</code></td>
                                    </tr>
                                    <tr>
                                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/components/formButton.html'>formButton.html</a></b></td>
                                        <td><code>❯ REPLACE-ME</code></td>
                                    </tr>
                                    <tr>
                                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templates/app/components/genericForm.html'>genericForm.html</a></b></td>
                                        <td><code>❯ REPLACE-ME</code></td>
                                    </tr>
                                    </table>
                                </blockquote>
                            </details>
                        </blockquote>
                    </details>
                </blockquote>
            </details>
            <details>
                <summary><b>generator</b></summary>
                <blockquote>
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/generator/views.py'>views.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/generator/urls.py'>urls.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    </table>
                </blockquote>
            </details>
            <details>
                <summary><b>templatetags</b></summary>
                <blockquote>
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/templatetags/custom_tags.py'>custom_tags.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    </table>
                </blockquote>
            </details>
            <details>
                <summary><b>management</b></summary>
                <blockquote>
                    <details>
                        <summary><b>commands</b></summary>
                        <blockquote>
                            <table>
                            <tr>
                                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/management/commands/rundhcp.py'>rundhcp.py</a></b></td>
                                <td><code>❯ REPLACE-ME</code></td>
                            </tr>
                            </table>
                        </blockquote>
                    </details>
                </blockquote>
            </details>
            <details>
                <summary><b>migrations</b></summary>
                <blockquote>
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/migrations/0003_template_name_alter_device_serial_number.py'>0003_template_name_alter_device_serial_number.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/migrations/0001_initial.py'>0001_initial.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/migrations/0002_alter_device_unique_together_device_configured_and_more.py'>0002_alter_device_unique_together_device_configured_and_more.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/migrations/0004_remove_template_file_path_template_file.py'>0004_remove_template_file_path_template_file.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    </table>
                </blockquote>
            </details>
            <details>
                <summary><b>views</b></summary>
                <blockquote>
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/views/help_views.py'>help_views.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/views/index_views.py'>index_views.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/views/config_view.py'>config_view.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/views/log_views.py'>log_views.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/views/device_views.py'>device_views.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/views/dashboard_views.py'>dashboard_views.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/views/form_views.py'>form_views.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    </table>
                </blockquote>
            </details>
            <details>
                <summary><b>utils</b></summary>
                <blockquote>
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/utils/device_utils.py'>device_utils.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/utils/dhcp_utils.py'>dhcp_utils.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/app/utils/media_utils.py'>media_utils.py</a></b></td>
                        <td><code>❯ REPLACE-ME</code></td>
                    </tr>
                    </table>
                </blockquote>
            </details>
        </blockquote>
    </details>
    <details> <!-- dhcp_server Submodule -->
        <summary><b>dhcp_server</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/dhcp_server/dhcp_db.py'>dhcp_db.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/dhcp_server/__init.py__'>__init.py__</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/dhcp_server/dhcp_server.py'>dhcp_server.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/dhcp_server/requirements.txt'>requirements.txt</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/Chadi-Mangle/web-ztp/blob/master/dhcp_server/django_setup.py'>django_setup.py</a></b></td>
                <td><code>❯ REPLACE-ME</code></td>
            </tr>
            </table>
        </blockquote>
    </details>
</details>

---
##  Commencer

###  Pré-requis

Vous aurez besoin de ces technologies :

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


###  Installation

Installer le projet :

**Build from source:**

1. Clonez le dépôt :
```sh
❯ git clone https://github.com/Chadi-Mangle/web-ztp
```

2. Allez dans le bon dossier :
```sh
❯ cd web-ztp
```

3. Installez les dépendances

**En utilisant `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt, dhcp_server/requirements.txt
```


**En utilisant `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t Chadi-Mangle/web-ztp .
```




###  Utilisation
Lancez l'application:
**En utilisant `python`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python manage.py runserver
```


**En utilisant `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```

## Auteurs

- Nassim El Haddad
- Chadi Manglé
- Ilyes Belkhir
- Lucas Dréano

---

##  Information

- Ce projet est réalisé dans le cadre de notre cursus ingénieur à Télécom SudParis

---
