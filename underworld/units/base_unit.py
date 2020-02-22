from underworld.event_manager.event_manager import global_event_manager
from underworld.modules import *


class base_unit:
    @classmethod
    def get_class_name(cls):
        return cls.__name__

    def __init__(self):
        self.team = None
        self.queued_damage = 0.0
        self.time = 0.0
        self.targets = {}
        self.targeted_by = []
        self.triggers = {}

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.get_class_name()}::{self.name}'

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
        for condition in self.triggers:
            if condition(self):
                for callback in self.triggers[condition]:
                    callback(self)

    def queue_damage(self, damage):
        self.queued_damage += damage

    def apply_damage(self):
        if self.shield_slot is not None and self.shield_slot.strength > 0:
            self.shield_slot.strength, self.queued_damage = max(0.0, self.shield - self.queued_damage), max(0.0, self.queued_damage - self.shield)
        self.hull -= self.queued_damage
        self.queued_damage = 0.0
        if self.hull <= 0:
            global_event_manager.notify(self.time, 'sector_death', {'sector': 1, 'unit': self})

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
