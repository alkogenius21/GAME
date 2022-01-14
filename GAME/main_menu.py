import pygame_menu
from main import game
from main import display
import pygame as pg
class Menu:
    def __init__(self):
        self.main_theme = pygame_menu.themes.THEME_DARK.copy()
        self.main_theme.set_background_color_opacity(0.4)
    def start_the_game(self):
        self.start_game = game(0, 0)
        self.start_game.run()

    def settings(self):
        pg.init()
        bg = pg.image.load('assets/1.jpg')

        setting_m = pygame_menu.Menu('Revenge Alpha Build', 1280, 720,
                       theme=self.main_theme)
        setting_m.add.button('Back', self.main_menu)
        
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

    def main_menu(self):
        menu = pygame_menu.Menu('Revenge Alpha Build', 600, 400,
                           theme=self.main_theme)

        menu.add.button('Play', self.start_the_game)
        menu.add.button('Continue', self.start_the_game)
        menu.add.button('Settings', self.settings)
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