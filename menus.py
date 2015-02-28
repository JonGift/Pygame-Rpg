# This is where all menus and info screens will go
import constants
import pygame

def pause():
    paused = True

    while paused:
        print("Paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        constants.display_surface.fill(constants.WHITE)
        constants.clock.tick(5)
