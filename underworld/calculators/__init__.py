from underworld.event_manager.event_manager import global_event_manager
import underworld.utils


def simulate_battle(battle_sector, team1, team2):
    time = 0.0
    dt = 0.2

    for u in team1:
        u.team = team1

    for u in team2:
        u.team = team2

    def remove_unit(payload):
        if payload.get('unit', None) in team1:
            team1.remove(payload['unit'])
        if payload.get('unit', None) in team2:
            team2.remove(payload['unit'])

    global_event_manager.register('sector_death', remove_unit)

    while team1 and team2:
        for u in team1:
            for ou, tid in zip(team2, range(u.weapon_slot.max_targets)):
                u.target(ou)
        for u in team2:
            for ou, tid in zip(team1, range(u.weapon_slot.max_targets)):
                u.target(ou)

        all_units = team1 + team2

        for u in all_units:
            u.update(dt)

        for u in all_units:
            u.apply_damage()

        time += dt

    print('remaining ships:')
    print('ship         hull         shield')
    if team1:
        for u in team1:
            print(f'{u.name:10}   {u.hull:<10.0f}   {u.shield:<10.0f}')

    if team2:
        for u in team2:
            print(f'{u.name:10}   {u.hull:<10.0f}   {u.shield:<10.0f}')
