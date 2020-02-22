class shield_module:
    def __init__(self, level):
        if level < 1 or level > 12:
            raise RuntimeError(f'Module {level} needs to be between 1 and 12!')

    def activate(self):
        self.strength = self.max_strength


class alpha_shield(shield_module):
    def __init__(self, level=1):
        if level < 1 or level > 5:
            raise RuntimeError(f'Module {level} needs to be between 1 and 5!')
        self.level = level
        self._set_level(level)
        self.activated = True

    def _set_level(self, level):
        if level ==  1:  self.max_strength, self.hydrogen = [2000, 40.0]
        if level ==  2:  self.max_strength, self.hydrogen = [2300, 50.0]
        if level ==  3:  self.max_strength, self.hydrogen = [2600, 60.0]
        if level ==  4:  self.max_strength, self.hydrogen = [2900, 70.0]
        if level ==  5:  self.max_strength, self.hydrogen = [3200, 80.0]
        self.strength = 0
        self.duration = 300
        self.cooldown = 300


class delta_shield(shield_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)
        self.activated = True

    def _set_level(self, level):
        if level ==  1:  self.max_strength, self.speed_increase, self.hydrogen = [3500, 1.06,  150.0]
        if level ==  2:  self.max_strength, self.speed_increase, self.hydrogen = [3800, 1.10,  200.0]
        if level ==  3:  self.max_strength, self.speed_increase, self.hydrogen = [4100, 1.14,  300.0]
        if level ==  4:  self.max_strength, self.speed_increase, self.hydrogen = [4400, 1.18,  500.0]
        if level ==  5:  self.max_strength, self.speed_increase, self.hydrogen = [4700, 1.22,  800.0]
        if level ==  6:  self.max_strength, self.speed_increase, self.hydrogen = [5000, 1.26, 1200.0]
        if level ==  7:  self.max_strength, self.speed_increase, self.hydrogen = [5300, 1.30, 1500.0]
        if level ==  8:  self.max_strength, self.speed_increase, self.hydrogen = [5600, 1.33, 2200.0]
        if level ==  9:  self.max_strength, self.speed_increase, self.hydrogen = [5900, 1.36, 2600.0]
        if level == 10:  self.max_strength, self.speed_increase, self.hydrogen = [6200, 1.40, 3000.0]
        if level == 11:  self.max_strength, self.speed_increase, self.hydrogen = [6500, 1.45, 3500.0]
        if level == 12:  self.max_strength, self.speed_increase, self.hydrogen = [6800, 1.50, 4000.0]
        self.strength = 0
        self.duration = 300
        self.cooldown = 300


class passive_shield(shield_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)
        self.activated = False

    def activate(self): pass

    def _set_level(self, level):
        if level ==  1:  self.max_strength, self.hydrogen = [ 5000,   6.0]
        if level ==  2:  self.max_strength, self.hydrogen = [ 6000,   8.8]
        if level ==  3:  self.max_strength, self.hydrogen = [ 7000,  12.4]
        if level ==  4:  self.max_strength, self.hydrogen = [ 8000,  15.4]
        if level ==  5:  self.max_strength, self.hydrogen = [ 9000,  19.8]
        if level ==  6:  self.max_strength, self.hydrogen = [10000,  28.6]
        if level ==  7:  self.max_strength, self.hydrogen = [11500,  37.4]
        if level ==  8:  self.max_strength, self.hydrogen = [13000,  46.2]
        if level ==  9:  self.max_strength, self.hydrogen = [14500,  55.0]
        if level == 10:  self.max_strength, self.hydrogen = [16000,  66.0]
        if level == 11:  self.max_strength, self.hydrogen = [17500,  70.0]
        if level == 12:  self.max_strength, self.hydrogen = [19000,  74.0]
        self.strength = self.max_strength


class omega_shield(shield_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)
        self.activated = True

    def _set_level(self, level):
        if level ==  1:  self.max_strength, self.hydrogen = [ 8000,  600.0]
        if level ==  2:  self.max_strength, self.hydrogen = [ 9000,  800.0]
        if level ==  3:  self.max_strength, self.hydrogen = [10000, 1000.0]
        if level ==  4:  self.max_strength, self.hydrogen = [11000, 1250.0]
        if level ==  5:  self.max_strength, self.hydrogen = [12000, 1500.0]
        if level ==  6:  self.max_strength, self.hydrogen = [13000, 1750.0]
        if level ==  7:  self.max_strength, self.hydrogen = [14000, 2000.0]
        if level ==  8:  self.max_strength, self.hydrogen = [15500, 2500.0]
        if level ==  9:  self.max_strength, self.hydrogen = [17000, 3000.0]
        if level == 10:  self.max_strength, self.hydrogen = [18500, 3500.0]
        if level == 11:  self.max_strength, self.hydrogen = [20000, 3750.0]
        if level == 12:  self.max_strength, self.hydrogen = [21500, 4000.0]
        self.strength = 0
        self.duration = 300
        self.cooldown = 300


