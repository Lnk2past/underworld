from underworld.event_manager.event_manager import global_event_manager


def simulate_battle(battle_sector, corporation_1, corporation_2):
    time = 0.0
    dt = 0.2

    for u in corporation_1:
        u.corporation = corporation_1

    for u in corporation_2:
        u.corporation = corporation_2

    while corporation_1.members and corporation_2.members:
        for u in corporation_1:
            if u.weapon_slot is not None:
                for ou, tid in zip(corporation_2, range(u.weapon_slot.max_targets)):
                    u.target(ou)
        for u in corporation_2:
            if u.weapon_slot is not None:
                for ou, tid in zip(corporation_1, range(u.weapon_slot.max_targets)):
                    u.target(ou)

        all_units = corporation_1.members + corporation_2.members

        for u in all_units:
            u.update(dt)

        for u in all_units:
            u.apply_damage()

        for u in all_units:
            u.finalize()

        time += dt

    print('remaining ships:')
    print('ship         hull         shield')
    if corporation_1:
        for u in corporation_1:
            print(f'{u.name:10}   {u.hull:<10.0f}   {u.shield:<10.0f}')

    if corporation_2:
        for u in corporation_2:
            print(f'{u.name:10}   {u.hull:<10.0f}   {u.shield:<10.0f}')
