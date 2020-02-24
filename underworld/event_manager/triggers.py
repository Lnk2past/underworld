def death():
    def wrapper(s):
        return s.hull <= 0.0
    return wrapper


def hull_percentage(threshold, other=None):
    def wrapper(s):
        if other is not None:
            return other.hull < threshold * other.max_hull
        return s.hull < threshold * s.max_hull
    return wrapper


def enemy_in_neighboring_sector():
    def wrapper(s):
        return True
    return wrapper

