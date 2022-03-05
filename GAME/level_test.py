import size as s
from wall import *
from player import Player
texture = 'assets/wall.png'
texture_floor = 'assets/floor.png'
import pygame
from video import start_video
from player import player_bullet
walls1 = pygame.sprite.Group()
walls_list = []

level = [
            "WWWWWWWWWWWWWWWWWWWWWWWWW",
            "W                       W",
            "W         WWWWWW        W",
            "W   WWWW       W        W",
            "W   W        WWWWWWW    W",
            "W WWW  WWWW        W    W",
            "W   W     W W      W    W",
            "W   W     W   WWW WW    W",
            "W   WWW WWW   W W       W",
            "W     W   W   W W       W",
            "WWW   W   WWWWW W       W",
            "W W      WW             W",
            "WWWWWWWWWWWWWWW WWWWWWWWW",            
        ]



class level1:
    def __init__(self):
        self.x = 72
        self.y = 72
        self.x1 = self.y1 = 72
        self.player = Player(250, 250, 30, 30)
        self.story  = start_video('assets/intro.mp4')
        self.num = 0
    def set_up(self):
        set_up(level, self.x, self.y, walls1, walls_list, texture, 'W', 'wall')
        self.x = self.y = 72
        set_up(level, self.x, self.y, walls1, walls_list, texture_floor, ' ', 'floor')
    def update(self, display):
        self.player.rotate()
        walls1.draw(display)
        #self.player.check_collide(floor)
        #self.motion()
        #for bullet in player_bullet:
                #bullet.main(display)
        display.blit(self.player.image, self.player.rect)
                

    def motion(self):

        self.player.update(walls_list)
