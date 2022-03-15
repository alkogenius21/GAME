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
floor_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
all_group = pygame.sprite.Group()
all_grou = set()

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
        self.player = Player(250, 250, 30, 30)
        self.story  = start_video('assets/intro.mp4')
        self.num = 0
        self.walls1 = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.all_group = pygame.sprite.Group()
    def set_up(self):
        set_up(level, self.x, self.y, self.walls1, walls_list, texture, 'W', 'wall', all_group)
        self.x = self.y = 72
        set_up(level, self.x, self.y, floor_group, walls_list, texture_floor, ' ', 'floor', all_group)
    def update(self, display):
        pygame.sprite.groupcollide(self.walls1, self.bullet_group, False, True)
        button = pygame.mouse.get_pressed()
        self.player.rotate()
        #walls1.draw(display)
        #floor_group.draw(display)
        #self.player.check_collide(floor)
        #self.motion()
        #for bullet in player_bullet:
                #bullet.main(display)
        display.blit(self.player.image, self.player.rect)
        if button[0]:
            self.player.set_shoot(self.bullet_group, self.all_group)
        self.all_group.add(self.walls1)
        self.all_group.draw(display)
        self.motion()
        all_group.update()
        pygame.sprite.groupcollide(self.walls1, self.bullet_group, False, True)
        self.all_group.update()
        #self.bullet_group.draw(display)
        #self.bullet_group.update()
    def motion(self):

        self.player.update(walls_list)
