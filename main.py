__author__ = 'Jawnathan'
import constants
import pygame
import sys

fps_clock = pygame.time.Clock()
pygame.init()
display_surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('An rpg')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    pygame.display.update()
    fps_clock.tick(constants.FPS)