import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, texture, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, (72, 72))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def set_up(level, x, y, sprite_group, walls_list, texture, trigger, type_obj, all_group):
    if type_obj == 'wall':
        for row in level:
            for col in row:
                if col == trigger:
                    sprite_group.add(Wall(texture, x, y))
                    all_group.add(Wall(texture, x, y))
                    walls_list.append(Wall(texture, x, y))
                x += 72
            y += 72
            x = 72

    if type_obj == 'floor':
         for row in level:
            for col in row:
                if col == trigger:
                    sprite_group.add(Wall(texture, x, y))
                    x += 72
                else:
                    x += 72
            y += 72
            x = 72

