# This is where all menus and info screens will go
import constants
import pygame

class Button:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.display = pygame.Surface((width, height))
        self.display.fill(color)
    def update(self, display_surface):
        display_surface.blit(self.display, (self.x, self.y))
        if self.rect.collidepoint(pygame.mouse.get_pos()) == True and pygame.mouse.get_pressed()[0]:
            return True

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
