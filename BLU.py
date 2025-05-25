from venv import create

import pygame
import random
pygame.init()

FAKTOR = 10

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
        self.window = Window(600, 600, "Snake game")
        self.snake = []
        self.snake.append(Snake(self.window.start(), 300, 300, "right"))
        self.food = Food(self.window.start(), self.snake[0].x, self.snake[0].y)

    def control(self):
        surface = pygame.display.get_surface()
        surface.fill((0, 0, 0))
        for i in range(len(self.snake)):
            self.snake[i].movie()

        self.food.create()

        if self.condition_of_cross():
            surface = pygame.display.get_surface()
            chain = Snake(surface, self.coordinate_of_last_chain_x(), self.coordinate_of_last_chain_y(), self.snake[-1].direction)
            self.snake.append(chain)
            self.food = Food(surface, self.snake[0].x, self.snake[0].y)
            self.food.create()

    def coordinate_of_last_chain_x(self):
        if self.snake[-1].direction == "right":
            return self.snake[-1].x-FAKTOR
        elif self.snake[-1].direction == "left":
            return self.snake[-1].x+FAKTOR
        elif self.snake[-1].direction == "down":
            return self.snake[-1].x
        else:
            return self.snake[-1].x
    def coordinate_of_last_chain_y(self):
        if self.snake[-1].direction == "right":
            return self.snake[-1].y
        elif self.snake[-1].direction == "left":
            return self.snake[-1].y
        elif self.snake[-1].direction == "down":
            return self.snake[-1].y - FAKTOR
        else:
            return self.snake[-1].y + FAKTOR


    def condition_of_cross(self):
        return (abs(self.food.food_x - self.snake[0].x) <= FAKTOR and abs(self.food.food_y - self.snake[0].y)<= FAKTOR)

class Generator_window:
    def __init__(self, event):
        self.event = event

    def select(self):
        pass

class Snake:
    def __init__(self, screen, x, y, direction):
        self.screen = screen
        self.x = x
        self.y = y
        self.direction = direction


    def movie(self):
        self.choose()
        pygame.draw.circle(self.screen, (0, 128, 255), (self.x, self.y), FAKTOR)
        self.x += self.delta_x
        self.y += self.delta_y
        self.handler_press()

    def handler_press(self):
        pressed = pygame.key.get_pressed()
        if  pressed[pygame.K_LEFT]:
            self.direction = "left"
        if pressed[pygame.K_RIGHT]:
            self.direction = "right"
        if pressed[pygame.K_UP]:
            self.direction = "up"
        if pressed[pygame.K_DOWN]:
            self.direction = "down"
        self.choose()

    def choose(self):
        if self.direction == "right":
            self.delta_x = FAKTOR/2
            self.delta_y = 0
        elif self.direction == "left":
            self.delta_y = 0
            self.delta_x = -FAKTOR/2
        elif self.direction == "up":
            self.delta_x = 0
            self.delta_y = -FAKTOR/2
        elif self.direction == "down":
            self.delta_x = 0
            self.delta_y = FAKTOR/2


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




