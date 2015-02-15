import constants
import pygame

display_surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

class Player():
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.x_vel = 0
        self.y_vel = 0
        self.wait = 0

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
            self.y_vel = -1
            self.x_vel = 0

        elif direction == "up":
            self.y_vel = 1
            self.x_vel = 0

        elif direction == "left":
            self.x_vel = -1
            self.y_vel = 0

        elif direction == "right":
            self.x_vel = 1
            self.y_vel = 0

        elif direction == "stop":
            self.x_vel = 0
            self.y_vel = 0

    def draw(self):
        display_surface.blit(self.sprite, (self.x_pos, self.y_pos))

    def update(self):
        if self.wait == 0:
            #move down
            if self.y_vel == -1:
                self.y_pos += constants.TILE_SIZE
                self.dir_facing = 2

            #move up
            elif self.y_vel == 1:
                self.y_pos -= constants.TILE_SIZE
                self.dir_facing = 0

            #move left
            elif self.x_vel == -1:
                self.x_pos -= constants.TILE_SIZE
                self.dir_facing = 1

            #move right
            elif self.x_vel == 1:
                self.x_pos += constants.TILE_SIZE
                self.dir_facing = 3
        self.wait += 1

        if self.wait > constants.PLAYER_SPEED:
            self.wait = 0


        self.draw()
