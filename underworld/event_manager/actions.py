from underworld.corporation import all_corporations


def activate_shield(s):
    return s.shield_slot.activate()


def neutralized(s):
    for corporation in all_corporations:
        if corporation is not s.corporation:
            for member in corporation:
                if s.distance_to(member) < s.neutralized_range:
                    member.queue_damage(s.neutralized)

