__author__ = 'Jawnathan'
import pygame
import sys

import constants
import tiles
import player
import menus

clock = pygame.time.Clock()
pygame.init()
display_surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('An rpg')
temp = pygame.image.load('img/blank_tile.png')
temp = tiles.map(16,12,'temp')

done = False

player = player.Player()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if player.wait == 0:
                if event.key == pygame.K_LEFT:
                    player.move("left")
                elif event.key == pygame.K_RIGHT:
                    player.move("right")
                elif event.key == pygame.K_UP:
                    player.move("up")
                elif event.key == pygame.K_DOWN:
                    player.move("down")
                elif event.key == pygame.K_w:
                    done = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.stop()
            elif event.key == pygame.K_RIGHT:
                player.stop()
            elif event.key == pygame.K_UP:
                player.stop()
            elif event.key == pygame.K_DOWN:
                player.stop()

    temp.update(display_surface)
    player.update()
    clock.tick(constants.FPS)
    pygame.display.update()

pygame.quit()