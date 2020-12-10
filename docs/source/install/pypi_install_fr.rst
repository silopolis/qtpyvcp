================
Installation standard
================

Ces instructions installeront la version actuelle de `QtPyVCP` à partir de PyPi,
comprenant des exemples de configurations pour LinuxCNC et Qt Designer pour l'édition des VCPs.

.. Note::

    Avec l'installation standard, vous pourrez créer et éditer des VCPs
    tiers, mais vous ne serez **pas** en mesure de modifier les exemples de VCPs inclus avec
    `QtPyVCP` ou d'éditer le code source de `QtPyVCP` lui-même. Si vous souhaitez le faire
    vous devrez utiliser la méthode :doc:`Installation de développement <dev_install_fr>`.


.. Warning::

    Avant de continuer, assurez-vous que vous satisfaisait aux conditions préalables énumérées sur
    la page :doc:`Prérequis <prerequisites>` !


Installation de QtPyVCP
+++++++++++++++

::

  pip install qtpyvcp

Ceci installera QtPyVCP avec les exemples, et ajoutera
les configurations sim spécifiques à QtPyVCP dans ``~/linuxcnc/configs/sim.qtpyvcp``.

.. note::
    Sur Debian, vous devrez vous déconnecter et vous reconnecter.


Mettre à jour QtPyVCP
+++++++++++++++

A mesure des améliorations apportées à QtPyVCP, vous pouvez mettre à jour une installation `pip` avec:
::

  pip install --upgrade qtpyvcp
