class damage:
    def __init__(self, x):
        self.amount = x


class direct_damage(damage):
    def __init__(self, x):
        super().__init__(x)


class blast_damage(damage):
    def __init__(self, x):
        super().__init__(x)
