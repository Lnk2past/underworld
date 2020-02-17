from underworld.modules import *

class battleship:
    def __init__(self, level=1, *modules):
        if level < 1 or level > 6:
            raise RuntimeError(f'Battleship {level} needs to be between 1 and 6!')
        self.level = level
        self.speed = 600.0
        self.attack_range = 120.0
        self.weapon_slot = weak_battery
        self.shield_slot = None
        self.support_slots = []
        self._set_level(level)
        for module in modules:
            self.set(module)

    def set(self, module):
        if isinstance(module, weapon_module):
            self.weapon_slot = module
        if isinstance(module, shield_module):
            self.shield_slot = module
        if isinstance(module, support_module):
            if len(self.support_slots) < self.level - 1 and module not in self.support_slots:
                self.support_slots.append(module)

    def clear(self):
        self.weapon_slot = weak_battery
        self.shield_slot = None
        self.support_slots = []

    @property
    def damage(self):
        return self.weapon_slot.damage

    def damage_applied(self, time, **kwargs):
        return self.weapon_slot.damage_applied(time, **kwargs)

    def _set_level(self, level):
        if level == 1:
            self.hull = 4000.0
            self.hydrogen = 2.8
            self.jump_cost = 20
            self.support_slots = {}
        if level == 2:
            self.hull = 5000.0
            self.hydrogen = 4.2
            self.jump_cost = 50
        if level == 3:
            self.hull = 6000.0
            self.hydrogen = 12.0
            self.jump_cost = 80
        if level == 4:
            self.hull = 7500.0
            self.hydrogen = 24.0
            self.jump_cost = 120
        if level == 5:
            self.hull = 9000.0
            self.hydrogen = 40.0
            self.jump_cost = 200
        if level == 6:
            self.hull = 9500.0
            self.hydrogen = 44.0
            self.jump_cost = 240

