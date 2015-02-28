import pygame
import sys

import constants
import player
import menus
import dungeons
import camera
import battle

pygame.init()
pygame.display.set_caption('An rpg')
temp = dungeons.generate_dungeon(16,12)
background = pygame.image.load('img/empty_space.png')
state = 0
#testing = menus.Button(0, 0, 600, 100, constants.LIGHT_RED)

done = False

player = player.Player()
while not done:
    constants.display_surface.blit(background, (0,0))
    if state == 0:
        battle.battle_gui('dingo')
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
                elif event.key == pygame.K_p:
                    menus.pause()
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

        temp.update(constants.display_surface)
        player.update()

    if state == 1:
        pass

    constants.clock.tick(constants.FPS)
    pygame.display.update()

pygame.quit()