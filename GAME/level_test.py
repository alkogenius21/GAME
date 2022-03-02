import size as s
from wall import *
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
        self.image = pygame.transform.scale(self.image, (62, 62))
        self.wall = pygame.image.load('assets/floor.png')
        self.wall = pygame.transform.scale(self.wall, (62, 62))
        self.player = Player(640, 384, 35, 35)
        self.story  = start_video('assets/intro.mp4')
        self.num = 0
    def set_up(self):
        for row in level:
            for col in row:
                if col == "W":
                    walls.append(pygame.Rect((self.x, self.y, 62, 62)))
                self.x += 62
            self.y += 62
            self.x = 0
        for row1 in level:
            for col1 in row1:
                if col1 == ' ':
                    floor.append(pygame.Rect((self.x1, self.y1, 62, 62)))
                    self.x1 += 62
                else:
                    self.x1 += 62
            self.y1 += 62
            self.x1 = 0
    def update(self, display):
        for fl in floor:
            display.blit(self.wall, fl)
        for wall in walls:
                display.blit(self.image, wall)
        for bullet in player_bullet:
                bullet.main(display)        
        #self.player.rotate()
        display.blit(self.player.img, self.player.rect1)
        #pygame.draw.rect(display, (255, 255, 255), self.player.rect)
        #display.blit(self.player.image, self.player.rect)
        self.rect = pygame.Rect(940, 100, 200, 200)
        pygame.draw.rect(display, (255, 255, 255), self.rect)
        if self.player.rect.colliderect(self.rect):
            if self.rect.right > 0:
                if self.num != 1:
                    self.story.play_vid()
                    del self.story
                    self.num += 1
                display.fill((0, 0, 0))
                

    def motion(self):

        self.player.update()
