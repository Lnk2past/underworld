from underworld.units.base_unit import base_unit
from underworld.modules import *


class battleship(base_unit):
    def __init__(self, level=1, *modules, name=None):
        super().__init__()
        if level < 1 or level > 6:
            raise RuntimeError(f'Battleship {level} needs to be between 1 and 6!')
        self.name = self.get_class_name() if name is None else name
        self.level = level
        self.speed = 600.0
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
        module.register(self)

    def clear(self):
        self.weapon_slot = weak_battery
        self.shield_slot = None
        self.support_slots = []

    def _set_level(self, level):
        if level == 1:
            self.hull = self.max_hull = 4000.0
            self.hydrogen = 2.8
            self.jump_cost = 20
            self.support_slots = {}
        if level == 2:
            self.hull = self.max_hull = 5000.0
            self.hydrogen = 4.2
            self.jump_cost = 50
        if level == 3:
            self.hull = self.max_hull = 6000.0
            self.hydrogen = 12.0
            self.jump_cost = 80
        if level == 4:
            self.hull = self.max_hull = 7500.0
            self.hydrogen = 24.0
            self.jump_cost = 120
        if level == 5:
            self.hull = self.max_hull = 9000.0
            self.hydrogen = 40.0
            self.jump_cost = 200
        if level == 6:
            self.hull = self.max_hull = 9500.0
            self.hydrogen = 44.0
            self.jump_cost = 240

