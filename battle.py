import player
import menus
import constants

def battle_gui(entity):
    bottom = menus.Button(0, 668, 1024, 100, constants.LIGHT_RED)
    bottom.update(constants.display_surface)

def battle(ally, enemy):
    #do the cool intro here
    ally_speed = 0
    enemy_speed = 0
    ally_party_hp = 1
    enemy_party_hp = 1
    all_entities = ally.party
    all_entities.append(enemy.party)

    for x in range(len(ally.party)):
        ally_speed += ally.party[x].speed
    for x in range(len(enemy.party)):
        enemy_speed += enemy.party[x].speed

        while ally_party_hp > 0 and enemy_party_hp > 0:
            for x in range(len(ally.party)):
                ally_party_hp += ally.party[x].hp
            for x in range(len(enemy.party)):
                enemy_party_hp += enemy.party[x].hp

            if ally_party_hp == 1:
                ally_party_hp = 0
            else:
                ally_party_hp = 1

            if enemy_party_hp == 1:
                enemy_party_hp = 0
            else:
                enemy_party_hp = 1

            if ally_speed >= enemy_speed:
                for x in range(len(ally.party)):
                    battle_gui(ally.party[x])

                for x in range(len(enemy.party)):
                    battle_gui(enemy.party[x])
            else:
                for x in range(len(enemy.party)):
                    battle_gui(enemy.party[x])

                for x in range(len(ally.party)):
                    battle_gui(ally.party[x])