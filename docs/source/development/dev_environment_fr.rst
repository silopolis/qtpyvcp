Guide de développement
^^^^^^^^^^^^^^^^^

Si vous commencez à travailler avec git, cela devrait vous permettre de démarrer.


Création d'une extraction locale
=========================

Si vous souhaitez apporter des modifications à QtPyVCP la première étape est de créer votre propre "fork"
du dépôt. Cela vous permet de créer des branches de fonctionnalités et de pousser les changements
dans votre "fork" personnel pour que les autres puissent les voir et les tester, sans que vous ayez
à vous inquiéter de mettre la pagaille dans le dépôt principal. Il est facile de créer un fork,
mais voici un `tutoriel rapide <https://help.github.com/articles/fork-a-repo>`_
si nécessaire.

Une fois votre fork créé, vous pouvez le cloner sur votre machine locale.

.. code:: sh

   $ git clone https://github.com/YOUR-USERNAME/REPOSITORY.git

Maintenant que vous avez une copie du dépôt, créez une branche pour la fonctionnalité ou
le bogue sur laquelle vous souhaitez travailler.

.. code:: sh

   $ git checkout -b my-feature

   $ git status
   On branch my-feature
   nothing to commit, working tree clean

.. admonition:: ProTip

    Je recommande vivement un client git graphique appelé `GitKraken <https://www.gitkraken.com/>`_.
    Il permet de réaliser les tâches git, même compliquées, en quelques clics, et
    l'historique des visuel des révisions est d'une grande aide.


Fusion des modifications
===============

Une fois satisfait de votre code, "poussez le" avec ``push`` dans votre fork sur GitHub.

.. code:: sh

   $ git push origin my-feature

Vous devriez maintenant être en mesure de créer une demande d'ajout ("Pull Request") vers le dépôt original.
Une fois que les modifications ont été vérifiées et examinées, la requête peut être fusionnée.


Synchronisation de votre extraction locale
===========================

Inévitablement, des changements dans le dépôt amont se produiront et vous devrez
mettre à jour votre "checkout" local pour les refléter. La première étape est d'ajouter le dépôt amont
à la liste des dépôts distants du "checkout" local:

.. code:: sh

   $ git remote add upstream https://github.com/kcjengr/qtpyvcp.git
   $ git remote -v
   origin   https://github.com/YOUR-USERNAME/qtpyvcp.git (fetch)
   origin   https://github.com/YOUR-USERNAME/qtpyvcp.git (push)
   upstream https://github.com/kcjengr/qtpyvcp.git (fetch)
   upstream https://github.com/kcjengr/qtpyvcp.git (push)

Maintenant, vous devez récupérer tous les changements depuis le dépôt amont. ``git fetch``
va récupérer les dernières révisions qui ont été fusionnées depuis que vous avez fait votre fork.

.. code:: sh

   $ git fetch upstream


Idéalement, vous n'avez apporté aucun changement à votre branche ``master``. Vous devriez donc être
capable de fusionner la dernière branche ``master`` depuis le dépôt amont sans
problème. Tout ce que vous avez à faire est de basculer vers votre branche ``master``, et de tirer
les changements par rapport au dépôt amont. Il est généralement une bonne idée de pousser tous
les modifications aussi dans votre fork:

.. code:: sh

   $ git checkout master
   $ git pull upstream master
   $ git push origin master

Enfin, vous devez mettre à jour votre branche de fonctionnalité pour qu'elle intègre les nouvelles modifications. Il est
préférable d'utiliser un ``git rebase`` pour prendre les changements locaux, les supprimer temporairement,
tirer les modifications en amont, puis ré-ajouter les modifications locales sur le
sommet de l'historique des révisions. Ceci évite que les révisions de fusion externes viennent encombrer
l'historique des révisions de la branche. Une discussion plus approfondie peut être trouvée `ici
<https://www.atlassian.com/git/tutorials/merging-vs-rebasing>`__. Ce procédé
ressemblerait à quelque chose comme ceci :

.. code:: sh

   $ git checkout my-feature
   $ git rebase upstream/master

.. warning::
   Un ``rebase`` ne devrait pas être réalisé si vous pensez que quelqu'un d'autre
   travaille aussi sur la branche. ``rebase`` réécrit l'historique des révisions de telle manière que
   tout autre "checkout" de la même branche aura l'ancien historique.
   Ainsi, quand elle finiront par être fusionnées, il y aura des doublons de toutes
   les révisions ``rebase``. Ce qui défait l'intérêt du ``rebase`` :)
