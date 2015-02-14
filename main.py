__author__ = 'Jawnathan'
import pygame
import sys

import constants
import tiles
import player

clock = pygame.time.Clock()
pygame.init()
display_surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('An rpg')
temp = pygame.image.load('img/blank_tile.png')
temp = tiles.map(25,20,'temp')

done = False

player = player.Player()
while not done:
    temp.update(display_surface)
    player.draw
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(constants.FPS)
    pygame.display.update()

pygame.quit()