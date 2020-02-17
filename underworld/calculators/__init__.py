import underworld.utils


def time_to_kill(squad, unit, **kwargs):
    f = lambda t: sum(bs.damage_applied(t, **kwargs) for bs in squad) - unit().total_hitpoints
    return underworld.utils.bisection(f, 0.0, 2500.0, 100)
