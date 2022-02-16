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
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, x ,y):
        if x != 0:
            self.move_on(x, 0)
        if y != 0:
            self.move_on(0, y)

    def move_on(self, x, y):
        self.rect.x += x
        self.rect.y +=y

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
        self.rect = pygame.Rect(pos[0], pos[1], 48, 48)

player = Player(640, 384, 16, 16)
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
"WWWWWWWWWWWWWWWWWWWW",
]

x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x,y))
        x += 48
    y += 48
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
                player_bullet.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))
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
    pygame.draw.rect(display, (0, 255, 0), player.rect)
    for wall in walls:
        pygame.draw.rect((display), (255, 255, 255), wall.rect)
    for bullet in player_bullet:
        bullet.main(display)

    clock.tick(60)
    pygame.display.update()