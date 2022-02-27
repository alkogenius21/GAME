import size as s
from wall import *
from player import Player
texture = 'assets/wall.png'
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
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, (62, 62))
        self.player = Player(640, 384, 35, 35)
        self.story  = start_video('assets/video.mp4')
    def set_up(self):
        for row in level:
            for col in row:
                if col == "W":
                    walls.append(pygame.Rect((self.x, self.y, 62, 62)))
                self.x += 62
            self.y += 62
            self.x = 0
    def update(self, display):
        for wall in walls:
                display.blit(self.image, wall)
        for bullet in player_bullet:
                bullet.main(display)        
        self.player.rotate()
        display.blit(self.player.img, self.player.rect1)
        self.rect = pygame.Rect(940, 100, 200, 200)
        pygame.draw.rect(display, (255, 255, 255), self.rect)
        if self.player.rect.colliderect(self.rect):
            if self.rect.right > 0:
                self.story.play_vid()
                

    def motion(self):

        self.player.update()
