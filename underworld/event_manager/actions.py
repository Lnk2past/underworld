from underworld.corporation import all_corporations


def activate_shield(s):
    return s.shield_slot.activate()


def neutralized(s):
    for corporation in all_corporations:
        if corporation is not s.corporation:
            for member in corporation:
                if s.distance_to(member) < 100.0:
                    member.queue_damage(1250.0)

