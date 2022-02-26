import pygame

walls = list()
lis = []

class Wall:
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 52, 52)
        self.rect.centerx = pos[0]
        self.rect.bottom = pos[1]

