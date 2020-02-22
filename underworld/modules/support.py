from underworld.event_manager.event_manager import global_event_manager


class support_module:
    def __init__(self, level):
        if level < 1 or level > 12:
            raise RuntimeError(f'Module {level} needs to be between 1 and 12!')


class emp(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True

    def _set_level(self, level):
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

    def activate(self, ships):
        pass
        # for s in ships:
        #     s.apply_status('emp')

class teleport(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
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


class red_star_life_extender(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass


class remote_repair(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class time_warp(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class unity(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class sanctuary(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class stealth(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class fortify(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class impulse(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class alpha_rocket(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class salvage(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.level = level
        self.is_activated = False

    def _set_level(self, level):
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
        if payload.get('sector', None) is not None:
            self.owner.hull = min(self.owner.hull + self.repair_percentage * self.owner.max_hull, self.owner.max_hull)


class suppress(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class destiny(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class barrier(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class vengeance(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class delta_rocket(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class leap(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class bond(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class alpha_drone(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class suspend(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



class omega_rocket(support_module):
    def __init__(self, level):
        super().__init__(level)
        self._set_level(level)
        self.is_activated = True


    def _set_level(self, level):
        pass



