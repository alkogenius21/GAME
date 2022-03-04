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
            "W                   W",
            "W     WWWWWWWW      W",
            "W     W      W      W",
            "W     W      W      W",
            "W     WWWWW WW      W",
            "W                   W",
            "W                   W",
            "WWWWWWWWWWWWWWW WWWWW",            
        ]



class level1:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x1 = self.y1 = 0
        self.camera_group = Camera()
        self.player = Player(0, 0, 35, 35, self.camera_group)
        self.story  = start_video('assets/intro.mp4')
        self.num = 0

    def set_up(self):
        for row in level:
            for col in row:
                if col == "W":
                    walls1.add(Wall('assets/wall.png', self.x, self.y, self.camera_group))
                    walls.append(Wall('assets/wall.png', self.x, self.y, self.camera_group))
                self.x += 200
            self.y += 200
            self.x = 0
        for row1 in level:
            for col1 in row1:
                if col1 == ' ':
                    #walls1.add(Wall('assets/floor.png', self.x1, self.y1, self.camera_group))
                    self.x1 += 200
                else:
                    self.x1 += 200
            self.y1 += 200
            self.x1 = 0
    def update(self, display):
        #walls1.draw(display)
        self.camera_group.update()
        self.camera_group.custom_draw(self.player)
        for bullet in player_bullet:
                bullet.main(display)
        #display.blit(self.player.img, self.player.rect1)
                

    def motion(self):

        self.player.update()
