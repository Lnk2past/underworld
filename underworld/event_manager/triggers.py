class trigger:
    def __init__(self, condition):
        self.condition = condition
        self.params = {}

    def __call__(self, x):
        return self.condition(x, **self.params)

    def param(self, k, v):
        self.params[k] = v
        return self


death = trigger(lambda ship, **params: ship.hull <= 0.0)


hull_strength = trigger(lambda ship, **params: ship.hull < params['strength'])


hull_percentage = trigger(lambda ship, **params: ship.hull < params['threshold'] * ship.max_hull)


enemy_in_neighboring_sector = trigger(lambda x, **params: True)
