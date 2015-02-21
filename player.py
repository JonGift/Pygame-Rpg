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
        self.move_delay = 0 # When this is 1 the player is moving
        self.finish_move = 0
        self.move_queue = ""

        self.health = 100
        self.mana = 20

        self.sprite = pygame.Surface([constants.TILE_SIZE, constants.TILE_SIZE])
        self.sprite.fill(constants.BLUE)

        self.rect = self.sprite.get_rect()

        # Lists which way the player is facing: N=0, W=1, S=2, E=3
        self.dir_facing = 0

    def set_location(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def move(self, direction):
        if self.x_vel == 0 and self.y_vel == 0:
            print("ran")
            if direction == "down":
                self.y_vel = -1
                self.x_vel = 0
                self.move_delay = 1

            elif direction == "up":
                self.y_vel = 1
                self.x_vel = 0
                self.move_delay = 1

            elif direction == "left":
                self.x_vel = -1
                self.y_vel = 0
                self.move_delay = 1

            elif direction == "right":
                self.x_vel = 1
                self.y_vel = 0
                self.move_delay = 1

        # This will queue up a move command for when the previous key is released.
        elif self.move_queue == "":
            if direction == "down":
                self.move_queue = "down"

            elif direction == "up":
                self.move_queue = "up"

            elif direction == "left":
                self.move_queue = "left"

            elif direction == "right":
                self.move_queue = "right"
                
    def stop(self):
            self.finish_move = 1
            self.move_delay = 0




    def draw(self):
        display_surface.blit(self.sprite, (self.x_pos, self.y_pos))

    def update(self):
        if self.move_delay == 1 or self.finish_move == 1:
            #move down
            if self.y_vel == -1:
                self.y_pos += (constants.TILE_SIZE/constants.PLAYER_SPEED)
                self.dir_facing = 2

            #move up
            elif self.y_vel == 1:
                self.y_pos -= (constants.TILE_SIZE/constants.PLAYER_SPEED)
                self.dir_facing = 0

            #move left
            elif self.x_vel == -1:
                self.x_pos -= (constants.TILE_SIZE/constants.PLAYER_SPEED)
                self.dir_facing = 1

            #move right
            elif self.x_vel == 1:
                self.x_pos += (constants.TILE_SIZE/constants.PLAYER_SPEED)
                self.dir_facing = 3
            self.wait += 1

        if self.wait >= constants.PLAYER_SPEED:
            self.wait = 0
            if self.finish_move == 1:
                self.finish_move = 0
                self.x_vel = 0
                self.y_vel = 0
                self.wait = 0

                if self.move_queue != "":
                    self.move(self.move_queue)
                    self.move_queue = ""


        self.draw()
