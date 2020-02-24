from underworld.event_manager.event_manager import global_event_manager
from underworld.units.base_unit import base_unit
from underworld.modules import *
from underworld.event_manager.actions import *
from underworld.event_manager.triggers import *


class alpha_rocket_rocket(base_unit):
    pass


class delta_rocket_rocket(base_unit):
    pass


class omega_rocket_rocket(base_unit):
    pass


class dart_launcher_rocket(base_unit):
    pass


class bomber_rocket_rocket(base_unit):
    def __init__(self):
        super().__init__()
        self.name = 'bomber_rocket_rocket'
        self.hull = 1000.0
        self.explosion = 4000.0
        self.neutralized = 1250.0
        self.weapon_slot = None
        self.shield_slot = None
        self.support_slots = []
        self.trigger_on(death(), neutralized)

class ghost_dart_launcher_rocket(base_unit):
    pass
