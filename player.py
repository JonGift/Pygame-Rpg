import constants
import pygame

class Player():
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

        self.health = 100
        self.mana = 20

        self.sprite =

    def set_location(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def move(self, direction):
        if direction == "down":
            self.y_pos += constants.TILE_SIZE
        elif direction == "up":
            self.y_pos -= constants.TILE_SIZE
        elif direction == "left":
            self.x_pos -= constants.TILE_SIZE
        elif direction == "right":
            self.x_pos += constants.TILE_SIZE

    def draw(self):