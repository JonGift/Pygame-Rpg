__author__ = 'Jawnathan'
import pygame
import sys

import constants
import tiles
import player

fps_clock = pygame.time.Clock()
pygame.init()
display_surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('An rpg')
temp = pygame.image.load('img/blank_tile.png')
temp = tiles.map(25,20,'temp')

while True:
    temp.update(display_surface)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    pygame.display.update()
    fps_clock.tick(constants.FPS)