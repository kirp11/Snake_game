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

class Generator_window:
    def __init__(self, event):
        self.event = event

    def select(self):
        pass


window = Window(500, 600, "Snake game")
running = True
while running:
    window.start()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()




