from underworld.event_manager.event_manager import global_event_manager
from underworld.modules import *


class shield_module():
    pass


class activated_shield_module(shield_module, activated_module):
    def activate(self):
        if super().activate():
            self.strength = self.max_strength
            return True


class passive_shield_module(shield_module, passive_module):
    pass


class area_shield_module:
    pass


class alpha_shield(activated_shield_module):
    def __init__(self, level=1):
        super().__init__()

    def set_level(self, level):
        if level < 1 or level > 5:
            raise RuntimeError(f'Module {level} needs to be between 1 and 5!')
        self.level = level
        if level ==  1:  self.max_strength, self.hydrogen = [2000.0, 40.0]
        if level ==  2:  self.max_strength, self.hydrogen = [2300.0, 50.0]
        if level ==  3:  self.max_strength, self.hydrogen = [2600.0, 60.0]
        if level ==  4:  self.max_strength, self.hydrogen = [2900.0, 70.0]
        if level ==  5:  self.max_strength, self.hydrogen = [3200.0, 80.0]
        self.strength = 0.0
        self.duration = 300.0
        self.cooldown = 300.0


class delta_shield(activated_shield_module):
    def __init__(self, level=1):
        super().__init__()
        self.set_level(level)


    def set_level(self, level):
        super().set_level(level)
        if level ==  1:  self.max_strength, self.speed_increase, self.hydrogen = [3500.0, 1.06,  150.0]
        if level ==  2:  self.max_strength, self.speed_increase, self.hydrogen = [3800.0, 1.10,  200.0]
        if level ==  3:  self.max_strength, self.speed_increase, self.hydrogen = [4100.0, 1.14,  300.0]
        if level ==  4:  self.max_strength, self.speed_increase, self.hydrogen = [4400.0, 1.18,  500.0]
        if level ==  5:  self.max_strength, self.speed_increase, self.hydrogen = [4700.0, 1.22,  800.0]
        if level ==  6:  self.max_strength, self.speed_increase, self.hydrogen = [5000.0, 1.26, 1200.0]
        if level ==  7:  self.max_strength, self.speed_increase, self.hydrogen = [5300.0, 1.30, 1500.0]
        if level ==  8:  self.max_strength, self.speed_increase, self.hydrogen = [5600.0, 1.33, 2200.0]
        if level ==  9:  self.max_strength, self.speed_increase, self.hydrogen = [5900.0, 1.36, 2600.0]
        if level == 10:  self.max_strength, self.speed_increase, self.hydrogen = [6200.0, 1.40, 3000.0]
        if level == 11:  self.max_strength, self.speed_increase, self.hydrogen = [6500.0, 1.45, 3500.0]
        if level == 12:  self.max_strength, self.speed_increase, self.hydrogen = [6800.0, 1.50, 4000.0]
        self.strength = 0.0
        self.duration = 300.0
        self.cooldown = 300.0


class passive_shield(passive_shield_module):
    def __init__(self, level=1):
        super().__init__()
        self.set_level(level)

    def activate(self): pass

    def set_level(self, level):
        super().set_level(level)
        if level ==  1:  self.max_strength, self.hydrogen = [ 5000.0,   6.0]
        if level ==  2:  self.max_strength, self.hydrogen = [ 6000.0,   8.8]
        if level ==  3:  self.max_strength, self.hydrogen = [ 7000.0,  12.4]
        if level ==  4:  self.max_strength, self.hydrogen = [ 8000.0,  15.4]
        if level ==  5:  self.max_strength, self.hydrogen = [ 9000.0,  19.8]
        if level ==  6:  self.max_strength, self.hydrogen = [10000.0,  28.6]
        if level ==  7:  self.max_strength, self.hydrogen = [11500.0,  37.4]
        if level ==  8:  self.max_strength, self.hydrogen = [13000.0,  46.2]
        if level ==  9:  self.max_strength, self.hydrogen = [14500.0,  55.0]
        if level == 10:  self.max_strength, self.hydrogen = [16000.0,  66.0]
        if level == 11:  self.max_strength, self.hydrogen = [17500.0,  70.0]
        if level == 12:  self.max_strength, self.hydrogen = [19000.0,  74.0]
        self.strength = self.max_strength


class omega_shield(activated_shield_module):
    def __init__(self, level=1):
        super().__init__()
        self.set_level(level)

    def set_level(self, level):
        super().set_level(level)
        if level ==  1:  self.max_strength, self.hydrogen = [ 8000.0,  600.0]
        if level ==  2:  self.max_strength, self.hydrogen = [ 9000.0,  800.0]
        if level ==  3:  self.max_strength, self.hydrogen = [10000.0, 1000.0]
        if level ==  4:  self.max_strength, self.hydrogen = [11000.0, 1250.0]
        if level ==  5:  self.max_strength, self.hydrogen = [12000.0, 1500.0]
        if level ==  6:  self.max_strength, self.hydrogen = [13000.0, 1750.0]
        if level ==  7:  self.max_strength, self.hydrogen = [14000.0, 2000.0]
        if level ==  8:  self.max_strength, self.hydrogen = [15500.0, 2500.0]
        if level ==  9:  self.max_strength, self.hydrogen = [17000.0, 3000.0]
        if level == 10:  self.max_strength, self.hydrogen = [18500.0, 3500.0]
        if level == 11:  self.max_strength, self.hydrogen = [20000.0, 3750.0]
        if level == 12:  self.max_strength, self.hydrogen = [21500.0, 4000.0]
        self.strength = 0.0
        self.duration = 300.0
        self.cooldown = 300.0


