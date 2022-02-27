import pygame
import random
from size import *
import math
from wall import lis
from bullet import Bullet
WIDTH = disp_width
HEIGHT = disp_height
player_bullet = []
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

        if not (self.rect.x, self.rect.y + speedy) in lis:
            self.rect.y += speedy


        self.rect.x += speedx
        self.rect.y += speedy

    def rotate(self):
        self.pos = pygame.mouse.get_pos()
        self.angle = (180 / math.pi) * -math.atan2(self.pos[1] - self.rect.y, self.pos[0] - self.rect.x)
        self.img = pygame.transform.rotate(self.image, int(self.angle))
        self.rect1 = self.img.get_rect(center = (self.rect.x + 15, self.rect.y - 15))

    def set_shoot(self):
        button = pygame.mouse.get_pressed()
        if button[0]:
            player_bullet.append(Bullet(self.rect.x + 15, self.rect.y - 15, self.pos[0], self.pos[1]))

    def update(self):
        self.set_shoot()
        self.rotate()
        self.set_shoot()
        self.move()
        self.set_shoot()
        self.rotate()
        self.set_shoot()