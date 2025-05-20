import pygame
import random
pygame.init()



class Window:
    def __init__(self, lenght, high, frase):
        self.lenght = lenght
        self.high = high
        self.frase = frase

    def start(self):
        screen = pygame.display.set_mode((self.lenght, self.high))
        pygame.display.set_caption(self.frase)
        return screen

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
        pygame.draw.circle(self.screen, (0, 128, 255), (self.x, self.y), 5)
        self.x += self.delta_x
        self.y += self.delta_y
        self.handler_press()

    def handler_press(self):
        pressed = pygame.key.get_pressed()
        if  pressed[pygame.K_LEFT]:
            self.delta_y = 0
            self.delta_x = -10
        if pressed[pygame.K_RIGHT]:
            self.delta_y = 0
            self.delta_x = 10
        if pressed[pygame.K_UP]:
            self.delta_x = 0
            self.delta_y = -10
        if pressed[pygame.K_DOWN]:
            self.delta_x = 0
            self.delta_y = 10





running = True
window = Window(500, 600, "Snake game")
snake = Snake(window.start())
while running:
    pygame.time.delay(60)
    snake.movie()


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()




