==============
Boutons d'action
==============

**Syntaxe**

La syntaxe de bouton d'action pour `nomAction` est
`group.action.subaction:argument=item`. Certains éléments d'action prennent un argument
optionnel comme ``spindle.override.reset:2`` pour réinitialiser la dérogation pour une
broche numéro 2.

-------------------
**Actions de refroidissement**
-------------------

**Arrosage** `actionNames` pour `ActionButtons`
::

    coolant.flood.off
    coolant.flood.on
    coolant.flood.toggle

**Brouillard** `actionNames` pour `ActionButtons`
::

    coolant.mist.off
    coolant.mist.on
    coolant.mist.toggle

-------------------
**Actions machine**
-------------------

**Arrêt d'urgence (E Stop)** `actionNames` pour `ActionButtons`
::

    machine.estop.activate
    machine.estop.reset
    machine.estop.toggle

**Dérogation d'avance** `actionNames` pour `ActionButtons`
::

    machine.feed-override.disable
    machine.feed-override.enable
    machine.feed-override.reset
    machine.feed-override.set:value
    machine.feed-override.toggle-enable

**Origine** `actionNames` pour `ActionButtons`
::

    machine.home.all
    machine.home.axis:axis lettre
    machine.home.joint:joint numero

**Lancer MDI** `actionNames` pour `ActionButtons`
Note: Utilisez MDIButton pour les commandes MDI
::

    machine.issue-mdi:command

**Jog** `actionNames` pour `ActionButtons`
::

    machine.jog.axis.axis letter,direction,speed,distance
    machine.jog.set-angular-speed.value
    machine.jog.set-increment.raw increment
    machine.jog.set-jog-continuous
    machine.jog.set-linear-speed.value

**Jog Mode** `actionNames` pour `ActionButtons`
::

    machine.jog-mode.continuous
    machine.jog-mode.incremental
    machine.jog-mode.toggle

**Vitesse Max** `actionNames` pour `ActionButtons`
::

    machine.max-velocity.set
    machine.max-velocity.reset

**Mode** `actionNames` pour `ActionButtons`
::

    machine.mode.auto
    machine.mode.manual
    machine.mode.toggle

**Alimentation** `actionNames` pour `ActionButtons`
::

    machine.power.off
    machine.power.on
    machine.power.toggle

**Annuler l'origine** `actionNames` pour `ActionButtons`
::

    machine.unhome.all
    machine.unhome.axis:axis lettre
    machine.unhome.joint:joint numero

-------------------
**Actions de programme**
-------------------

**Interrompre** `actionNames` pour `ActionButtons`
::

    program.abort

**Blocs Optionnels** `actionNames` pour `ActionButtons`
::

    program.block-delete.off
    program.block-delete.on
    program.block-delete.toggle

**Saut Optionnel** `actionNames` pour `ActionButtons`
::

    program.

**Arrêt optionnel** `actionNames` pour `ActionButtons`
::

    program.option-stop.off
    program.optional-stop.on
    program.optional-stop.toggle

**Mise en pause Programme** `actionNames` pour `ActionButtons`
::

    program.pause

**Reprise du Programme** `actionNames` pour `ActionButtons`
::

    program.resume

**Exécuter le Programme** `actionNames` pour `ActionButtons`

``run`` a un argument optionnel ``start line`` (ligne de départ), remplacez `n` par le numéro de ligne.
::

    program.run
    program.run:n

**Bloc à bloc** `actionNames` pour `ActionButtons`
::

    program.step

-------------------
**Actions de broche**
-------------------

Les actions de broche ont un argument optionnel `spindle` pour le numéro de broche. Si il est absent, la broche 0 est considérée
par défaut. Pour spécifier une broche, remplacez `spindle` dans les exemples avec le
numéro de broche.


**Frein** `actionNames` pour `ActionButtons`
::

    spindle.brake.off
    spindle.brake.off:spindle
    spindle.brake.on
    spindle.brake.on:spindle
    spindle.brake.toggle
    spindle.brake.toggle:spindle

**Accélérer** `actionNames` pour `ActionButtons`

Augmente la vitesse de la broche de 100 tpm
::

    spindle.faster
    spindle.faster:spindle

**En avant** `actionNames` pour `ActionButtons`

Rotation de la broche dans la direction avant
::

    spindle.forward
    spindle.forward:speed
    spindle.forward:speed,spindle

**Arrêt** `actionNames` pour `ActionButtons`
::

    spindle.off
    spindle.off:spindle

**Dérogation** `actionNames` pour `ActionButtons`

Définit le pourcentage de dérogation de vitesse de broche. Utilisé avec un ActionSlider vous pouvez omettre la
vitesse.
::

    spindle.override
    spindle.override:speed
    spindle.override:speed,spindle

**En arrière** `actionNames` pour `ActionButtons`
::

    spindle.reverse
    spindle.reverse:speed
    spindle.reverse:speed,spindle

**Ralentir** `actionNames` pour `ActionButtons`

Diminuer la vitesse de broche de 100 tpm
::

    spindle.slower
    spindle.slower:spindle

----------------
**Actions des outils**
----------------

**Étalonnage** `actionNames` pour `ActionButtons`
::

    tool_actions.calibration

**Halmeter** `actionNames` pour `ActionButtons`
::

    tool_actions.halmeter

**Halscope** `actionNames` pour `ActionButtons`
::

    tool_actions.halscope

**Halshow** `actionNames` pour `ActionButtons`
::

    tool_actions.halshow

**Simuler le Palpeur** `actionNames` pour `ActionButtons`
::

    tool_actions.simulate_probe

**Etat** `actionNames` pour `ActionButtons`
::

    tool_actions.status

