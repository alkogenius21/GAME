import pygame as pg
from pygame.constants import DOUBLEBUF, FULLSCREEN, OPENGL
import sys
from player import Player
from video import start_video
import size as s
import pygame_menu

flags = pg.FULLSCREEN | pg.DOUBLEBUF
display = pg.display.set_mode((s.disp_width, s.disp_height), flags, vsync = 1)

      
class game:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.usr_width = 60
        self.usr_height = 100
        self.usr_x = s.disp_width // 3
        self.usr_y = s.disp_height - self.usr_height - 100
        self.fps = 60

    def run(self):
        
        pg.init()
        pg.mixer.init()
        pg.mouse.set_visible(True)
        self.clock = pg.time.Clock()
        
        self.bgg = pg.image.load('assets/2.jpg')

        pg.display.set_caption('Revenge alpha')
        pg.mixer.music.load('assets/3.mp3')
        pg.mixer.music.play(5)
        
        self.all_sprites = pg.sprite.Group()
        self.play = Player()
        self.all_sprites.add(self.play)

        self.ev = True
        while self.ev:
            self.clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.ev = False
                    #pg.quit()
                    #sys.exit()
                    main_menu()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.ev = False
                        #pg.quit()
                        #sys.exit()
                        main_menu()

            self.all_sprites.update()

            display.blit(self.bgg, (0, 0))
            pg.draw.rect(display, (247, 240, 22), (self.usr_x, self.usr_y, self.usr_width, self.usr_height))
            self.all_sprites.draw(display)
            pg.display.flip()

if __name__ == '__main__':

    play = start_video('assets/intro.mp4')
    play1 = start_video('assets/video.mp4')

    play.play_vid()
    del play
    #play1.play_vid()
    del play1

    main_theme = pygame_menu.themes.THEME_DARK.copy()
    main_theme.set_background_color_opacity(0.4)
    def start_the_game():
        start_game = game(0, 0)
        start_game.run()

    def settings():
        pg.init()
        bg = pg.image.load('assets/1.jpg')

        setting_m = pygame_menu.Menu('Revenge Alpha Build', 1280, 720,
                       theme=main_theme)
        setting_m.add.button('Back', main_menu)
        
        while True:
            display.blit(bg, (0, 0))
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()

            if setting_m.is_enabled():
                setting_m.update(events)
                setting_m.draw(display)

            pg.display.update()

    def main_menu():
        menu = pygame_menu.Menu('Revenge Alpha Build', 600, 400,
                           theme=main_theme)

        menu.add.button('Play', start_the_game)
        menu.add.button('Continue', start_the_game)
        menu.add.button('Settings', settings)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        pg.mixer.init()
        pg.mixer.music.load('assets/2.mp3')
        pg.mixer.music.play()
        bg = pg.image.load('assets/1.jpg')
        while True:
            display.blit(bg, (0, 0))
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()

            if menu.is_enabled():
                menu.update(events)
                menu.draw(display)

            pg.display.update()

    main_menu()