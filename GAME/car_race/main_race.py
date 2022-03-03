import pygame
from pygame import mixer
import colorspy as colors
import random
import os
import gradient
import particles

# import animator

pygame.init()

# Basic Variables
path = os.getcwd()
score_time = 100
GAME_NAME = "Car Dash"

# Fonts
FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.Font(f'{path}/car_race/font/PixelPowerline-11Mg.ttf', 80)

# Events
ADD_RACER = pygame.USEREVENT
UPDATE_FRAME = pygame.USEREVENT + 3
pygame.time.set_timer(ADD_RACER, 1000)
pygame.time.set_timer(UPDATE_FRAME, 80)

class Player:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y - 50
        self.img = pygame.transform.scale(pygame.image.load(f'{path}/car_race/car_imgs/tile000.png'), (w, h))
        self.rect = pygame.Rect(x, y - 50, w, h)
        self.color = color
        self.health = 3
        self.braking = False
        self.particles = []

    def draw(self):
        win.blit(self.img, self.rect)

        self.particles.append(particles.Particle(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height + 10,
                                                 [random.randrange(-60, 60) / 100, 1.5],
                                                 colors=[colors.light_gray, colors.gray]))

        if not game_paused:
            for particle in self.particles:
                particle.render(win)
                if particle.size <= 0:
                    self.particles.remove(particle)

        self.play_horn()

    # pygame.draw.rect(win, self.color, self.rect)

    def move(self, move, vel):
        if move == 'right':
            self.update_position((vel, 0))
        elif move == 'left':
            self.update_position((-vel, 0))
        elif move == 'down':
            self.braking = True
            change_velocity(6, 4, 5)
        elif move is None:
            self.braking = False

    def get_collisions(self):
        collisions = []
        for racer in racer_list:
            if self.rect.colliderect(racer.rect):
                collisions.append(racer)
        return collisions

    def update_position(self, movement):
        self.rect.x += movement[0]
        collisions = self.get_collisions()

        for racer in collisions:
            if movement[0] > 0:
                self.rect.right = racer.rect.left + 5
            if movement[0] < 0:
                self.rect.left = racer.rect.right - 5

    def play_horn(self):
        if probability(1, 200):
            HORN_SOUND.play()

