import pygame
import random
from size import *
import math
from bullet import Bullet
import time



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
        self.img = pygame.image.load('assets/png2.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (30, 30))
        self.rect1 = pygame.Rect(x, y, width, height)
        self.speedx = 1
        self.speedy = 1
    def keyboard(self):

        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_a]:
            self.speedx = -4
        if keystate[pygame.K_d]:
            self.speedx = 4
        if keystate[pygame.K_w]:
            self.speedy = -4
        if keystate[pygame.K_s]:
            self.speedy = 4

    def move(self, walls_list):
        self.keyboard()
        if self.speedx != 0:
            self.move_on(self.speedx, 0, walls_list)
        if self.speedy != 0:
            self.move_on(0, self.speedy, walls_list)       

    def move_on(self, speedx, speedy, walls_list):

        self.rect1.x += speedx
        self.rect1.y += speedy

        for wall in walls_list:
            if self.rect1.colliderect(wall):
                if self.speedy < 0:
                    self.rect1.top = wall.rect.bottom
                if self.speedy > 0:
                    self.rect1.bottom = wall.rect.top
                if self.speedx > 0:
                    self.rect1.right = wall.rect.left
                if self.speedx < 0:
                    self.rect1.left = wall.rect.right

    #def check_collide(self, walls_list, bullet_group, wall_group):
    #    pygame.sprite.groupcollide(bullet_group, wall_group, False, True)
    #    for wall in walls_list:
    #        if self.rect1.colliderect(wall):
    #            if self.speedy < 0:
    #                self.rect1.top = wall.rect.bottom
    #            if self.speedy > 0:
    #                self.rect1.bottom = wall.rect.top
    #            if self.speedx > 0:
    #                self.rect1.right = wall.rect.left
    #            if self.speedx < 0:
    #                self.rect1.left = wall.rect.right

        


    def rotate(self):
        self.pos = pygame.mouse.get_pos()
        self.dX = self.pos[0] - self.rect1.x 
        self.dY = self.pos[1] - self.rect1.y
        self.angle = (-math.atan2(self.dY, self.dX)) * 180 / 3.14159265
        self.image = pygame.transform.rotate(self.img, int(self.angle))
        self.rect = self.image.get_rect(center = (self.rect1.x + 15, self.rect1.y + 20))

    def set_shoot(self, bullet_group, all_group):
        self.pos1 = pygame.mouse.get_pos()
        bullet_group.add(Bullet(self.rect.x + 15, self.rect.y + 15, self.pos1[0], self.pos1[1]))
        all_group.add(Bullet(self.rect.x + 15, self.rect.y + 15, self.pos1[0], self.pos1[1]))


    def update(self, walls_list):
        
        self.move(walls_list)
        #self.set_shoot(bullet_group)
        self.move(walls_list)
        self.rotate()
        self.move(walls_list)
        #self.set_shoot(bullet_group)
        self.move(walls_list)
        #self.set_shoot(bullet_group)
        self.move(walls_list)
        self.rotate()
        self.move(walls_list)
        #self.set_shoot(bullet_group)