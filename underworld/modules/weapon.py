class weapon_module:
    def __init__(self, level):
        if level < 1 or level > 12:
            raise RuntimeError(f'Module {level} needs to be between 1 and 12!')

    def dps_after_time(self, time):
        if time < 45.0:
            r = (self.max_damage - self.damage) / 45.0
            return self.damage + r * time
        return self.max_damage


class weak_battery(weapon_module):
    def __init__(self):
        super().__init__(level)
        self.level = 1
        self.damage = self.max_damage = 80
        self.max_targets = 1

    def damage_applied(self, time, **kwargs):
        return self.damage * time


class battery(weapon_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)

    def _set_level(self, level):
        self.max_targets = 1
        if level == 1:  self.damage, self.hydrogen = [100,  0.4]
        if level == 2:  self.damage, self.hydrogen = [120,  0.8]
        if level == 3:  self.damage, self.hydrogen = [140,  1.6]
        if level == 4:  self.damage, self.hydrogen = [160,  2.8]
        if level == 5:  self.damage, self.hydrogen = [180,  4.0]
        if level == 6:  self.damage, self.hydrogen = [210,  6.0]
        if level == 7:  self.damage, self.hydrogen = [250,  9.0]
        if level == 8:  self.damage, self.hydrogen = [285, 12.0]
        if level == 9:  self.damage, self.hydrogen = [315, 16.0]
        if level == 10: self.damage, self.hydrogen = [340, 20.0]
        if level == 11: self.damage, self.hydrogen = [365, 24.0]
        if level == 12: self.damage, self.hydrogen = [390, 28.0]
        self.max_damage = self.damage

    def damage_applied(self, time, **kwargs):
        return self.damage * time 


class laser(weapon_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)

    def _set_level(self, level):
        self.max_targets = 1
        if level == 1:  self.damage, self.max_damage, self.hydrogen = [ 80,  200,  1.0]
        if level == 2:  self.damage, self.max_damage, self.hydrogen = [ 90,  240,  2.0]
        if level == 3:  self.damage, self.max_damage, self.hydrogen = [100,  280,  3.0]
        if level == 4:  self.damage, self.max_damage, self.hydrogen = [120,  325,  4.0]
        if level == 5:  self.damage, self.max_damage, self.hydrogen = [140,  360,  7.0]
        if level == 6:  self.damage, self.max_damage, self.hydrogen = [160,  400, 10.0]
        if level == 7:  self.damage, self.max_damage, self.hydrogen = [180,  500, 13.0]
        if level == 8:  self.damage, self.max_damage, self.hydrogen = [200,  600, 16.0]
        if level == 9:  self.damage, self.max_damage, self.hydrogen = [225,  700, 20.0]
        if level == 10: self.damage, self.max_damage, self.hydrogen = [250,  800, 24.0]
        if level == 11: self.damage, self.max_damage, self.hydrogen = [275,  900, 25.0]
        if level == 12: self.damage, self.max_damage, self.hydrogen = [300, 1000, 26.0]

    def damage_applied(self, time, **kwargs):
        return self.damage * time + 0.5 * time * time * (self.max_damage - self.damage) / 45.0 + max(0.0, time - 45.0) * self.max_damage


class mass_battery(weapon_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)

    def _set_level(self, level):
        if level == 1:  self.damage, self.max_targets, self.hydrogen = [ 60, 3,  2.0]
        if level == 2:  self.damage, self.max_targets, self.hydrogen = [ 75, 3,  5.0]
        if level == 3:  self.damage, self.max_targets, self.hydrogen = [ 90, 3,  8.0]
        if level == 4:  self.damage, self.max_targets, self.hydrogen = [110, 3, 11.0]
        if level == 5:  self.damage, self.max_targets, self.hydrogen = [120, 4, 14.0]
        if level == 6:  self.damage, self.max_targets, self.hydrogen = [140, 4, 17.0]
        if level == 7:  self.damage, self.max_targets, self.hydrogen = [160, 4, 20.0]
        if level == 8:  self.damage, self.max_targets, self.hydrogen = [180, 5, 23.0]
        if level == 9:  self.damage, self.max_targets, self.hydrogen = [210, 5, 26.0]
        if level == 10: self.damage, self.max_targets, self.hydrogen = [240, 5, 29.0]
        if level == 11: self.damage, self.max_targets, self.hydrogen = [270, 6, 32.0]
        if level == 12: self.damage, self.max_targets, self.hydrogen = [300, 6, 35.0]
        self.max_damage = self.damage

    def damage_applied(self, time, **kwargs):
        return self.damage * time 


