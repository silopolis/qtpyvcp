===================
Installation de développement
===================

Cette méthode d'installation devrait être utilisée si vous songez à
contribuer à `QtPyVCP`, ou souhaitez avoir accès au code
source afin de pouvoir l'étudier et voir comment tout fonctionne.

Ce type d'installation est éditable, ce qui signifie que vous pouvez apporter des modifications aux
fichiers sources et les modifications prendront effet au prochain lancement de `QtPyVCP`
, sans avoir besoin de mettre à jour manuellement ou de réinstaller quoi que ce soit.


.. note::

    Si vous n'êtes **pas** intéressé par le développement, il est plus simple
    d'installer à partir de PyPi selon le guide :doc:`Installation standard <pypi_install_fr>`.


.. Warning::

    Avant de continuer, assurez-vous de satisfaire aux conditions préalables énumérées sur
     à la page :doc:`Prérequis <prerequisites_fr>` !


Obtenir le code source de QtPyVCP
+++++++++++++++++++++++++++++++

Si vous avez l'intention de contribuer à QtPyVCP, vous devriez cloner le
`dépôt QtPyVCP <https://github.com/kcjengr/qtpyvcp>`_ avec git ::

  git clone https://github.com/kcjengr/qtpyvcp qtpyvcp

Sinon, vous pouvez simplement télécharger l'archive du code source :
:download:`qtpyvcp-master.tar.gz <https://github.com/kcjengr/qtpyvcp/tarball/master>`


Installation des dépendances de développement
++++++++++++++++++++++++

Dépendances de développement (en plus de celles listées sur la page :doc:`Prérequis <prerequisites_fr>`) ::

  sudo apt install qttools5-dev qttools5-dev-tools python-wheel

Pour construire la documentation ::

  pip install sphinx sphinx_rtd_theme mock

(Depuis le répertoire ``docs``, exécutez ``make html`` pour construire la documentation HTML.)


**Remarque:** *Nous essayons de garder tout cela à jour, mais si vous trouvez que d'autres
dépendances sont requises, merci d'en informer l'un des développeurs afin qu'elles
puissent être ajoutées.*


Installation avec pip
+++++++++++++++++++++

.. warning::

    Si vous avez précédemment installé QtPyVCP en utilisant la méthode d'installation standard
    vous devriez d'abord désinstaller avec ``pip uninstall qtpyvcp`` avant de continuer
    pour éviter la possibilité de conflits entre plusieurs installations.

Depuis le répertoire source qtpyvcp, installez QtPyVCP en exécutant ::

  pip install --editable .

Ceci va créer une installation de développement setup.py et ajouter des scripts pour la ligne de commande au dossier
``~/.local/bin/`` pour lancer QtPyVCP, les exemples de VCPs et les outils en ligne de commande.

.. hint::
    Si l'installation pip échoue, essayez de désinstaller avant de réessayer:
    ``pip uninstall qtpyvcp``

.. note::
    Sur Debian 9 (Stretch) ``~/.local/bin/`` n'est pas dans le PATH en raison d'une régression dans Bash.
    Cela empêche de lancer ``qtpyvcp`` depuis la ligne de commande ou de pouvoir l'utiliser
    en tant que directive ``[DISPLAY]DISPLAY`` dans le fichier INI de LinuxCNC. Pour une session shell unique,
    vous pouvez contourner ce problème en exécutant ``export PATH=$PATH:~/.local/bin/`` avant de lancer
    ``linuxcnc`` or any ``qtpyvcp`` commands.

    Une solution plus permanente est de copier le fichier ``.xsessionrc`` depuis le
    dossier ``qtpyvcp/scripts`` dans votre répertoire personnel, de vous déconnecter et vous connecter
    à nouveau. Ceci ajoutera ``~/.local/bin/`` à votre ``PATH`` à chaque fois que XWindows
    démarrera. Dans le gestionnaire de fichiers, sélectionnez Affichage > Afficher les fichiers cachés afin de voir
    les fichiers qui commencent par un point comme ``.xsessionrc``.


Test de l'installation
^^^^^^^^^^^^^^^^^^^

Confirmez que QtPyVCP est installé correctement et est disponible en exécutant ::

  qtpyvcp -h

Ceci affichera une liste des options en ligne de commande si l'installation a
réussi.

Plugins QtDesigner
^^^^^^^^^^^^^^^^^^

Si vous souhaitez modifier un VCP ou en créer un à partir d'un modèle, vous devez avoir les
modules Qt Designer installés. Pour charger, vous devez avoir la bonne version de
``libpyqt5.so`` dans le répertoire ``/usr/lib/x86_64-linux-gnu/qt5/plugins/designer/``. Des librairies
pré-compilées adaptées pour Debian 9 (Stretch) 64Bit (ou autre système avec Qt v5.7.1 et
Python v2.7) sont inclus dans le répertoire Qt Designer. Le moyen le plus simple d'installer
les bibliothèques à l'emplacement correct est d'utiliser le script ``install.sh`` situé dans
le répertoire ``qtpyvcp/pyqt5designer/Qt5.7.1-64bit`` avec la commande:
::

    sudo ./install.sh

Si vous utilisez une architecture ou une version de Qt différente, vous devrez peut-être compiler PyQt5 à partir des
sources pour obtenir le fichier ``libpyqt5.so`` approprié. Les étapes devraient être similaires à celles listées
`ici <https://gist.github.com/KurtJacobson/34a2e45ea2227ba58702fc1cb0372c40>`_.

Dépannage
^^^^^^^^^^^^^^^^

Si vous obtenez une erreur `Make sure that you have the correct version of the
libpyqt5.so` vous avez probablement installé la version système de Qt Designer par dessus
la version QtPyVCP. Pour corriger cela, installez simplement ``libpyqt5.so`` avec le script d'installation.
