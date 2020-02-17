class sentinel:
    def __init__(self):
        self.hull = 750.0
        self.shield = 0.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class guardian:
    def __init__(self):
        self.hull = 7000.0
        self.shield = 0.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class interceptor:
    def __init__(self):
        self.hull = 8000.0
        self.shield = 0.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class colossus:
    def __init__(self):
        self.hull = 40000.0
        self.shield = 16000.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class destroyer:
    def __init__(self):
        self.hull = 10000.0
        self.shield = 0.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class bomber:
    def __init__(self):
        self.hull = 48000.0
        self.shield = 0.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class phoenix:
    def __init__(self):
        self.hull = 45000.0
        self.shield = 22000.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class storm:
    def __init__(self):
        self.hull = 40000.0
        self.shield = 0.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class ghost:
    def __init__(self):
        self.hull = 200.0
        self.shield = 0.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class weak_cerberus_base:
    def __init__(self):
        self.hull = 20000.0
        self.shield = 20000.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class cerberus_base:
    def __init__(self):
        self.hull = 50000.0
        self.shield = 50000.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield


class strong_cerberus_base:
    def __init__(self):
        self.hull = 90000.0
        self.shield = 90000.0

    @property
    def total_hitpoints(self):
        return self.hull + self.shield
