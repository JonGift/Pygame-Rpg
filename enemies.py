
class Enemy:
    def __init__(self, level, health, mana, abilities, sprite, sprite_battle):
        self.level = level
        self.health = health
        self.mana = mana
        self.abilities = abilities
        self.sprite = pygame.image.load(sprite)
        self.sprite_battle = pygame.image.load(sprite_battle)

        self.x = 0
        self.y = 0
        self.dead = False

    def update(self, display_surface):
        pass

    def update_battle(self, display_surface):
        if self.hp <= 0:
            self.dead = True
        display_surface.blit(self.sprite_battle, (self.x, self.y))