class dual_laser(weapon_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)

    def _set_level(self, level):
        self.max_targets = 2
        if level == 1:  self.damage, self.max_damage, self.hydrogen = [ 80, 250,  2.0]
        if level == 2:  self.damage, self.max_damage, self.hydrogen = [ 90, 300,  5.0]
        if level == 3:  self.damage, self.max_damage, self.hydrogen = [100, 350,  8.0]
        if level == 4:  self.damage, self.max_damage, self.hydrogen = [110, 400, 11.0]
        if level == 5:  self.damage, self.max_damage, self.hydrogen = [120, 450, 14.0]
        if level == 6:  self.damage, self.max_damage, self.hydrogen = [130, 500, 17.0]
        if level == 7:  self.damage, self.max_damage, self.hydrogen = [140, 550, 20.0]
        if level == 8:  self.damage, self.max_damage, self.hydrogen = [160, 600, 23.0]
        if level == 9:  self.damage, self.max_damage, self.hydrogen = [180, 650, 26.0]
        if level == 10: self.damage, self.max_damage, self.hydrogen = [200, 700, 29.0]
        if level == 11: self.damage, self.max_damage, self.hydrogen = [220, 750, 32.0]
        if level == 12: self.damage, self.max_damage, self.hydrogen = [240, 800, 35.0]

    def damage_applied(self, time, **kwargs):
        if kwargs.get('number_of_targets', 1) == 1:
            return self.damage * time
        return self.damage * time + 0.5 * time * time * (self.max_damage - self.damage) / 45.0 + max(0.0, time - 45.0) * self.max_damage


class barrage(weapon_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)

    def _set_level(self, level):
        self.max_targets = 1
        if level == 1:  self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [ 80,  60, 1040,  4.0]
        if level == 2:  self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [ 90,  65, 1130,  8.0]
        if level == 3:  self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [100,  70, 1220, 12.0]
        if level == 4:  self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [110,  80, 1390, 16.0]
        if level == 5:  self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [120,  90, 1560, 20.0]
        if level == 6:  self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [135, 100, 1735, 24.0]
        if level == 7:  self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [150, 110, 1910, 28.0]
        if level == 8:  self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [170, 120, 2090, 32.0]
        if level == 9:  self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [185, 130, 2265, 36.0]
        if level == 10: self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [200, 140, 2440, 40.0]
        if level == 11: self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [220, 150, 2620, 44.0]
        if level == 12: self.damage, self.dmg_per_enemy, self.max_damage, self.hydrogen = [240, 160, 2800, 48.0]

    def damage_applied(self, time, **kwargs):
        return (self.damage + self.dmg_per_enemy * kwargs.get('enemies_in_sector', 0)) * time


class dart_launcher(weapon_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)

    def _set_level(self, level):
        self.max_targets = 1
        if level == 1:  self.damage, self.hydrogen = [ 4100, 24.0]
        if level == 2:  self.damage, self.hydrogen = [ 4500, 28.0]
        if level == 3:  self.damage, self.hydrogen = [ 4900, 32.0]
        if level == 4:  self.damage, self.hydrogen = [ 5300, 36.0]
        if level == 5:  self.damage, self.hydrogen = [ 5700, 40.0]
        if level == 6:  self.damage, self.hydrogen = [ 6100, 44.0]
        if level == 7:  self.damage, self.hydrogen = [ 6500, 48.0]
        if level == 8:  self.damage, self.hydrogen = [ 7000, 52.0]
        if level == 9:  self.damage, self.hydrogen = [ 7500, 56.0]
        if level == 10: self.damage, self.hydrogen = [ 8000, 60.0]
        if level == 11: self.damage, self.hydrogen = [ 9000, 64.0]
        if level == 12: self.damage, self.hydrogen = [10000, 68.0]
        self.max_damage = self.damage

    def damage_applied(self, time, **kwargs):
        return self.damage * (time // 10.0)


class guardian_battery(weapon_module):
    def __init__(self):
        self.level = 1
        self.damage = self.max_damage = 60
        self.max_targets = 1

    def damage_applied(self, time, **kwargs):
        return self.damage * time 


class colossus_laser(weapon_module):
    def __init__(self):
        self.level = 1
        self.damage = 110
        self.max_damage = 270
        self.max_targets = 1

    def damage_applied(self, time, **kwargs):
        return self.damage * time + 0.5 * time * time * (self.max_damage - self.damage) / 45.0 + max(0.0, time - 45.0) * self.max_damage


class ghost_battery(weapon_module):
    def __init__(self):
        self.level = 1
        self.damage = self.max_damage = 140
        self.max_targets = 1

    def damage_applied(self, time, **kwargs):
        return self.damage * time 


class weak_cerberus_base_battery(weapon_module):
    def __init__(self):
        self.level = 1
        self.damage = self.max_damage = 100
        self.max_targets = 1

    def damage_applied(self, time, **kwargs):
        return self.damage * time 


class cerberus_base_battery(weapon_module):
    def __init__(self):
        self.level = 1
        self.damage = self.max_damage = 140
        self.max_targets = 1

    def damage_applied(self, time, **kwargs):
        return self.damage * time 


class strong_cerberus_base_battery(weapon_module):
    def __init__(self):
        self.level = 1
        self.damage = self.max_damage = 200
        self.max_targets = 1

    def damage_applied(self, time, **kwargs):
        return self.damage * time 


class dart_barrage(weapon_module):
    def __init__(self):
        self.level = 1
        self.damage = self.max_damage = 200
        self.max_targets = 1

    def damage_applied(self, time, **kwargs):
        return self.damage * time 
