from venv import create

import pygame
import random
pygame.init()

FAKTOR = 5

class Window:
    def __init__(self, lenght, high, frase):
        self.lenght = lenght
        self.high = high
        self.frase = frase

    def start(self):
        screen = pygame.display.set_mode((self.lenght, self.high))
        pygame.display.set_caption(self.frase)
        return screen

class Game:
    def __init__(self):
        self.window = Window(500, 600, "Snake game")
        self.snake = Snake(self.window.start())
        self.food = Food(self.window.start(), self.snake.x, self.snake.y)

    def control(self):
        self.snake.movie()
        self.food.create()
        if self.food.food_x <= self.snake.x + FAKTOR and self.food.food_x >= self.snake.x - FAKTOR and self.food.food_y <= self.snake.y + FAKTOR and self.food.food_y >= self.snake.y - FAKTOR:
            self.food.leave()
            self.food = Food(self.window.start(), self.snake.x, self.snake.y)
            self.food.create()



class Generator_window:
    def __init__(self, event):
        self.event = event

    def select(self):
        pass

class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.x = 250
        self.y = 300
        self.delta_x = 0
        self.delta_y = 0


    def movie(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.circle(self.screen, (0, 128, 255), (self.x, self.y), FAKTOR)
        self.x += self.delta_x
        self.y += self.delta_y
        self.handler_press()

    def handler_press(self):
        pressed = pygame.key.get_pressed()
        if  pressed[pygame.K_LEFT]:
            self.delta_y = 0
            self.delta_x = -FAKTOR
        if pressed[pygame.K_RIGHT]:
            self.delta_y = 0
            self.delta_x = FAKTOR
        if pressed[pygame.K_UP]:
            self.delta_x = 0
            self.delta_y = -FAKTOR
        if pressed[pygame.K_DOWN]:
            self.delta_x = 0
            self.delta_y = FAKTOR

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
            self.food_x = random.randint(10,(width_w-10))
            self.food_y = random.randint(10,(height_w-10))
        pygame.draw.circle(self.screen, (0, 0, 128), (self.food_x, self.food_y), FAKTOR)

    def leave(self):
        pass





running = True
game = Game()

while running:
    pygame.time.delay(60)

    game.control()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()




