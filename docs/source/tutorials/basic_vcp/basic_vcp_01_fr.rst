=================
Cloner et Préparer
=================

.. note::
    Le tutoriel suivant a été réalisé en utilisant Debian 9 (Stretch).

Avant de cloner, vous devriez avoir installé QtPyVCP comme indiqué sur la
page :doc:`/install/index_fr`.

Pour commencer, vous devez cloner le `VCP Modèle`. Il contient toute la structure
de base nécessaire pour construire un VCP. Dans un terminal ::

    git clone https://github.com/kcjengr/vcp-template.git


Pour faire une copie du `VCP Modèle` pour ce tutoriel, dans le terminal passez d'abord
dans le dossier ``vcp-template``puis exécutez ``tutorial.sh`` et utilisez un nouveau nom ne
contenant que des lettres, des nombres et des tirets bas "_". Pour ce tutoriel j'ai utilisé
"vcp1", donc tous les exemples utilisent ce nom. Choisissez oui pour copier les fichiers
de configuration de LinuxCNC.
::

    cd vcp-template
    ./tutorial.sh

Pour modifier le nouveau VCP créé à partir du modèle vcp-template, exécutez la commande suivante
dans un terminal. Dans cet exemple, le modèle vcp-template copié a été nommé `vcp1`.
::

    editvcp vcp1

Le `VCP Modèle` est maintenant ouvert dans `Qt Designer`.

.. image:: images/vcp1-designer-01_fr.png
   :align: center
   :scale: 40 %

**Tester le VCP**

Pour tester votre VCP, démarrez LinuxCNC et choisissez la configuration "vcp1". Assurez vous de
cocher `Créer un raccourcis sur le bureau` pour pouvoir lancer le VCP en un clic.

.. image:: images/vcp1-config-selector_fr.png
   :align: center
   :scale: 60 %

Vous pouvez maintenant voir un VCP vierge avec un menu ajouté.

.. image:: images/vcp1-run-01.png
   :align: center
   :scale: 60 %

Rendez vous à l'emplacement du VCP ``~/vcp1/vcp1`` et ouvrez le fichier `config.yml` avec un
éditeur de texte. Ici, vous pouvez changer l'auteur, la version, la description. Changez la
ligne `menu: ( default_menubar )` en `menu: null` et enregistrez le fichier. Maintenant, exécutez le
configuration vcp1 et vous voyez que le menu a disparu car c'est un tutoriel pour
écran tactile et nous ne voulons pas de menu.

.. image:: images/vcp1-run-02.png
   :align: center
   :scale: 60 %

Le fichier ``mainwindow.py`` est le fichier dans lequel ajouter toutes méthodes personnalisées.

.. note::
    Python utilise l'indentation pour définir des blocs de code. Vous ne devez pas mélanger les espaces
    et les tabulations dans le même fichier.

Le fichier `ui/style.qss` est celui dans lequel mettre les styles CSS. Dans l'exemple suivant, il s'agit d'un
`ActionButton` avec le `actionName` `machine.estop.toggle` et quand il est
coché son arrière plan change au rouge. Le point important à noter est le
`coché`: par défaut, un bouton d'action n'est pas cochable, donc pour que cela fonctionne vous
devez sélectionner cela dans l'`Éditeur de propriété`.

.. code-block:: css

    ActionButton[actionName="machine.estop.toggle"]:checked{
        background: rgb(239, 41, 41);
    }

