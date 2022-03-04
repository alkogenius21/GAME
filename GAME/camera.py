import pygame
from pygame import display

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.floor = pygame.image.load('assets/floor.jpg')
        self.floor = pygame.transform.scale(self.floor, (1920 * 2.15, 1080 * 4.05))
        self.fl_rect = self.floor.get_rect(topleft = (0, 0))

    def center_target_camera(self, target):
        self.offset.x = target.rect1.x - self.half_w
        self.offset.y = target.rect1.y - self.half_h

    def custom_draw(self, player):
        player.rotate()
        self.center_target_camera(player)
        floor_offset = self.fl_rect.topleft - self.offset
        self.display_surface.blit(self.floor, floor_offset)
        #self.display_surface.blit(player.image, player.rect)
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)