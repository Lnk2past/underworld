import math
from underworld.event_manager.event_manager import global_event_manager
from underworld.modules import *


class base_unit:
    @classmethod
    def get_class_name(cls):
        return cls.__name__

    def __init__(self):
        self.position = [0.0, 0.0]
        self.corporation = []
        self.queued_damage = 0.0
        self.queued_shield_damage = 0.0
        self.time = 0.0
        self.targets = {}
        self.targeted_by = []
        self.triggers = {}

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.get_class_name()}::{self.name}'

    def distance_to(self, unit):
        return math.sqrt((unit.position[0] - self.position[0])**2 + (unit.position[1] - self.position[1])**2 )

    @property
    def weapon(self):
        return self.weapon_slot

    @property
    def shield(self):
        return self.shield_slot.strength if self.shield_slot is not None else 0.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield

    @property
    def damage(self):
        return self.weapon_slot.damage

    def damage_applied(self, time, **kwargs):
        return self.weapon_slot.damage_applied(time, **kwargs)

    def update(self, dt):
        self.time += dt
        for t in self.targets:
            if isinstance(self.weapon_slot, dual_laser):
                if len(self.targets.keys()) != 2:
                    self.targets[t] = 0.0
                else:
                    self.targets[t] = self.targets[max(self.targets, key=lambda x: self.targets[x])]

            dps = self.weapon_slot.dps_after_time(self.targets[t])
            t.queue_damage(dps * dt)
            self.targets[t] += dt
        if self.weapon_slot is not None:
            self.weapon_slot.update(dt)
        if self.shield_slot is not None:
            self.shield_slot.update(dt)
        for support_slot in self.support_slots:
            support_slot.update(dt)

    def queue_damage(self, damage):
        for t in self.corporation:
            if damage > 0.0 and t is not self:
                # check distance!
                if isinstance(t.shield_slot, area_shield_module) and t.queued_shield_damage < t.shield:
                    t.queued_shield_damage, damage = min(t.shield, t.queued_shield_damage + damage), max(0.0, damage - (t.shield - t.queued_shield_damage))
        if damage > 0.0 and self.shield_slot is not None and self.queued_shield_damage < self.shield:
            self.queued_shield_damage, damage = min(self.shield, self.queued_shield_damage + damage), max(0.0, damage - (self.shield - self.queued_shield_damage))

        if damage > 0.0:
            self.queued_damage += damage

    def apply_damage(self):
        if self.shield_slot is not None and self.queued_shield_damage:
            self.shield_slot.strength -= self.queued_shield_damage
        self.hull -= self.queued_damage
        self.queued_damage = 0.0
        self.queued_shield_damage = 0.0

    def finalize(self):
        if self.hull <= 0:
            global_event_manager.notify(self.time, 'sector_death', {'sector': 1, 'unit': self})
        if self.shield <= 0 and isinstance(self.shield_slot, activated_module) and self.shield_slot.activated:
            self.shield_slot.deactivate()
        for condition in self.triggers:
            if condition(self):
                for callback in self.triggers[condition]:
                    if callback(self):
                        # print(self.time, self.name, 'successful activation')
                        pass

    def target(self, target):
        if target not in self.targets:
            self.targets[target] = 0.0
            global_event_manager.register('sector_death', self.untarget)

    def untarget(self, payload):
        if payload.get('unit', None) in self.targets:
            del self.targets[payload['unit']]

    def trigger_on(self, condition, callback):
        if condition not in self.triggers:
            self.triggers[condition] = []
        self.triggers[condition].append(callback)
