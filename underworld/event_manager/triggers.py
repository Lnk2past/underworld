def hull_percentage(threshold):
    def wrapper(s):
        return s.hull < threshold * s.max_hull
    return wrapper
