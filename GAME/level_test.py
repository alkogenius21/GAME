import size as s
from wall import *
from player import Player
texture = 'assets/wall.png'
import pygame
bullet = list()
from bullet import *
level = [
            "WWWWWWWWWWWWWWWWWWWWW",
            "W                   W",
            "W         WWWWWW    W",
            "W   WWWW       W    W",
            "W   W        WWWW   W",
            "W WWW  WWWW         W",
            "W   W     W W       W",
            "W   W     W   WWW W W",
            "W   WWW WWW   W W   W",
            "W     W   W   W W   W",
            "WWW   W   WWWWW W   W",
            "W W      WW         W",
            "W W   WWWW          W",
            "W     W             W",
            "WWWWWWWWWWWWWWW WWWWW",
        ]



class level1:
    def __init__(self):
        self.x = s.disp_width // 4
        self.y = s.disp_height - 1000
        lis.append((self.x, self.y))
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, (52, 52))
        self.player = Player(640, 384, 52, 52)
    def set_up(self):

        for row in level:
            for col in row:
                if col == "W":
                    Wall((self.x, self.y))
                self.x += 52
                lis.append((self.x, self.y))
            self.y += 52
            self.x = s.disp_width // 4
            lis.append((self.x, self.y))
    def update(self, display):
        for wall in walls:
                display.blit(self.image, wall.rect)
                
        self.player.rotate()
        display.blit(self.player.img, self.player.rect1)

    def motion(self):
        self.player.update()
