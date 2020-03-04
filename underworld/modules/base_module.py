from underworld.event_manager.event_manager import global_event_manager


class base_module:
    def set_level(self, level):
        if level < 1 or level > 12:
            raise RuntimeError(f'Module {level} needs to be between 1 and 12!')
        self.level = level

    def update(self, _): pass
    def register(self, *_): pass
    def activate(self): pass
    def deactivate(self): pass


class passive_module(base_module):
    pass


class activated_module(base_module):
    def __init__(self):
        super().__init__()
        self.time = 0.0
        self.duration = 0.0
        self.activated = False
        self.on_cooldown = False

    def update(self, dt):
        if self.activated and self.time >= self.duration:
            self.deactivate()

        elif self.on_cooldown and self.time >= self.cooldown:
            self.on_cooldown = False
            self.time = 0.0

        else:
            self.time += dt

    def activate(self, *args):
        activate = not self.activated and not self.on_cooldown
        if activate:
            self.time = 0.0
            self.activated = True
        return activate

    def deactivate(self):
        self.activated = False
        self.on_cooldown = True
        self.time = 0.0
