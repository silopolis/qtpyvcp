===========
Utilisation de base
===========

À ce stade, vous devriez avoir les dépendances satisfaites et QtPyVCP devrait être installé.

Lancer une configuration sim
^^^^^^^^^^^^^^^^^^^^^^
Plusieurs configurations sim sont incluses avec QtPyVCP, elles devraient avoir été
copiées dans votre dossier ``~/linuxcnc`` lorsque vous avez installé QtPyVCP. Sinon,
exécutez ``$ cp -r linuxcnc $HOME`` depuis le répertoire ``qtpyvcp`` pour les installer.


**Configuration SIM incluses**::

  sim.qtpyvcp
  ├── hal-widgets.ini
  ├── xyz.ini
  ├── xyz3s.ini
  ├── xyz-metric.ini
  ├── xyzab.ini
  ├── xyzb.ini
  ├── xyzcw.ini
  └── xyzy-gantry.ini

Pour lancer la machine XYZ de base, exécutez ::

  linuxcnc ~/linuxcnc/configs/sim.qtpyvcp/xyz.ini

Cela devrait démarrer LinuxCNC et afficher le sélecteur de panneau de contrôle avec la liste des
VCPs disponibles.

.. figure:: /_static/vcp-chooser.png

    Fenêtre de dialogue du Sélecteur de VCP

**Note :** S'il n'y a pas de VCPs listés, il est fort probable que vous n'ayez pas exécuté
``setup.py`` selon les instructions d'installation.

Pour passer le sélecteur de VCPs et lancer un VCP directement, vous pouvez spécifier le nom de
du VCP souhaité sur la ligne de commande. Par exemple pour lancer le VCP "Mini":
``linuxcnc ~/linuxcnc/configs/sim.qtpyvcp/xyz.ini mini``


Configuration INI
^^^^^^^^^^^^^^^^^

QtPyVCP ne nécessite aucun paramètre INI particulier. Pour définir QtPyVCP comme
interface éditez simplement l'entrée ``DISPLAY`` du fichier INI pour lire ::

    [DISPLAY]
    DISPLAY = qtpyvcp
    ...

Ceci affichera le sélecteur de VCP chaque fois que vous démarrerez LinuxCNC, mais comme nous l'avons vu
précédemment, il est possible de préciser un VCP spécifique sur la ligne de commande. Nous pouvons
en faire de même dans le fichier INI ::

    [DISPLAY]
    DISPLAY = qtpyvcp mini
    ...

Mais comme QtPyVCP prend en charge un tas d'options de ligne de commande, cela peut devenir désordonné.
Nous pouvons tirer avantage du fait que lorsque QtPyVCP démarre, il analyse la section ``[DISPLAY]``
du fichier INI à la recherche de tous les éléments correspondant aux noms des options en ligne de commande,
et les fusionne avec toutes les options spécifiées sur la ligne de commande.

Ainsi une meilleure configuration INI ressemblerait à ceci ::

    [DISPLAY]
    DISPLAY = qtpyvcp
    VCP = mini
    ...

En général, les options en ligne de commande ont la priorité, ce qui signifie qu'elles remplaceront
celles définies dans le fichier INI. L'exception à cela sont tous les drapeaux, tels que
l'àption ``--fullscreen`` qui, si spécifiée dans l'INI, ne peut pas être remplacée sur
la ligne de commande.
