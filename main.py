__author__ = 'Jawnathan'
import pygame
import sys

import constants
import tiles
import player
import menus
import dungeons

clock = pygame.time.Clock()
pygame.init()
display_surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('An rpg')
temp = dungeons.generate_dungeon(16,12)

done = False

player = player.Player()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
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

    #if temp.tile_dictionary_xy['0,11'].new_type != 'grass':
    #    temp.tile_dictionary_xy['0,11'].new_type = 'grass'
    #    temp.update_tile_xy('0,11')
    #else:
    #    temp.tile_dictionary_xy['15,11'].new_type = 'blank_tile'
    #    temp.update_tile_xy('15,11')

pygame.quit()