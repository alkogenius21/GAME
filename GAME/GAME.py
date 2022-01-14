import pygame as pg

pg.init()

disp_width = 1280
disp_height = 720

display = pg.display.set_mode((disp_width, disp_height))
pg.display.set_caption('GAME')

usr_width = 60
usr_height = 100
usr_x = disp_width // 3
usr_y = disp_height - usr_height - 100

def run():
    game = True
    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        display.fill((255, 255, 255))
        pg.draw.rect(display, (247, 240, 22), (usr_x, usr_y, usr_width, usr_height))
        pg.display.update()

run()
