Guide de contribution
^^^^^^^^^^^^^^^^^^

Il y a plusieurs façons de contribuer à QtPyVCP, et toutes sont encouragées et
très appréciées:

- contributions aux rapports de bogue et aux demandes de fonctionnalités

- contributions à la documentation (et, oui, cela inclut ce document)

- examiner et trier les bogues et les demandes de fusion

- tester et fournir des commentaires sur les problèmes / bugs

Avant d'aller plus loin, soyez assuré que votre contribution, aussi modeste soit-elle,
*est* précieuse. Même si c'est quelque chose d'aussi simple que de corriger une faute d'orthographe,
ou de clarifier une phrase dans la documentation.


Lignes directrices
==========

Nous n'avons pas de lignes directrices strictes, vous êtes encouragés à contribuer
de quelque manière que ce soit, et surtout, amusez-vous
en espérant que vous apprendrez quelque en chemin. Cela étant dit, ci-dessous
sont regroupées quelques recommandations qui devraient faciliter la tâche pour tous les développements.


Flux de travail de développement
====================

En général, nous essayons d'utiliser le flux de travail *Branche Fonctionnelle et Demandes de Fusions*.
Si vous n'êtes pas familier avec les flux de travail git, ne vous inquiétez pas, c'est très
simple (et nous ne sommes pas stricts à ce sujet de toute façon).


Messages de révisions
===============

Bien que ce ne soit pas obligatoire, il est bien de préfixer les messages de révision
avec un TLA (Three Letter Acronym: Acronyme à Trois Lettres) indiquant le type de la révision. Ceci facilite
de parcourir visuellement le journal des révisions et de voir quels types de changements
ont été faits. Cela facilite également le filtrage de certains types de révisions.
Par exemple, pour voir toutes les révisions de type BugFix, vous pouvez utiliser ``git log --grep=BUG``.
Peut-être le plus important, les préfixes de révisions sont utilisés pour générer automatiquement le journal
des changements pour chaque version.

===   ===
TLA   Description
===   ===
API une modification (incompatible) de l'API
BLD changement lié à la construction
BUG correction de bogue
DEP déprécie quelque chose, ou supprime un objet obsolète
DEV outil de développement ou utilitaire
DOC   documentation
ENH   amélioration
MNT   révision de maintenance (remaniement, coquilles, etc.)
REV   annulation d'une révision antérieure
STY   correction de style (espacement, PEP8)
TST   Ajout de ou modification de tests
REL   lié à une publication (incrémentation des numéros de version, etc.)
WIP   travail en cours
SIM changements liés aux configurations LinuxCNC sim
VCP   travail sur les VCPs exemple
===   ===

Dans cet esprit, un message de révision idéal pourrait ressembler à ceci :

.. code-block:: none

  DOC: ajouter un exemple de message de révision aux directives de développement (Voir #42)

  La première ligne d'un message de révision devrait commencer par un acronyme en majuscule
  (options dans le tableau ci-dessus) indiquant le type de révision, et un court résumé.
  Si la révision est liée à un ticket GitHub, indiquez cela avec
  une mention "Fixes #42" (corrige), "See #42" (voir), "Closes #42" (ferme) ou similaire.

  Si cela ne suffit pas pour décrire complètement la révision, ajoutez une ligne vide
  puis autant de texte que nécessaire. Les lignes ne doivent pas contenir plus de 72 caractères afin
  de s'afficher correctement lors de la consultation du journal git dans un terminal.

Vivons-nous dans un monde idéal ? Non. Pas de problème si vos messages de révision s'écartent
de ce format, mais vous devriez au moins essayer d'utiliser des ATLs pour les révisions que
vous souhaiteriez voir apparaître dans les journaux de changement.


Docstrings Python
=================

Il est appréciable que vous documentiez votre code en écrivant des "docstrings" (documentation) pour tous les
modules, classes et fonctions Python. Celles-ci sont automatiquement converties par Sphinx en
documentation HTML. Les "docstrings" doivent suivre les directives de style Google, dont un exemple
peut être trouvé `ici
<https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`__.
