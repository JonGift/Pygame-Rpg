# This is where all menus and info screens will go
import constants
import pygame

def pause():
    paused = True

    while paused:
        print("Paused")
        text_to_screen("Paused")
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

def text_to_screen(text, x="center", y="center", color=constants.BLACK, size="small"):
    if size == "small":
        text_surface = constants.small_font.render(text, True, color)
    elif size == "medium":
        text_surface = constants.medium_font.render(text, True, color)
    elif size == "large":
        text_surface = constants.large_font.render(text, True, color)

    text_rect = text_surface.get_rect()
    text_rect.center = (constants.SCREEN_WIDTH/2), (constants.SCREEN_HEIGHT/2)
    constants.display_surface.blit(text_surface, text_rect)