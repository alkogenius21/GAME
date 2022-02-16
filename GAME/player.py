import pygame
import random
from size import *
import math

WIDTH = disp_width
HEIGHT = disp_height
walls = []
GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/png2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 100
        self.speedx = 0


    def keyboard(self):

        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -6
        if keystate[pygame.K_d]:
            self.speedx = 6
        if keystate[pygame.K_w]:
            self.speedy = -6
        if keystate[pygame.K_s]:
            self.speedy = 6
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # if self.rect.right > WIDTH:
        #     self.rect.right = WIDTH
        # if self.rect.left < 0:
        #     self.rect.left = 0


        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.rect.right > 0:
                    self.rect.right = wall.rect.left
                if self.rect.left < 0:
                    self.rect.left = wall.rect.right
                if self.speedy > 0:
                    self.rect.bottom = wall.rect.top
                if self.speedy < 0:
                    self.rect.top = wall.rect.bottom


    def rotate(self):

        self.position = pygame.mouse.get_pos()
        self.angle = math.atan2(self.position[1] - (self.rect.bottom + 40), self.position[0] + (self.rect.centerx + 50))
        self.rect = pygame.transform.rotate(self.image, 360 - self.angle * 57.9)

    def update(self):

        self.keyboard()

class Wall:
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 52, 40)
