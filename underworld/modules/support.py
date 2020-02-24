from underworld.event_manager.event_manager import global_event_manager
from underworld.modules import *
from underworld.traits import *


class support_module():
    pass


class activated_support_module(support_module, activated_module):
    pass


class passive_support_module(support_module, passive_module):
    pass


class emp(activated_support_module):
    def __init__(self, level):
        self.set_level(level)

    def set_level(self, level):
        super().set_level(level)
        if level == 1:  self.duration, self.hydrogen = [30,   40.0]
        if level == 2:  self.duration, self.hydrogen = [33,   80.0]
        if level == 3:  self.duration, self.hydrogen = [36,  150.0]
        if level == 4:  self.duration, self.hydrogen = [38,  250.0]
        if level == 5:  self.duration, self.hydrogen = [40,  400.0]
        if level == 6:  self.duration, self.hydrogen = [42,  600.0]
        if level == 7:  self.duration, self.hydrogen = [44,  800.0]
        if level == 8:  self.duration, self.hydrogen = [46, 1000.0]
        if level == 9:  self.duration, self.hydrogen = [48, 1250.0]
        if level == 10: self.duration, self.hydrogen = [50, 1500.0]
        if level == 11: self.duration, self.hydrogen = [52, 1750.0]
        if level == 12: self.duration, self.hydrogen = [54, 2000.0]


class teleport(activated_support_module):
    def __init__(self, level):
        self.set_level(level)

    def set_level(self, level):
        super().set_level(level)
        if level == 1:  self.duration, self.hydrogen = [30,    40.0]
        if level == 2:  self.duration, self.hydrogen = [33,    80.0]
        if level == 3:  self.duration, self.hydrogen = [36,   150.0]
        if level == 4:  self.duration, self.hydrogen = [38,   250.0]
        if level == 5:  self.duration, self.hydrogen = [40,   400.0]
        if level == 6:  self.duration, self.hydrogen = [42,   600.0]
        if level == 7:  self.duration, self.hydrogen = [44,   800.0]
        if level == 8:  self.duration, self.hydrogen = [46,  1000.0]
        if level == 9:  self.duration, self.hydrogen = [48,  1250.0]
        if level == 10: self.duration, self.hydrogen = [50,  1500.0]
        if level == 11: self.duration, self.hydrogen = [52,  1750.0]
        if level == 12: self.duration, self.hydrogen = [54,  2000.0]


class red_star_life_extender(activated_support_module):
    def __init__(self, level):
        self.set_level(level)


class remote_repair(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class time_warp(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class unity(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class sanctuary(passive_support_module):
    def __init__(self, level):
        self.set_level(level)



class stealth(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class fortify(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class impulse(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class alpha_rocket(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class salvage(passive_support_module):
    def __init__(self, level):
        self.set_level(level)
        self.level = level
        self.is_activated = False

    def set_level(self, level):
        super().set_level(level)
        if level == 1:  self.repair_percentage, self.hydrogen = [ 0.6,   2.0]
        if level == 2:  self.repair_percentage, self.hydrogen = [ 0.7,   5.0]
        if level == 3:  self.repair_percentage, self.hydrogen = [ 0.8,   8.0]
        if level == 4:  self.repair_percentage, self.hydrogen = [ 0.9,  11.0]
        if level == 5:  self.repair_percentage, self.hydrogen = [0.10,  14.0]
        if level == 6:  self.repair_percentage, self.hydrogen = [0.12,  17.0]
        if level == 7:  self.repair_percentage, self.hydrogen = [0.14,  20.0]
        if level == 8:  self.repair_percentage, self.hydrogen = [0.16,  23.0]
        if level == 9:  self.repair_percentage, self.hydrogen = [0.18,  26.0]
        if level == 10: self.repair_percentage, self.hydrogen = [0.20,  29.0]
        if level == 11: self.repair_percentage, self.hydrogen = [0.22,  30.0]
        if level == 12: self.repair_percentage, self.hydrogen = [0.24,  32.0]

    def register(self, entity):
        self.owner = entity
        global_event_manager.register('sector_death', self.heal_owner)

    def heal_owner(self, payload):
        sector = payload.get('sector', None)
        unit = payload.get('unit', None)
        if sector is not None and isinstance(unit, salvageable):
            self.owner.hull = min(self.owner.hull + self.repair_percentage * self.owner.max_hull, self.owner.max_hull)


class suppress(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class destiny(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class barrier(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class vengeance(passive_support_module):
    def __init__(self, level):
        self.set_level(level)



class delta_rocket(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class leap(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class bond(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class alpha_drone(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class suspend(activated_support_module):
    def __init__(self, level):
        self.set_level(level)



class omega_rocket(activated_support_module):
    def __init__(self, level):
        self.set_level(level)
