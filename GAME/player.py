import pygame
import random
from size import *
import math


WIDTH = disp_width
HEIGHT = disp_height

GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/png2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 100
        self.speedx = 0

    def keyboard(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        if keystate[pygame.K_w]:
            self.speedy = -8
        if keystate[pygame.K_s]:
            self.speedy = 8
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def rotate(self):
        self.position = pygame.mouse.get_pos()
        self.angle = math.atan2(self.position[1] - (self.rect.bottom + 40), self.position[0] + (self.rect.centerx + 50))
        self.rect = pygame.transform.rotate(self.image, 360 - self.angle * 57.9)

    def update(self):
        self.keyboard()
