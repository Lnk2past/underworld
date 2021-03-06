from underworld.event_manager.event_manager import global_event_manager
from underworld.event_manager.triggers import *
from underworld.units.base_unit import base_unit
from underworld.units.other import bomber_rocket_rocket
from underworld.modules import *
from underworld.traits import *


class sentinel(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 750.0
        self.weapon_slot = battery(6)


class guardian(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 7000.0
        self.weapon_slot = guardian_battery()


class interceptor(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 8000.0
        self.weapon_slot = mass_battery(1)


class colossus(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 40000.0
        self.weapon_slot = colossus_laser()
        self.shield_slot = passive_shield(10)
        self.support_slots = [salvage(12)]
        self.support_slots[0].register(self)


class destroyer(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 10000.0


class bomber(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 48000.0
        self.weapon_slot = bomber_rocket()
        self.weapon_slot.register(self)
        self.set_trigger(enemy_in_neighboring_sector, self.weapon_slot.activate)

    def spawn_bomber_rocket(self):
        brr = bomber_rocket_rocket()
        brr.time = self.time
        brr.corporation = self.corporation
        self.corporation.add(brr)


class phoenix(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 45000.0
        self.weapon_slot = dual_laser(5)
        self.shield_slot = phoenix_area_shield()
        self.set_trigger(death, phoenix.spawn_sentinels)

    @staticmethod
    def spawn_sentinels(s):
        for i in range(3):
            se = sentinel()
            se.time = s.time
            s.corporation.add(se)
            se.corporation = s.corporation

class storm(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 40000.0
        self.weapon_slot = dart_barrage()


class ghost(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 200.0
        self.weapon_slot = ghost_battery()


class weak_cerberus_base(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 20000.0
        self.weapon_slot = weak_cerberus_base_battery()
        self.shield_slot = weak_cerberus_base_passive_shield()


class cerberus_base(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 50000.0
        self.weapon_slot = cerberus_base_battery()
        self.shield_slot = cerberus_base_passive_shield()


class strong_cerberus_base(base_unit, salvageable):
    def __init__(self, name=None):
        super().__init__()
        self.name = self.get_class_name() if name is None else name
        self.hull = self.max_hull = 90000.0
        self.weapon_slot = strong_cerberus_base_battery()
        self.shield_slot = strong_cerberus_base_passive_shield()
