import pygame as pg
from pygame.constants import DOUBLEBUF, FULLSCREEN, OPENGL
import sys
from video import start_video
from level_test import *
import size as s
import pygame_menu
import threading



# global arguments
main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.4)
flags = pg.FULLSCREEN | pg.DOUBLEBUF
display = pg.display.set_mode((s.disp_width, s.disp_height), flags, vsync = 1)
class Pause:

    def __init__(self):
        self.menu = Menu()

    def Continue(self):
        pg.mixer.music.unpause()
        self.bool = False

    def set_volume(self, a, volume):
        pg.mixer.music.set_volume(volume)

    def back_to_the_pause_menu(self):
        self.bool1 = False

    def settings(self):
        self.p_menu.settings = pygame_menu.Menu('Settings', 350, 350,
                           theme=main_theme)
        self.p_menu.settings.add.selector('Volume :', [('Loudness', 0.8), ('Middle', 0.5), ('Quiet', 0.2)], onchange=self.set_volume)
        self.p_menu.settings.add.button('Back', self.back_to_the_pause_menu)
        
        self.bool1 = True

        while self.bool1:

            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()

            if self.p_menu.settings.is_enabled():
                self.p_menu.settings.update(events)
                self.p_menu.settings.draw(display)

            pg.display.update()

    def pause(self):
        pg.mixer.music.pause()
        self.p_menu = pygame_menu.Menu('Pause', 350, 350,
                           theme=main_theme)

        self.p_menu.add.button('Continue', self.Continue)
        self.p_menu.add.button('Settings', self.settings)
        self.p_menu.add.button('Back to the main menu', self.menu.main_menu)
        self.p_menu.add.button('Quit', pygame_menu.events.EXIT)
        self.bool = True
        while self.bool:

            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()

            if self.p_menu.is_enabled():
                self.p_menu.update(events)
                self.p_menu.draw(display)

            pg.display.update()

class Menu:

    pg.mixer.init()
    pg.mixer.music.load('assets/2.mp3')

    def load_bg(self):
        pass

    def start_the_game(self):
        self.start_game = game(0, 0)
        #self.start_game.run()
        self.p1 = threading.Thread(target=self.start_game.run())
        print(self.p1.is_alive())
        self.p1.start()

        print(self.p1.is_alive())

    def settings(self):
        pg.init()
        self.bg = pg.image.load('assets/1.jpg')
        self.bg = pg.transform.scale(self.bg, s.screensize)

        self.setting_m = pygame_menu.Menu('Revenge Alpha Build', 1280, 720,
                       theme=main_theme)
        self.setting_m.add.button('Back', self.main_menu)
        
        while True:
            display.blit(self.bg, (0, 0))
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()

            if self.setting_m.is_enabled():
                self.setting_m.update(events)
                self.setting_m.draw(display)

            pg.display.update()

    def main_menu(self):
        self.menu = pygame_menu.Menu('Revenge Alpha Build', 600, 400,
                           theme=main_theme)

        self.menu.add.button('Play', self.start_the_game)
        self.menu.add.button('Continue', self.start_the_game)
        self.menu.add.button('Settings', self.settings)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

        pg.mixer.init()
        pg.mixer.music.load('assets/2.mp3')
        pg.mixer.music.play(10)
        bg = pg.image.load('assets/1.jpg')
        bg = pg.transform.scale(bg, s.screensize)


        while True:
            display.blit(bg, (0, 0))
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()

            if self.menu.is_enabled():
                self.menu.update(events)
                self.menu.draw(display)

            pg.display.update()

    def __del__(self):
        print()

      
class game:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.usr_width = 60
        self.usr_height = 100
        self.usr_x = s.disp_width // 3
        self.usr_y = s.disp_height - self.usr_height - 100
        self.fps = 60
        self.pause = Pause()


    def run(self):
        
        pg.init()
        pg.mixer.init()
        pg.mouse.set_visible(True)
        self.clock = pg.time.Clock()
        
        self.bgg = pg.image.load('assets/2.jpg')
        self.bgg = pg.transform.scale(self.bgg, s.screensize)
        self.level = level1()
        self.level.set_up()

        pg.display.set_caption('Revenge alpha')
        pg.mixer.music.load('assets/3.mp3')
        #pg.mixer.music.play(5)
        self.ev = True
        while self.ev:
            self.clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.ev = False
                    #pg.quit()
                    #sys.exit()          
            key = pg.key.get_pressed()
            if key[pg.K_ESCAPE]:
                self.pause.pause()
            display.blit(self.bgg, (0, 0))
            #pg.draw.rect(display, (247, 240, 22), (self.usr_x, self.usr_y, self.usr_width, self.usr_height))
            self.level.motion()
            self.level.update(display)
            pg.display.flip()

if __name__ == '__main__':

    play = start_video('assets/intro.mp4')
    play1 = start_video('assets/video.mp4')

    #play.play_vid()
    del play
    #play1.play_vid()
    del play1

    menu = Menu()
    menu.main_menu()
    del menu