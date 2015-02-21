import pygame
import constants

class tile:
    #Create an individual tile. Also convert texture number to texture name for easy access.
    def __init__(self, type, tile_size):
        self.type = type
        self.new_type = 'No new type.'
        self.tile_size = tile_size
        self.x = 0
        self.y = 0
        self.reference_name = 0
        self.solid = False
        if self.type == 0:
            self.type = 'blank_tile'
        if self.type == 1:
            self.type = 'grass'
        if self.type == 2:
            self.type = 'wall_stone'
            self.solid = True

def create_tile(pos_x, pos_y, type, reference_number, tile_size = constants.TILE_SIZE):
    #Create a tile with all of the needed params. Used best with class map.
    new_tile = tile(type, tile_size)
    new_tile.type = pygame.image.load('img/' + new_tile.type + '.png')
    new_tile.x = pos_x * 64
    new_tile.y = pos_y * 64
    reference_list = []
    reference_list.append(str(str(pos_x) + ',' + str(pos_y)))
    new_tile.reference_name = reference_number
    new_tile.xy_name = reference_list[0]

    return new_tile

class map:
    #Create a large area of tiles. You can update the tiles individually using either their number, or their xy value.
    #Example one: self.tile_dictionary[17] will pick the 17th block.
    #Example two: self.tile_dictionary_xy['5,5'] will pick the block at 5,5.
    def __init__(self, length, width, effect):
        self.length = length
        self.width = width
        self.effect = effect
        self.tile_dictionary = {}
        self.tile_dictionary_xy = {}
        self.counter = 0

        for x in range(self.length):
            for i in range(self.width):
                self.temp = create_tile(x, i, 0, self.counter)
                self.tile_dictionary[self.temp.reference_name] = create_tile(x, i, 0, self.counter)
                self.tile_dictionary_xy[self.temp.xy_name] = self.tile_dictionary[self.temp.reference_name]
                self.counter += 1

    def update(self, display_surface):
        #Update tiles here!
        for i in range(len(self.tile_dictionary)):
            display_surface.blit(self.tile_dictionary[i].type, (self.tile_dictionary[i].x, self.tile_dictionary[i].y))

    def update_tile(self, number):
        self.tile_dictionary[number].type = pygame.image.load('img/' + self.tile_dictionary[number].new_type + '.png')

    #Update the original dict through the use of the xy dict.
    def update_tile_xy(self, xy):
        self.tile_dictionary[self.tile_dictionary_xy[xy].reference_name].type = pygame.image.load('img/' + self.tile_dictionary[self.tile_dictionary_xy[xy].reference_name].new_type + '.png')


