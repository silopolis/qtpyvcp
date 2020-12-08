===========
Paramètres du fichier INI
===========

Pour obtenir une liste des options courantes du fichier INI exécutez:

.. code-block:: bash

    qtpyvcp -h

Les options de la ligne de commande sont en minuscule et utilisent le tiret, les options du fichier INI sont en majuscule
et utilisent le tiret bas. Exemple: ``--hide-menu-bar`` >> ``HIDE_MENU_BAR``.

Les options disponibles dans le fichier INI sont:

.. code-block:: vim

    [DISPLAY]
    # Nom du VCP à utiliser, ou fichier .ui ou .yml
    VCP = nom

    # Le thème Qt à utiliser: fusion, windows, etc
    THEME = theme

    # Chemin du fichier de feuille de style QSS
    STYLESHEET = style.qss

    # Taille initiale de la fenêtre en pixels
    SIZE = <L>x<H>

    # Position initiale de la fenêtre en pixels
    POSITION = <X>x<Y>

    # Indicateur pour démarrer en mode plein écran
    FULLSCREEN = bool

    # Indicateur pour démarrer avec la fenêtre maximisée
    MAXIMIZE = bool

    # Masque la barre de menus, si présente
    HIDE_MENU_BAR = bool

    # Masque la barre d'état, si présente
    HIDE_STATUS_BAR = bool

    # Masque le curseur pour les VCPs pour écrans tactiles
    HIDE_CURSOR = True

    # S'il faut afficher une boîte de dialogue pour confirmer la sortie
    CONFIRM_EXIT = bool

    # Un de DEBUG, INFO, WARN, ERROR ou CRITICAL
    LOG_LEVEL = level

    # Spécifie le fichier journal
    LOG_FILE = file

    # Spécifie un fichier de configuration YML spécifique à la machine
    CONFIG_FILE = fichier

    # Spécifie le fichier de préférences
    PREF_FILE = fichier

    # Surveiller et enregistrer les performances du système
    PERFMON = bool

    # Liaison Qt Python à utiliser, pyqt5 ou pyside2
    QT_API = api

    # Arguments supplémentaires passés à l'application QtApplication.
    COMMAND_LINE_ARGS = <args>

    # Options du parcours d'outil VTK_BackPlot
    [VTK]
    # Affichage de l'enveloppe de la machine
    MACHINE_BOUNDRY = bol

    # Affichage des limites de la machine
    MACHINE_TICKS = bool

    # Affichage des étiquettes de la machine
    MACHINE_LABELS = bool

    # Affichage de l'enveloppe du programme
    PROGRAM_BOUNDRY = bool

    # Affichage des limites du programme
    PROGRAM_TICKS = bool

    # Affichage des libellés du programme
    PROGRAM_LABELS = bool

Les valeurs booléennes peuvent être ``true``, ``on``, ``yes`` ou ``1`` pour **Vrai**,
et ``false``, ``off``, ``no`` ou ``0`` pour **Faux**.

Les chemins des fichiers peuvent être relatifs au dossier de configuration, au répertoire utilisateur, ou
absolus. Les variables d'environnement sont développées.

.. code-block:: vim

    Chemins de fichiers:
    # Les chemins de fichiers peuvent être relatifs au répertoire de configuration :
    #LOG_FILE = qtpyvcp.log

    # Ou relatif à $HOME: (Peut ne pas être compatible avec d'autres GUI!)
    #LOG_FILE = ~/qtpyvcp.log

    # Ou à un emplacement absolu :
    #LOG_FILE = /home/<USER>/qtpyvcp.log

    # Les variables d'environnement sont également étendues:
    #LOG_FILE = $CONFIG_DIR/qtpyvcp.log