class mirror_shield(shield_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)
        self.activated = True

    def _set_level(self, level):
        if level ==  1: self.max_strength, self.reflected, self.hydrogen = [ 6500, 0.14,  600.0]
        if level ==  2: self.max_strength, self.reflected, self.hydrogen = [ 7000, 0.16,  800.0]
        if level ==  3: self.max_strength, self.reflected, self.hydrogen = [ 7500, 0.18, 1000.0]
        if level ==  4: self.max_strength, self.reflected, self.hydrogen = [ 8000, 0.20, 1250.0]
        if level ==  5: self.max_strength, self.reflected, self.hydrogen = [ 8500, 0.22, 1500.0]
        if level ==  6: self.max_strength, self.reflected, self.hydrogen = [ 9000, 0.24, 1075.0]
        if level ==  7: self.max_strength, self.reflected, self.hydrogen = [10000, 0.26, 2000.0]
        if level ==  8: self.max_strength, self.reflected, self.hydrogen = [11500, 0.28, 2500.0]
        if level ==  9: self.max_strength, self.reflected, self.hydrogen = [13000, 0.30, 3000.0]
        if level == 10: self.max_strength, self.reflected, self.hydrogen = [14500, 0.32, 3500.0]
        if level == 11: self.max_strength, self.reflected, self.hydrogen = [16000, 0.34, 3750.0]
        if level == 12: self.max_strength, self.reflected, self.hydrogen = [18000, 0.36, 4000.0]
        self.strength = 0
        self.duration = 300
        self.cooldown = 300


class blast_shield(shield_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)
        self.activated = True

    def _set_level(self, level):
        if level ==  1:  self.max_strength, self.hydrogen = [ 15000,   500.0]
        if level ==  2:  self.max_strength, self.hydrogen = [ 20000,   600.0]
        if level ==  3:  self.max_strength, self.hydrogen = [ 25000,   750.0]
        if level ==  4:  self.max_strength, self.hydrogen = [ 33000,   900.0]
        if level ==  5:  self.max_strength, self.hydrogen = [ 40000,  1200.0]
        if level ==  6:  self.max_strength, self.hydrogen = [ 50000,  1350.0]
        if level ==  7:  self.max_strength, self.hydrogen = [ 60000,  1650.0]
        if level ==  8:  self.max_strength, self.hydrogen = [ 70000,  2000.0]
        if level ==  9:  self.max_strength, self.hydrogen = [ 85000,  2500.0]
        if level == 10:  self.max_strength, self.hydrogen = [100000,  3000.0]
        if level == 11:  self.max_strength, self.hydrogen = [120000,  3500.0]
        if level == 12:  self.max_strength, self.hydrogen = [140000,  4000.0]
        self.strength = 0
        self.duration = 300
        self.cooldown = 300
        self.range = 140


class area_shield(shield_module):
    def __init__(self, level=1):
        super().__init__(level)
        self.level = level
        self._set_level(level)
        self.activated = True

    def _set_level(self, level):
        if level ==  1:  self.max_strength, self.hydrogen = [ 7000,  1000.0]
        if level ==  2:  self.max_strength, self.hydrogen = [ 7500,  1250.0]
        if level ==  3:  self.max_strength, self.hydrogen = [ 8000,  1500.0]
        if level ==  4:  self.max_strength, self.hydrogen = [ 8500,  2000.0]
        if level ==  5:  self.max_strength, self.hydrogen = [ 9000,  2500.0]
        if level ==  6:  self.max_strength, self.hydrogen = [ 9500,  3000.0]
        if level ==  7:  self.max_strength, self.hydrogen = [10000,  3500.0]
        if level ==  8:  self.max_strength, self.hydrogen = [11000,  4000.0]
        if level ==  9:  self.max_strength, self.hydrogen = [12000,  4500.0]
        if level == 10:  self.max_strength, self.hydrogen = [13000,  5000.0]
        if level == 11:  self.max_strength, self.hydrogen = [15000,  5500.0]
        if level == 12:  self.max_strength, self.hydrogen = [17000,  6000.0]
        self.strength = 0
        self.duration = 300
        self.cooldown = 300
        self.range = 160


class phoenix_area_shield(shield_module):
    def __init__(self):
        self.level = 1
        self.strength = self.max_strength = 22000


class weak_cerberus_base_passive_shield(shield_module):
    def __init__(self):
        self.level = 1
        self.strength = self.max_strength = 20000


class cerberus_base_passive_shield(shield_module):
    def __init__(self):
        self.level = 1
        self.strength = self.max_strength = 50000


class strong_cerberus_base_passive_shield(shield_module):
    def __init__(self):
        self.level = 1
        self.strength = self.max_strength = 90000
