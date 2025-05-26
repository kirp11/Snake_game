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
        self.snake = Snake(self.window.start())
        self.food = Food(self.window.start(), self.snake[0].x, self.snake[0].y)

    def control(self):
        self.snake.movie()
        self.food.create()
        self.cross_with_food()

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

    def cross_with_food(self):
        if self.condition_of_cross():
            surface = pygame.display.get_surface()
            chain = Snake(surface, self.coordinate_of_last_chain_x(), self.coordinate_of_last_chain_y(), self.snake[-1].direction)
            self.snake.append(chain)
            self.food = Food(surface, self.snake[0].x, self.snake[0].y)
            self.food.create()

class Generator_window:
    def __init__(self, event):
        self.event = event

    def select(self):
        pass

class Chain:
    def __init__(self, x, y, x_next, y_next, direction):
        self.x = x
        self.y = y
        self.x_next = x_next
        self.y_next = y_next
        self.direction = direction


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.head = Chain(300, 300, None, None, 'right')
        self.body = []
        self.delta_x = 0
        self.delta_y = 0
        self.body.append(self.head)

    def movie(self):
        surface = pygame.display.get_surface()
        surface.fill((0, 0, 0))
        for i in range(len(self.body)):
            pygame.draw.circle(self.screen, (0, 128, 255), (self.body[i].x, self.body[i].y), FAKTOR)


    def handler_direction_head(self):
        self.head.x += self.delta_x
        self.head.y += self.delta_y
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
        self.choose()

    def choose(self):
        if self.head.direction == "right":
            self.delta_x = FAKTOR/2
            self.delta_y = 0
        elif self.head.direction == "left":
            self.delta_y = 0
            self.delta_x = -FAKTOR/2
        elif self.head.direction == "up":
            self.delta_x = 0
            self.delta_y = -FAKTOR/2
        elif self.head.direction == "down":
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