class Road:
    def __init__(self, x, y, w, h, color):
        self.rect1 = pygame.Rect(x, y, w, h)
        self.rect2 = pygame.Rect(x, y - HEIGHT, w, h)
        self.color = color
        self.vel = 8

    def draw(self):
        win.blit(ROAD_IMG, self.rect1)  # self.road1 = pygame.draw.rect(win, self.color, self.rect1)
        win.blit(ROAD_IMG, self.rect2)  # self.road2 = pygame.draw.rect(win, self.color, self.rect2)
        pygame.draw.rect(win, colors.white, (WIDTH / 2 - 20, self.rect1.y + HEIGHT // 2, 40, 100))
        pygame.draw.rect(win, colors.white, (WIDTH / 2 - 20, self.rect1.y + HEIGHT, 40, 100))
        pygame.draw.rect(win, colors.white, (WIDTH / 2 - 20, self.rect2.y + HEIGHT // 2, 40, 100))
        pygame.draw.rect(win, colors.white, (WIDTH / 2 - 20, self.rect2.y + HEIGHT, 40, 100))

    def move(self):
        self.rect1.y += self.vel
        self.rect2.y += self.vel

        if self.rect1.y >= HEIGHT:
            self.rect1.y = -HEIGHT

        if self.rect2.y >= HEIGHT:
            self.rect2.y = -HEIGHT

        if self.on_road():
            self.vel = 6
        else:
            self.vel = 8

    def on_road(self):
        if player.rect.x > self.rect1.x + self.rect1.width or player.rect.x < self.rect1.x:
            return True

        if player.rect.x > self.rect2.x + self.rect2.width or player.rect.x < self.rect2.x:
            return True

        return False

class Racer:
    def __init__(self):
        self.cars_list = [pygame.transform.scale(pygame.image.load(f'{path}/car_race/car_imgs/tile001.png'),
                                                 (player.rect.width, player.rect.height)).convert_alpha(),
                          pygame.transform.scale(pygame.image.load(f'{path}/car_race/car_imgs/tile002.png'),
                                                 (player.rect.width, player.rect.height)).convert_alpha(),
                          pygame.transform.scale(pygame.image.load(f'{path}/car_race/car_imgs/tile003.png'),
                                                 (player.rect.width, player.rect.height)).convert_alpha()]
        # self.flipped_cars_list = []

        # for car in self.cars_list:
        # self.flipped_cars_list.append(pygame.transform.flip(car, False, True).convert_alpha())

        # self.list = random.choice([self.cars_list, self.cars_list])
        self.car = random.choice(self.cars_list)  # self.list
        self.x = random.randint(620, 1200)
        self.y = -110
        self.rect = pygame.Rect(self.x, self.y, player.rect.width, player.rect.height)
        self.vel = 5
        self.collide = False
        self.colliding = False
        self.particles = []

    def draw(self):

        win.blit(self.car, self.rect)

        self.particles.append(particles.Particle(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height + 10,
                                                 [random.randrange(-60, 60) / 100, self.vel + 1],
                                                 colors=[colors.light_gray, colors.gray]))

        if not game_paused:
            for p in self.particles:
                p.render(win)
                if p.size <= 0:
                    self.particles.remove(p)

    # pygame.draw.rect(win, self.color, self.rect)

    def move(self, lis):
        self.rect.y += self.vel

        if self.rect.y >= HEIGHT:
            lis.remove(self)

        self.slow_when_collision()

    def slow_when_collision(self):
        if self.rect.colliderect(player.rect):
            self.colliding = True
            self.vel = 0
        else:
            self.colliding = False
            self.vel = 5

class Button:
    def __init__(self, x, y, w, h, text=None, bg_color=colors.white, fg_color=colors.black, hovered_color=None,
                 text_color=colors.black, text_size=None, font='comicsans', border_size=0, image=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.old_bg_color = bg_color
        self.old_fg_color = fg_color
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.text_color = text_color
        self.font = font
        self.b_size = border_size
        self.img = image

        if text_size is None:
            self.text_font = pygame.font.SysFont(font, round(self.h * 0.50))
        else:
            self.text_font = pygame.font.SysFont(font, text_size)

        if not hovered_color:
            self.hovered_color = self.bg_color
        else:
            self.hovered_color = hovered_color

    def draw(self):
        pygame.draw.rect(win, self.bg_color, self.rect, width=self.b_size)

        if self.mouse_hovered():
            self.bg_color = self.hovered_color

        else:
            self.bg_color = self.old_bg_color

        self.draw_text()

        if not self.img is None:
            self.draw_image()

        if self.b_size > 0:
            self.draw_border()

    def mouse_hovered(self):
        xPos, yPos = pygame.mouse.get_pos()

        if self.x <= xPos <= self.x + self.w and self.y <= yPos <= self.y + self.h:
            return True

        return False

    def draw_text(self):
        text = self.text_font.render(self.text, True, self.text_color)
        win.blit(text, (self.x + (self.w / 2) - text.get_width() / 2, self.y + (self.h / 2) - text.get_height() / 2))

    def draw_image(self):
        img_rect = pygame.Rect(self.x + (self.w / 2) - self.img.get_width() / 2,
                               self.y + (self.h / 2) - self.img.get_height() / 2, self.img.get_width(),
                               self.img.get_height())
        win.blit(self.img, img_rect)

    def draw_border(self):
        pygame.draw.line(win, self.fg_color, (self.x - 2, self.y - 2), (self.x + self.w - 2, self.y - 2), self.b_size)
        pygame.draw.line(win, self.fg_color, (self.x - 2, self.y - 2), (self.x - 2, self.y + self.h - 2), self.b_size)

class GameController:
    def __init__(self):
        pass
    def start(self):
        main()
    def exit_scene(self):
        end_screen()

    def reset(self):
        global coins, score, player, racer_list, coin_list, move, run, menu, end_mode
        coins = 0
        score = 0
        move = None
        player.health = 3
        player.rect.x = player.x
        racer_list.clear()
        coin_list.clear()
        run = False
        menu = False
        end_mode = False


# Screen
WIDTH = 1920
HEIGHT = 1080
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(f'{GAME_NAME} FPS: {round(clock.get_fps(), 1)}')

ICON_IMG = pygame.image.load(f'{path}/car_race/imgs/icon-tyre.png').convert_alpha()
pygame.display.set_icon(ICON_IMG)

# Images
BG_IMG = pygame.transform.scale(pygame.image.load(f'{path}/car_race/imgs/grass.png'), (WIDTH, HEIGHT)).convert_alpha()
ROAD_IMG = pygame.transform.scale(pygame.image.load(f'{path}/car_race/imgs/road2.jpg'), (680, HEIGHT)).convert_alpha()
COIN_IMG = pygame.transform.scale(pygame.image.load(f'{path}/car_race/imgs/coin.png'), (30, 30)).convert_alpha()
HEART_IMG = pygame.transform.scale(pygame.image.load(f'{path}/car_race/imgs/heart.png'), (50, 50)).convert_alpha()

# Game Variables
move = None
score = 0
coins = 0
show_laser = False
game_paused = False

# Sounds
HIT_SOUND = mixer.Sound(f'{path}/car_race/sounds/hit.wav')
HORN_SOUND = mixer.Sound(f'{path}/car_race/sounds/horn.wav')
BG_CAR_SOUND = mixer.Sound(f'{path}/car_race/sounds/car-music-other.mp3')
mixer.music.load(f'{path}/car_race/sounds/music.wav')

# Sprites
race_track = Road(600, 0, 680, HEIGHT, colors.slate_gray)
player = Player(400, 560, 70, 140, colors.red)
racer_list = []
rect1 = pygame.Rect(0, 0, WIDTH, HEIGHT)
rect2 = pygame.Rect(0, rect1.y - HEIGHT, WIDTH, HEIGHT)
coin_list = []

speed_list = []


game = GameController()


def probability(percent=100, chance=100):
    if 0 <= percent <= 100:
        number = random.randint(1, chance)

        if number <= round(percent):  # 40 -> 40
            return True

        return False

    else:
        raise ValueError


def change_velocity(rd_vel, rc_vel, c_vel):
    race_track.vel = rd_vel
    for racer in racer_list:
        racer.vel = rc_vel
    for coin in coin_list:
        coin.vel = c_vel





def draw_lives(lives):
    x = 0
    for i in range(lives):
        win.blit(HEART_IMG, (x, 0))
        x += 65


def draw_text(text, pos=None, color=colors.black):
    rendered_text = FONT.render(text, True, color)
    if not pos:
        win.blit(rendered_text, (WIDTH - rendered_text.get_width(), 0))
    else:
        if pos == 'center':
            win.blit(rendered_text, (WIDTH / 2 - rendered_text.get_width() / 2, 0))
        else:
            win.blit(rendered_text, pos)


def draw_background():
    if not game_paused:
        vel = race_track.vel
        win.blit(BG_IMG, rect1)
        win.blit(BG_IMG, rect2)

        rect1.y += vel
        rect2.y += vel

        if rect1.y >= HEIGHT:
            rect1.y = -HEIGHT

        if rect2.y >= HEIGHT:
            rect2.y = -HEIGHT


def draw():
    global game_paused, event
    draw_background()

    race_track.draw()

    player.draw()

    if not game_paused:
        race_track.move()

    for racer in racer_list:
        racer.draw()

        if not game_paused:
            racer.move(racer_list)


    if game_paused:
        play_btn = Button(WIDTH / 2 - 200 / 2, HEIGHT / 2 - 100 / 2, 200, 100, "Resume Game", colors.yellow_green,
                          hovered_color=colors.yellow, text_size=30)

        play_btn.draw()

        if play_btn.mouse_hovered() and event.type == pygame.MOUSEBUTTONDOWN:
            game_paused = False


    draw_lives(player.health)


def main():
    global score, move, show_laser, game_paused, event
    run = True

    mixer.music.stop()
    BG_CAR_SOUND.play(-1)
    vol = 100

    while run:
        clock.tick(60)
        pygame.display.set_caption(f'{GAME_NAME} FPS: {round(clock.get_fps(), 1)}')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    move = 'right'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    move = 'left'
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    move = 'down'
                if event.key == pygame.K_e:
                    HORN_SOUND.play()
                if event.key == pygame.K_ESCAPE:
                    game_paused = not game_paused
                    continue

            if event.type == pygame.KEYUP:
                move = None

            if event.type == ADD_RACER and not game_paused:
                racer_list.append(Racer())



        draw()

        if not game_paused:
            player.move(move, 6)

        for racer in racer_list:
            if player.rect.colliderect(racer.rect):
                if not racer.collide:
                    racer.collide = True
                    player.health -= 1
                    HIT_SOUND.play()
            else:
                racer.collide = False      


        if player.health == 0:
            run = False
            game.exit_scene()

        pygame.display.update()





def end_screen():
    end_mode = True

    game_over_text = TITLE_FONT.render("Game Over", True, colors.red)


    retry_button = Button((WIDTH / 2 - 100 / 2) - 100, 500, 100, 50, "Retry", hovered_color=colors.off_white)
    exit_button = Button((WIDTH / 2 - 100 / 2) + 100, 500, 100, 50, "Exit", hovered_color=colors.off_white)


    BG_CAR_SOUND.stop()
    mixer.music.play(-1)

    while end_mode:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_mode = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.mouse_hovered():
                    end_mode = False
                if retry_button.mouse_hovered():
                    end_mode = False
                    game.reset()
                    game.start()

        draw_background()

        race_track.draw()
        race_track.move()

        win.blit(game_over_text, (WIDTH / 2 - game_over_text.get_width() / 2, 100))
        # pygame.draw.rect(win, colors.lime, (WIDTH/2 - 600/2, 250, 600, 400))



        retry_button.draw()
        exit_button.draw()

        pygame.display.update()





game.start()

pygame.quit()
