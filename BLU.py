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
        self.food = Food(self.window.start(), self.snake.body[0].x, self.snake.body[0].y)

    def control(self):
        self.snake.movie()
        self.food.create()
        self.cross_with_food()

    def condition_of_cross(self):
        return (abs(self.food.food_x - self.snake.body[0].x) <= FAKTOR and abs(self.food.food_y - self.snake.body[0].y)<= FAKTOR)

    def cross_with_food(self):
        if self.condition_of_cross():
            self.snake.add_chain()
            surface = pygame.display.get_surface()
            self.food = Food(surface, self.snake.head.x, self.snake.head.y)
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
        self.head = Chain(300, 300, None, None, "right")
        self.body = []
        self.delta_x = 0
        self.delta_y = 0
        self.body.append(self.head)

    def movie(self):
        self.screen.fill((0, 0, 0))
        self.handler_direction_head()
        for i in range(len(self.body)):
            if i != 0:
                self.body[i].x = self.body[i-1].x_next
                self.body[i].y = self.body[i-1].y_next
            pygame.draw.circle(self.screen, (0, 128, 255), (self.body[i].x, self.body[i].y), FAKTOR)




    def handler_direction_head(self):
        self.head.x += self.delta_x
        self.head.y += self.delta_y
        self.head.x_next = self.head.x - 2*self.delta_x
        self.head.y_next = self.head.y - 2*self.delta_y
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


    def add_chain(self):
        if self.head.direction == "right":
            x_chain = self.head.x - FAKTOR*2
            y_chain = self.head.y
        elif self.head.direction == "left":
            x_chain = self.head.x + FAKTOR*2
            y_chain = self.head.y
        elif self.head.direction == "up":
            x_chain = self.head.x
            y_chain = self.head.y + FAKTOR*2
        elif self.head.direction == "down":
            x_chain = self.head.x
            y_chain = self.head.y - FAKTOR*2
        chain = Chain(x_chain, y_chain, None, None, "right")
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




