import pygame
walls1 = pygame.sprite.Group()
walls = list()
lis = []

class Wall(pygame.sprite.Sprite):
    def __init__(self, texture, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y