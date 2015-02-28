"""
Global constants
"""
import pygame

# Sets clock function
clock = pygame.time.Clock()

# Colors
BLACK    = (   0,   0,   0) 
WHITE    = ( 255, 255, 255) 
BLUE     = (   0,   0, 255)

WHITE = (255,255,255)
BLACK = (0,0,0)

GREY = (200,200,200)

RED = (200,0,0)
LIGHT_RED = (255,0,0)

BLUE = (0,0,255)

YELLOW = (200,200,0)
LIGHT_YELLOW = (255,255,0)

GREEN = (0,155,0)
LIGHT_GREEN = (0,255,0)

# Screen dimensions
SCREEN_WIDTH  = 1024
SCREEN_HEIGHT = 768

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Tile size
TILE_SIZE = 64

FPS = 60

#The lower the number the faster the player will move
PLAYER_SPEED = 8