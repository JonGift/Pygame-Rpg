import pygame
import sys

import constants
import player
import menus
import dungeons
import camera

clock = pygame.time.Clock()
pygame.init()
display_surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('An rpg')
temp = dungeons.generate_dungeon(16,12)
background = pygame.image.load('img/empty_space.png')

done = False

player = player.Player()
while not done:
    display_surface.blit(background, (0,0))

    camera.camera_movement(camera.camera(player, temp), player, temp)

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
                player.stop("left")
            elif event.key == pygame.K_RIGHT:
                player.stop("right")
            elif event.key == pygame.K_UP:
                player.stop("up")
            elif event.key == pygame.K_DOWN:
                player.stop("down")

    temp.update(display_surface)
    player.update()
    clock.tick(constants.FPS)
    pygame.display.update()

pygame.quit()