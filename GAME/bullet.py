import math
import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y):
        #pygame.sprite.Sprite.__init__(self)
        #self.x = x
        #self.y = y
        #self.image = pygame.Surface((5, 5))
        #self.image.fill((255, 0, 0))
        #self.rect = self.image.get_rect()
        #self.rect.x = self.x + 24
        #self.rect.y = self.y
        #self.mouse_x = mouse_x
        #self.mouse_y = mouse_y
        #self.speed = 10
        #self.angle = math.atan2(y-mouse_y, x-mouse_x)
        #self.x_vel = math.cos(self.angle) * self.speed
        #self.y_vel = math.sin(self.angle) * self.speed

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.centerx = x
        self.rect.centery = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 4
        self.angle = math.atan2(self.y-mouse_y, self.x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    def update(self):
        self.rect.x -= int(self.x_vel)
        self.rect.y -= int(self.y_vel)

        

