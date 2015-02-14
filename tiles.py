import constants

class tile:
    def __init__(self, tile_size, type):

def create_tile(x, y, tile_size = constants.TILE_SIZE, type):


class map:
    def __init__(self, length, width, effect):
        self.length = length
        self.width = width
        self.effect = effect

        for x in range(self.length):
            for i in range(self.width):
                create_tile(x, i)
