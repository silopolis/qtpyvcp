=============
Prérequis
=============

QtPyVCP peut être installé et exécuté sur des ordinateurs et systèmes d'exploitation raisonnablement modernes.
Il y a quelques exigences qui doivent être satisfaites, cependant, et il est préférable de
de vérifier que le système est effectivement capable d'exécuter QtPyVCP avant de l'installer.

Ces exigences sont les mêmes indépendamment de la méthode d'installation.


Configuration requise
-------------------

* Debian 9 (Stretch) et 10 (buster) ou Linux Mint 19, 64 bits
* LinuxCNC **2.8** ou supérieur, soit installé pour l'ensemble du système, soit en tant que compilation Run In Place (RIP) à partir des sources
* Carte graphique prenant en charge OpenGL 1.50 ou ultérieur (pour la visualisation VTK)

.. note::
    QtPyVCP requiert un système d'exploitation 64 bits, les systèmes 32 bits ne sont **pas** pris en charge.

Les instructions pour installer LinuxCNC sur Debian 9 (stretch) et d'autres distributions
peuvent être trouvées ici : https://gnipsel.com/linuxcnc/uspace/debian9-emc.html


Dépendances logicielles
---------------------

Ces paquets devraient être installés avant d'essayer d'installer QtPyVCP.

::

  sudo apt install python-pyqt5 python-dbus.mainloop.pyqt5 python-pyqt5.qtopengl python-pyqt5.qsci python-pyqt5.qtmultimedia python-pyqt5.qtquick qml-module-qtquick-controls gstreamer1.0-plugins-bad libqt5multimedia5-plugins pyqt5-dev-tools python-dev python-setuptools python-wheel python-pip git
