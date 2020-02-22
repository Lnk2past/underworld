# underworld

Try me now on Binder! [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Lnk2past/underworld/master)

## Overview

For now you can create a team which consists of `battleship` objects outfitted with whatever mods you desire, and then do the same for a second team (which can just be `Cerberus` ships). Once you have the teams set and configured,

### Features

Support for more ships, modules, and behaviors are being added frequently, but a lot is missing still. The following units, modules, etc. are supported (either fully or partially): *italics will denote partial support*.

#### Ships

* battleship
* sentinel
* guardian
* interceptor
* *colossus* - passive shield does not recharge
* *phoenix* - area shield does not cover allies

#### Modules

##### Weapon

* weak battery
* battery
* laser
* mass battery
* dual laser
* *barrage* - does not properly track number of enemies in sector
* *dart laucher* - no dart rocket is launched and is thus not targetable (not realistic when fighting multitarget)

##### Shield

* alpha
* delta
* *passive* - does not recharge
* omega
* *mirror* - no damage reflection
* *blast* - does not cover allies; does not react to explosion damage only
* *area* - does not cover allies

##### Support

* salvage
