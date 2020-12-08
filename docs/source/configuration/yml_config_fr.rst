=================
Fichiers de configuration YAML
=================

Au cœur de chaque VCP basé sur QtPyVCP se trouve un fichier de configuration
YAML. Ce fichier est probablement plus important que tout autre fichier, puisqu'il
définit comment les fichiers ``.ui``, ``.py`` et ``.qss`` se regroupent pour créer
un VCP complet.

Plusieurs fichiers de configuration sont utilisés à différents niveaux, et
une fois combinés et fusionnés déterminent la configuration finale du
VCP.

Au niveau le plus bas se trouve le fichier ``default_config.yml``. Ce fichier
n'est pas modifiable par l'utilisateur et est toujours chargé. Il définit les éléments de
essentiels qui doivent exister pour que le VCP le plus basique puisse fonctionner.

Au niveau suivant se trouve le fichier de configuration spécifique au VCP. C'est
à ce niveau que les VCPs sont définit individuellement, et ne sont généralement édités que
les développeurs du VCP. Il inclut des informations de base telles que le nom du VCP et son auteur,
ainsi que les fichiers ``.ui``, ``.py`` et ``.qss`` à utiliser lors du chargement du VCP.
C'est aussi là que les menus spécifiques du VCP, les dialogues, etc. sont définis.

Au niveau le plus haut se trouve le fichier de configuration spécifique à la machine. Ce
fichier se trouve généralement dans le dossier de configuration avec le fichier INI. Il
n'est pas requis mais peut être utilisé pour modifier les paramètres de configuration pour une
machine particulière.

Plus d'informations sur les fichiers YAML peuvent être trouvées sur 
`Wikipedia <https://en.wikipedia.org/wiki/YAML>`_
