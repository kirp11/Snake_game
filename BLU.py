from venv import create

import pygame
from pygame_widgets.button import Button
import pygame_widgets

import random
pygame.init()




FAKTOR = 5
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WGREEN = (153,255,153)
YELLOW = (255, 255, 0)
end_image = pygame.image.load('game_over.jpg')

class Window:
    def __init__(self, lenght=None, high=None, frase=None, color=None):
        self.lenght = lenght
        self.high = high
        self.frase = frase
        self.color = color
        self.screen = None

    def view(self):
        self.screen = pygame.display.set_mode((self.lenght, self.high))
        pygame.display.set_caption(self.frase)
        self.screen.fill(self.color)

    def get_frase(self):
        return self.frase

    def set_frase(self, frase):
        self.frase = frase

    def game(self):
        self.lenght = 600
        self.high = 600
        self.frase = "Snake game"
        self.color = WGREEN
        self.view()

    def game_over(self):
        self.lenght = 400
        self.high = 400
        self.frase = "Game over"
        self.color = BLUE
        self.view()
        over_font = pygame.font.SysFont('Verdana', 50)
        text_surface = over_font.render('GAME OVER', False, YELLOW)
        over_font_result = pygame.font.SysFont('Verdana', 25)
        text_surface_result = over_font_result.render("ВАШ РЕЗУЛЬТАТ: ", False, YELLOW)
        over_font_low = pygame.font.SysFont('Verdana', 20)
        text_surface_low = over_font_low.render('НАЧАТЬ ЗАНОВО?', False, GREEN)

        yes_button = Button(self.screen, 260, 320, 120, 50, inactiveColour=YELLOW,
        pressedColour=(0, 255, 0), text="ДА", onClick=lambda: self.set_frase("Snake game"))
        no_button = Button(self.screen, 30, 320, 120, 50, inactiveColour=YELLOW,
        pressedColour=(0, 255, 0), text="НЕТ", onClick=lambda: self.start_menu())
        yes_button.draw()
        no_button.draw()
        self.screen.blit(text_surface, (40, 0))
        self.screen.blit(end_image, (100, 80))
        self.screen.blit(text_surface_result, (80, 220))
        self.screen.blit(text_surface_low, (100, 260))
        events = pygame.event.get()
        pygame_widgets.update(events)
        # pygame.display.update()

        # yes_button.listen(events)
        # no_button.listen(events)


    def menu(self):
        self.lenght = 500
        self.high = 500
        self.frase = "Main menu"
        self.color = WHITE
        self.view()
        over_font = pygame.font.SysFont('Verdana', 30)
        text_surface = over_font.render('Выберите действие', False, GREEN)

        game_button = Button(self.screen, 100, 80, 300, 80, inactiveColour=YELLOW,
        pressedColour=(0, 255, 0), text="НАЧАТЬ ИГРУ", onClick=lambda: self.set_frase("Snake game"))
        record_button = Button(self.screen, 100, 180, 300, 80, inactiveColour=YELLOW,
        pressedColour=(0, 255, 0), text="ТАБЛИЦА РЕКОРДОВ",onClick=None)
        setting_button = Button(self.screen, 100, 280, 300, 80, inactiveColour=YELLOW,
        pressedColour=(0, 255, 0), text="НАСТРОЙКИ",onClick=None)
        exit_button = Button(self.screen, 100, 380, 300, 80, inactiveColour=YELLOW,
        pressedColour=(0, 255, 0), text="НАСТРОЙКИ",onClick=None)
        game_button.draw()
        record_button.draw()
        setting_button.draw()
        exit_button.draw()

        self.screen.blit(text_surface, (100, 20))

        events = pygame.event.get()
        pygame_widgets.update(events)
        # pygame.display.update()

        # yes_button.listen(events)
        # no_button.listen(events)

    def start_menu(self):
        pass

#
# class Pause_window(Window):
#     def __init__(self, lenght, high, frase, color):
#         super().__init__(lenght, high, frase, color)
#
# class Settings_window(Window):
#     def __init__(self, lenght, high, frase, color):
#         super().__init__(lenght, high, frase, color)
#
#
# class Complexity_window(Window):
#     def __init__(self, lenght, high, frase, color):
#         super().__init__(lenght, high, frase, color)
#
# class Themes_window(Window):
#     def __init__(self, lenght, high, frase, color):
#         super().__init__(lenght, high, frase, color)


