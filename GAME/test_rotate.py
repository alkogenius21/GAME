import pygame
import math
from pygame.locals import *
  
YELLOW = (255, 255, 0)
  
pygame.init()
  
w, h = 1000, 1000
screen = pygame.display.set_mode((w, h))
  
running = True
angle = 0
scale = 1
  
img_logo = pygame.image.load('assets/png2.png')
img_logo = pygame.transform.scale(img_logo, (90, 90))
img_logo.convert()

center = w//2, h//2
mouse = pygame.mouse.get_pos()

while running:
    for event in pygame.event.get():
  
        if event.type == QUIT:
            running = False
  
        if event.type == MOUSEMOTION:
            mouse = event.pos
            x = mouse[0] - center[0]
            y = mouse[1] - center[1]

            angle = math.degrees(-math.atan2(y, x))
            img = pygame.transform.rotate(img_logo, angle)
            rect = img.get_rect()
            rect.center = center
      
    screen.fill(YELLOW)
    screen.blit(img, rect)
   
    pygame.display.update()
  

pygame.quit()