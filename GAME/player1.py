import pygame
import sys
import math
from camera import *
pygame.init()

display = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()
screen = pygame.Surface((1920, 1080))

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.cam_x = 0
        self.cam_y = 0
        self.width = width
        self.height = height
        self.image = pygame.image.load('assets/png2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = pygame.Rect(x, y, width, height)
        

    def move(self, x ,y):
        if x != 0:
            self.move_on(x, 0)
        if y != 0:
            self.move_on(0, y)       

    def move_on(self, x, y):
        self.cam_x -= x * 2
        lp = self.cam_x
        self.cam_y -= y * 2
        pl = self.cam_y
        #self.rect.x += x
        #self.rect.y += y

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if x > 0:
                    self.rect.right = wall.rect.left
                    self.cam_x = lp
                if x < 0:
                    self.rect.left = wall.rect.right
                    self.cam_x = lp
                if y > 0:
                    self.rect.bottom = wall.rect.top
                    self.cam_y = pl
                if y < 0:
                    self.rect.top = wall.rect.bottom
                    self.cam_y = pl


    def rotate(self):
        pos = pygame.mouse.get_pos()
        #self.cursor_rect = pygame.Rect()
        self.dX = pos[0] - self.rect.x + 15
        self.dY = pos[1] - self.rect.y - 15
        angle = (-math.atan2(self.dY, self.dX)) * 180 / 3.14159265
        print(angle)
        self.img = pygame.transform.rotate(self.image, angle)
        self.rect1 = self.img.get_rect(center=(self.rect.x + 15, self.rect.y + 20))


class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 16
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(display, (255, 0, 0), (self.x, self.y), 4)

class Wall:
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 72, 72)

player = Player(1024//2, 768//2, 30, 30)
player_bullet = []
walls = []

level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                        W",
"W         WWWWWW     WWW W",
"W   WWWW       W    W W  W",
"W   W        WWWW        W",
"W WWW  WWWW              W",
"W   W     W W            W",
"W   W     W   WWW       WW",
"W   WWW WWW   W W        W",
"W     W   W   W W        W",
"WWW   W   WWWWW W        W",
"W W      WW              W",
"W W   WWWW   WWW         W",
"W     W        W         W",
"WWWWWWWWWWWWWW  WWWWWWWWWW",
]

x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x,y))
        x += 72
    y += 72
    x=0

image = pygame.image.load('assets/wall.png')
image = pygame.transform.scale(image, (72, 72))
while True:
    pressed_key = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    speed = 6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
        # if pressed_mouse[0]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullet.append(PlayerBullet(player.rect.x + 15, player.rect.y + 15, mouse_x, mouse_y))

    player.rotate()
    if pressed_key[ord ('w')]:
        player.move(0, -6)
    if pressed_key[ord ('s')]:
        player.move(0, 6)
    if pressed_key[ord('a')]:
        player.move(-6, 0)
    if pressed_key[ord('d')]:
        player.move(6, 0)
        # if pressed_key[ord('w')]:
        #     player.y -= speed
        #     for bullet in player_bullet:
        #         bullet.y += speed
        # if pressed_key[ord('s')]:
        #     player.y += speed
        #     for bullet in player_bullet:
        #         bullet.y -= speed
        # if pressed_key[ord('d')]:
        #     player.x += speed
        #     for bullet in player_bullet:
        #         bullet.x -= speed
        # if pressed_key[ord('a')]:
        #     player.x -= speed
        #     for bullet in player_bullet:
        #         bullet.x += speed

    screen.fill((0, 0, 0))

    player.rotate()
    for wall in walls:
        screen.blit(image, wall.rect)
    for bullet in player_bullet:
        bullet.main(screen)
    display.fill((0, 0, 0))
    player.rotate()
    screen.blit(player.img, player.rect1)
    display.blit(screen, (player.cam_x, player.cam_y))
    #display.blit(player.img, player.rect1)
    clock.tick(60)
    pygame.display.update()