class Game:
    def __init__(self):

        self.window = Window()
        self.window.menu()
        self.snake = Snake(self.window.screen)
        self.food = Food(self.window.screen, self.snake.body[0].x, self.snake.body[0].y)
        self.barrier = Barrier(self.window.screen)

    def control(self):
        if self.window.frase == "Snake game":
            self.window.game()
            self.barrier.frame()
            self.snake.movie()
            self.food.create()
            self.cross_with_food()
            self.cross_barrier()
        elif self.window.frase == "Game over":
            self.window.game_over()
        elif self.window.frase == "Main menu":
            self.window.menu()

        pygame.display.update()


    def condition_of_cross(self):
        return (abs(self.food.food_x - self.snake.body[0].x) <= 2*FAKTOR and abs(self.food.food_y - self.snake.body[0].y)<= 2*FAKTOR)

    def cross_with_food(self):
        surface = pygame.display.get_surface()
        if self.condition_of_cross():
            self.snake.add_chain()
            self.food = Food(surface, self.snake.head.x, self.snake.head.y)

    def cross_barrier(self):
        if not self.check_crash():
            self.window.set_frase("Game over")

    def check_crash(self):
        return self.barrier.frame().collidepoint(self.snake.head.x, self.snake.head.y)

class Chain:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.head = Chain(300, 300, "right")
        self.body = []
        self.way_head = [[]]
        self.delta_x = 0
        self.delta_y = 0
        self.body.append(self.head)

    def movie(self):
        self.handler_direction_head()
        pygame.draw.circle(self.screen, BLUE, (self.body[0].x, self.body[0].y), FAKTOR*2)
        for i in range(1, len(self.body)):
            self.body[i].x = self.way_head[i*4][0]
            self.body[i].y = self.way_head[i*4][1]

            pygame.draw.circle(self.screen, BLUE, (self.body[i].x, self.body[i].y), FAKTOR*2)


    def handler_direction_head(self):
        self.head.x += self.delta_x
        self.head.y += self.delta_y
        self.way_head.insert(0, [self.head.x, self.head.y])

        self.handler_press()


    def handler_press(self):
        pressed = pygame.key.get_pressed()
        if  pressed[pygame.K_LEFT]:
            self.head.direction = "left"
        elif pressed[pygame.K_RIGHT]:
            self.head.direction = "right"
        elif pressed[pygame.K_UP]:
            self.head.direction = "up"
        elif pressed[pygame.K_DOWN]:
            self.head.direction = "down"
        self.choose_head_direction()

    def choose_head_direction(self):
        if self.head.direction == "right":
            self.delta_x = FAKTOR
            self.delta_y = 0
        elif self.head.direction == "left":
            self.delta_y = 0
            self.delta_x = -FAKTOR
        elif self.head.direction == "up":
            self.delta_x = 0
            self.delta_y = -FAKTOR
        elif self.head.direction == "down":
            self.delta_x = 0
            self.delta_y = FAKTOR

    def add_chain(self):
        chain = Chain(None, None, None)
        self.body.append(chain)

class Food:
    def __init__(self, screen, stop_x, stop_y):
        self.screen = screen
        self.stop_x = stop_x
        self.stop_y = stop_y
        self.food_x = self.stop_x
        self.food_y = self.stop_y

    def create(self):
        surface = pygame.display.get_surface()
        width_w = surface.get_width()
        height_w = surface.get_height()
        while self.food_x == self.stop_x and self.food_y == self.stop_y:
            self.food_x = random.randint(20,(width_w-20))
            self.food_y = random.randint(20,(height_w-20))
        pygame.draw.circle(self.screen, (0, 0, 128), (self.food_x, self.food_y), FAKTOR*2)

class Barrier:
    def __init__(self, screen):
        self.screen = screen

    def frame(self):

        width_w = self.screen.get_width()
        height_w = self.screen.get_height()
        frame = pygame.draw.rect(self.screen, (51,102,0), [0, 0, width_w, height_w], FAKTOR*3)
        return frame

    def field(self):
        pass


running = True
game = Game()

while running:
    pygame.time.delay(60)
    game.control()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()




