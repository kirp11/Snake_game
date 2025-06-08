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
        self.barrier = Barrier(self.window.start())

    def control(self):
        self.barrier.frame()
        self.snake.movie()
        self.food.create()
        self.cross_with_food()
        self.cross_barrier()

    def condition_of_cross(self):
        return (abs(self.food.food_x - self.snake.body[0].x) <= 2*FAKTOR and abs(self.food.food_y - self.snake.body[0].y)<= 2*FAKTOR)

    def cross_with_food(self):
        surface = pygame.display.get_surface()
        if self.condition_of_cross():
            self.snake.add_chain()
            self.food = Food(surface, self.snake.head.x, self.snake.head.y)

    def cross_barrier(self):
        if self.check_crash():
            pygame.quit()

    def check_crash(self):
        frame = self.barrier.frame()
        return not(frame.collidepoint(self.snake.head.x, self.snake.head.y))

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
        self.screen.fill((153,255,153))
        self.handler_direction_head()
        pygame.draw.circle(self.screen, (0, 128, 255), (self.body[0].x, self.body[0].y), FAKTOR*2)
        for i in range(1, len(self.body)):
            self.body[i].x = self.way_head[i*4][0]
            self.body[i].y = self.way_head[i*4][1]

            pygame.draw.circle(self.screen, (0, 128, 255), (self.body[i].x, self.body[i].y), FAKTOR*2)


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
        pygame.display.flip()
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




