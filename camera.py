import constants

def camera_movement(direction, entity, map):
    if direction == 0:
        return

    if direction == 1:
        entity.x_pos += (constants.TILE_SIZE/constants.PLAYER_SPEED)
        for i in range(len(map.tile_dictionary)):
            map.tile_dictionary[i].x += (constants.TILE_SIZE/constants.PLAYER_SPEED)

    if direction == 2:
        entity.x_pos -= (constants.TILE_SIZE/constants.PLAYER_SPEED)
        for i in range(len(map.tile_dictionary)):
            map.tile_dictionary[i].x -= (constants.TILE_SIZE/constants.PLAYER_SPEED)

    if direction == 3:
        entity.y_pos += (constants.TILE_SIZE/constants.PLAYER_SPEED)
        for i in range(len(map.tile_dictionary)):
            map.tile_dictionary[i].y += (constants.TILE_SIZE/constants.PLAYER_SPEED)

    if direction == 4:
        entity.y_pos -= (constants.TILE_SIZE/constants.PLAYER_SPEED)
        for i in range(len(map.tile_dictionary)):
            map.tile_dictionary[i].y -= (constants.TILE_SIZE/constants.PLAYER_SPEED)

def camera(entity, map):
    if entity.x_pos < 192:
        return 1

    if entity.x_pos > 768:
        return 2

    if entity.y_pos < 128:
        return 3

    if entity.y_pos > 576:
        return 4

    return 0