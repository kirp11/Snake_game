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
        self.window = Window(600, 600, "Snake game")
        self.snake = Snake(self.window.start())
        self.food = Food(self.window.start(), self.snake.body[0].x, self.snake.body[0].y)

    def control(self):
        self.snake.movie()
        self.food.create()
        self.cross_with_food()

    def condition_of_cross(self):
        return (abs(self.food.food_x - self.snake.body[0].x) <= 2*FAKTOR and abs(self.food.food_y - self.snake.body[0].y)<= 2*FAKTOR)

    def cross_with_food(self):
        surface = pygame.display.get_surface()
        if self.condition_of_cross():
            self.snake.add_chain()
            self.food = Food(surface, self.snake.head.x, self.snake.head.y)

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
        self.head = Chain(300, 300, None, None, "right")
        self.body = []
        self.delta_x = 0
        self.delta_y = 0
        self.body.append(self.head)

    def movie(self):
        self.screen.fill((0, 0, 0))
        self.handler_direction_head()
        for i in range(len(self.body)):
            if i == 1 :
            #     self.body[i].x = self.body[i - 1].x_next
            #     self.body[i].y = self.body[i - 1].y_next
            # elif i > 1:
            #     chain_delta_x = self.body[i-1].x - self.body[i - 1].x_next
            #     chain_delta_y = self.body[i-1].y - self.body[i - 1].y_next
            #
            #     self.body[i].x = self.body[i-1].x + chain_delta_x
            #     self.body[i].y = self.body[i-1].y + chain_delta_y
            #
            #
            #     self.body[i].x_next = self.body[i].x + chain_delta_x
            #     self.body[i].y_next = self.body[i].y + chain_delta_y

            pygame.draw.circle(self.screen, (0, 128, 255), (self.body[i].x, self.body[i].y), 2*FAKTOR)

            # chain_delta_x= self.delta_x
            # chain_delta_y = self.delta_y



    def handler_direction_head(self):
        self.head.x += self.delta_x
        self.head.y += self.delta_y
        self.head.x_next = self.head.x - 4*self.delta_x
        self.head.y_next = self.head.y - 4*self.delta_y
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

    def choose_chain_direction(self, chain):
        if chain.direction == "right":
            chain.delta_x = FAKTOR
            chain.delta_y = 0
        elif chain.direction == "left":
            chain.delta_y = 0
            chain.delta_x = -FAKTOR
        elif chain.direction == "up":
            chain.delta_x = 0
            chain.delta_y = -FAKTOR
        elif chain.direction == "down":
            chain.delta_x = 0
            chain.delta_y = FAKTOR
        return chain.delta_x, chain.delta_y

    def add_chain(self):
        # if self.head.direction == "right":
        #     x_chain = self.body[-1].x - FAKTOR
        #     y_chain = self.body[-1].y
        # elif self.head.direction == "left":
        #     x_chain = self.body[-1].x + FAKTOR
        #     y_chain = self.body[-1].y
        # elif self.head.direction == "up":
        #     x_chain = self.body[-1].x
        #     y_chain = self.body[-1].y + FAKTOR
        # elif self.head.direction == "down":
        #     x_chain = self.body[-1].x
        #     y_chain = self.body[-1].y - FAKTOR
        chain = Chain(None, None, None, None, None)
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




