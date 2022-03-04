import pygame
walls1 = pygame.sprite.Group()
walls = list()
lis = []

class Wall(pygame.sprite.Sprite):
    def __init__(self, texture, x, y, group):
        super().__init__(group)
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y