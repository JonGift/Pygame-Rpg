import constants
import pygame

class Player():
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

        self.health = 100
        self.mana = 20

        self.sprite = pygame.Surface([constants.TILE_SIZE, constants.TILE_SIZE])
        self.sprite.fill(constants.BLUE)

        self.rect = self.sprite.get_rect()

        #Lists which way the player is facing: N=0, W=1, S=2, E=3
        self.dir_facing = 0

    def set_location(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def move(self, direction):
        if direction == "down":
            self.y_pos += constants.TILE_SIZE
            self.dir_facing = 2

        elif direction == "up":
            self.y_pos -= constants.TILE_SIZE
            self.dir_facing = 0

        elif direction == "left":
            self.x_pos -= constants.TILE_SIZE
            self.dir_facing = 1

        elif direction == "right":
            self.x_pos += constants.TILE_SIZE
            self.dir_facing = 3

    def draw(self):
        gameDisplay.blit(self.sprite, (self.x_pos, self.y_pos))
        print("I ran")