class mirror_shield(activated_shield_module):
    def __init__(self, level=1):
        super().__init__()
        self.set_level(level)

    def set_level(self, level):
        super().set_level(level)
        if level ==  1: self.max_strength, self.reflected, self.hydrogen = [ 6500.0, 0.14,  600.0]
        if level ==  2: self.max_strength, self.reflected, self.hydrogen = [ 7000.0, 0.16,  800.0]
        if level ==  3: self.max_strength, self.reflected, self.hydrogen = [ 7500.0, 0.18, 1000.0]
        if level ==  4: self.max_strength, self.reflected, self.hydrogen = [ 8000.0, 0.20, 1250.0]
        if level ==  5: self.max_strength, self.reflected, self.hydrogen = [ 8500.0, 0.22, 1500.0]
        if level ==  6: self.max_strength, self.reflected, self.hydrogen = [ 9000.0, 0.24, 1075.0]
        if level ==  7: self.max_strength, self.reflected, self.hydrogen = [10000.0, 0.26, 2000.0]
        if level ==  8: self.max_strength, self.reflected, self.hydrogen = [11500.0, 0.28, 2500.0]
        if level ==  9: self.max_strength, self.reflected, self.hydrogen = [13000.0, 0.30, 3000.0]
        if level == 10: self.max_strength, self.reflected, self.hydrogen = [14500.0, 0.32, 3500.0]
        if level == 11: self.max_strength, self.reflected, self.hydrogen = [16000.0, 0.34, 3750.0]
        if level == 12: self.max_strength, self.reflected, self.hydrogen = [18000.0, 0.36, 4000.0]
        self.strength = 0.0
        self.duration = 300.0
        self.cooldown = 300.0


class blast_shield(activated_shield_module, area_shield_module):
    def __init__(self, level=1):
        super().__init__()
        self.set_level(level)

    def set_level(self, level):
        super().set_level(level)
        if level ==  1:  self.max_strength, self.hydrogen = [ 15000.0,   500.0]
        if level ==  2:  self.max_strength, self.hydrogen = [ 20000.0,   600.0]
        if level ==  3:  self.max_strength, self.hydrogen = [ 25000.0,   750.0]
        if level ==  4:  self.max_strength, self.hydrogen = [ 33000.0,   900.0]
        if level ==  5:  self.max_strength, self.hydrogen = [ 40000.0,  1200.0]
        if level ==  6:  self.max_strength, self.hydrogen = [ 50000.0,  1350.0]
        if level ==  7:  self.max_strength, self.hydrogen = [ 60000.0,  1650.0]
        if level ==  8:  self.max_strength, self.hydrogen = [ 70000.0,  2000.0]
        if level ==  9:  self.max_strength, self.hydrogen = [ 85000.0,  2500.0]
        if level == 10:  self.max_strength, self.hydrogen = [100000.0,  3000.0]
        if level == 11:  self.max_strength, self.hydrogen = [120000.0,  3500.0]
        if level == 12:  self.max_strength, self.hydrogen = [140000.0,  4000.0]
        self.strength = 0.0
        self.duration = 300.0
        self.cooldown = 300.0
        self.range = 140.0


class area_shield(activated_shield_module, area_shield_module):
    def __init__(self, level=1):
        super().__init__()
        self.set_level(level)

    def set_level(self, level):
        super().set_level(level)
        if level ==  1:  self.max_strength, self.hydrogen = [ 7000.0,  1000.0]
        if level ==  2:  self.max_strength, self.hydrogen = [ 7500.0,  1250.0]
        if level ==  3:  self.max_strength, self.hydrogen = [ 8000.0,  1500.0]
        if level ==  4:  self.max_strength, self.hydrogen = [ 8500.0,  2000.0]
        if level ==  5:  self.max_strength, self.hydrogen = [ 9000.0,  2500.0]
        if level ==  6:  self.max_strength, self.hydrogen = [ 9500.0,  3000.0]
        if level ==  7:  self.max_strength, self.hydrogen = [10000.0,  3500.0]
        if level ==  8:  self.max_strength, self.hydrogen = [11000.0,  4000.0]
        if level ==  9:  self.max_strength, self.hydrogen = [12000.0,  4500.0]
        if level == 10:  self.max_strength, self.hydrogen = [13000.0,  5000.0]
        if level == 11:  self.max_strength, self.hydrogen = [15000.0,  5500.0]
        if level == 12:  self.max_strength, self.hydrogen = [17000.0,  6000.0]
        self.strength = 0.0
        self.duration = 300.0
        self.cooldown = 300.0
        self.range = 160.0


class phoenix_area_shield(passive_shield_module, area_shield_module):
    def __init__(self):
        self.strength = self.max_strength = 22000.0


class weak_cerberus_base_passive_shield(passive_shield_module):
    def __init__(self):
        self.strength = self.max_strength = 20000.0


class cerberus_base_passive_shield(passive_shield_module):
    def __init__(self):
        self.strength = self.max_strength = 50000.0


class strong_cerberus_base_passive_shield(passive_shield_module):
    def __init__(self):
        self.strength = self.max_strength = 90000.0
