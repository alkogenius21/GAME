import pygame
import sys
import math

pygame.init()

display = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load('assets/png2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = pygame.Rect(x, y, width, height)

        self.rect.centerx = 1024 / 2
        self.rect.bottom = 768 - 100
        center = [1024/2, 768 - 100]
    def move(self, x ,y):
        if x != 0:
            self.move_on(x, 0)
        if y != 0:
            self.move_on(0, y)       

    def move_on(self, x, y):
        self.rect.x += x
        self.rect.y += y

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if x > 0:
                    self.rect.right = wall.rect.left
                if x < 0:
                    self.rect.left = wall.rect.right
                if y > 0:
                    self.rect.bottom = wall.rect.top
                if y < 0:
                    self.rect.top = wall.rect.bottom


    def rotate(self):
        pos = pygame.mouse.get_pos()
        angle = 720-math.atan2(pos[1]-300,pos[0]-400)*180/math.pi
        self.img = pygame.transform.rotate(self.image, angle)
        self.rect1 = self.img.get_rect(center = (self.rect.x + 15, self.rect.y - 15))


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
        self.rect = pygame.Rect(pos[0], pos[1], 90, 90)

player = Player(640, 384, 30, 30)
player_bullet = []
walls = []

level = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W         WWWWWW   W",
"W   WWWW       W   W",
"W   W        WWWW  W",
"W WWW  WWWW        W",
"W   W     W W      W",
"W   W     W   WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W        W   W",
"WWWWWWWWWWWWWW WWWWW",
]

x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x,y))
        x += 90
    y += 90
    x=0
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
                player_bullet.append(PlayerBullet(player.rect.x + 15, player.rect.y - 15, mouse_x, mouse_y))

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

    display.fill((0, 0, 0))

    display.blit(player.img, player.rect1)

    for wall in walls:
        pygame.draw.rect((display), (255, 255, 255), wall.rect)
    for bullet in player_bullet:
        bullet.main(display)

    clock.tick(60)
    pygame.display.update()