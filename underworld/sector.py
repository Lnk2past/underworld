class sector:
    def __init__(self):
        self.units = []

    def enter(self, unit):
        self.units.append(unit)

    def notify_death(self, unit):
        for u in self.units:
            u.notify_death()
        self.units.remove(unit)