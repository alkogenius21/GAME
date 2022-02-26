import pygame
import random
from size import *
import math
from wall import lis
WIDTH = disp_width
HEIGHT = disp_height

GREEN = (0, 255, 0)

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load('assets/png2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (52, 52))
        self.rect = pygame.Rect(x, y, width, height)
        self.speedx = 1
        self.speedy = 1
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

    def move(self):
        self.keyboard()
        if self.speedx != 0:
            self.move_on(self.speedx, 0)
        if self.speedy != 0:
            self.move_on(0, self.speedy)       

    def move_on(self, speedx, speedy):
        if not (self.rect.x + speedx, self.rect.y) in lis:
            self.rect.x += speedx
            print(self.rect.x, self.rect.y)
        if not (self.rect.x, self.rect.y + speedy) in lis:
            self.rect.y += speedy
            print(self.rect.x, self.rect.y)

        self.rect.x += speedx
        self.rect.y += speedy

    def rotate(self):
        self.pos = pygame.mouse.get_pos()
        self.angle = 720-math.atan2(self.pos[1]-512,self.pos[0]-334) * 180 / math.pi
        self.img = pygame.transform.rotate(self.image, self.angle)
        self.rect1 = self.img.get_rect(center = (self.rect.x + 15, self.rect.y - 15))

    def update(self):

        self.rotate()
        self.move()
        self.rotate()