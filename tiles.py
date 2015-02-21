import pygame
import constants

class tile:
    def __init__(self, type, tile_size):
        self.type = type
        self.tile_size = tile_size
        self.x = 0
        self.y = 0
        self.reference_name = 0
        if self.type == 0:
            self.type = 'blank_tile'

def create_tile(pos_x, pos_y, type, reference_number, tile_size = constants.TILE_SIZE):
    new_tile = tile(type, tile_size)
    new_tile.type = pygame.image.load('img/' + new_tile.type + '.png')
    new_tile.x = pos_x * 64
    new_tile.y = pos_y * 64
    new_tile.reference_name = reference_number

    return new_tile

class map:
    def __init__(self, length, width, effect):
        self.length = length
        self.width = width
        self.effect = effect
        #tile dict here, need to update tiles.
        self.tile_dictionary = {}
        self.counter = 0

        for x in range(self.length):
            for i in range(self.width):
                self.temp = create_tile(x, i, 0, self.counter)
                self.tile_dictionary[self.temp.reference_name] = create_tile(x, i, 0, self.counter)
                self.counter += 1

    def update(self, display_surface):
        #Update tiles here!
        for i in range(len(self.tile_dictionary)):
            display_surface.blit(self.tile_dictionary[i].type, (self.tile_dictionary[i].x, self.tile_dictionary[i].y))

