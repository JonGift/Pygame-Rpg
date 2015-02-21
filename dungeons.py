import tiles
import random

def generate_dungeon(length, width):
    dungeon_map = tiles.map(length, width, 'temp')
    length = length - 1
    width = width - 1

    entrance = '0,0'
    side = random.randrange(1, 5)
    if side == 1:
        entrance_location = random.randrange(0, length)
        entrance_location = str(str(entrance_location) + ',0')
    if side == 2:
        entrance_location = random.randrange(0, width)
        entrance_location = str(str(length) + ',' + str(entrance_location))
    if side == 3:
        entrance_location = random.randrange(0, length)
        entrance_location = str(str(entrance_location) + ',' + str(width ))
    if side == 4:
        entrance_location = random.randrange(0, width)
        entrance_location = str('0,' + str(entrance_location))

    dungeon_map.tile_dictionary_xy[entrance_location].new_type = 'grass'
    dungeon_map.update_tile_xy(entrance_location)

    return dungeon_map