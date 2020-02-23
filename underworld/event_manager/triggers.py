def hull_percentage(threshold, other=None):
    def wrapper(s):
        if other:
            return other.hull < threshold * other.max_hull
        return s.hull < threshold * s.max_hull
    return wrapper
