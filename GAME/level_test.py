import size as s
from wall import *
from camera import *
from player import Player
texture = 'assets/wall.png'
floor = []
import pygame
from video import start_video
from player import player_bullet



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
        self.x = 0
        self.y = 0
        self.x1 = self.y1 = 0
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.wall = pygame.image.load('assets/floor.png')
        self.wall = pygame.transform.scale(self.wall, (110, 110))
        self.player = Player(120, 120, 35, 35)
        self.story  = start_video('assets/intro.mp4')
        self.num = 0
        total_level_width = len(level[0])*110
        total_level_height = len(level)*110
        self.camera = Camera(camera_func, total_level_width, total_level_height)

    def set_up(self):
        for row in level:
            for col in row:
                if col == "W":
                    walls1.add(Wall('assets/wall.png', self.x, self.y))
                    walls.append(Wall('assets/wall.png', self.x, self.y))
                self.x += 110
            self.y += 110
            self.x = 0
        for row1 in level:
            for col1 in row1:
                if col1 == ' ':
                    walls1.add(Wall('assets/floor.png', self.x1, self.y1))
                    self.x1 += 110
                else:
                    self.x1 += 110
            self.y1 += 110
            self.x1 = 0
    def update(self, display):
        self.camera.update(self.player)
        for e in walls1:
            display.blit(e.image, self.camera.apply(e))
            #walls.append(self.camera.apply(e))


        #self.walls1.draw(display)
        for bullet in player_bullet:
                bullet.main(display)
        display.blit(self.player.img, self.player.rect1)
                

    def motion(self):

        self.player.update()
