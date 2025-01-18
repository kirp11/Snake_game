import pygame
import random
pygame.init()



class Game:
    def __init__(self):

    def screen(self):
        screen = pygame.display.set_mode((800, 600))
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

    def start(self):
        pygame.display.flip()
        pass

    def play(self):
        pass

    def restart(self):
        pass

    def exit(self):
        pass


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 2
        if pressed[pygame.K_DOWN]: y += 2
        if pressed[pygame.K_LEFT]: x -= 2
        if pressed[pygame.K_RIGHT]: x += 2


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        return pygame.draw.circle(screen, self.color, (self.x, self.y), 5)

    pass

class Snake(Point):
    def __init__(self):
        self.color = (0, 255,130)

    def change_dir(self):
        pass

    def add_node(self):
        pass

    def count_food(self):
        pass

    pass

class Border(Point):
    def __init__(self):
        self.color = (130, 0,20)

    pass

class Food(Point):
    def __init__(self):
        self.color = (10, 100,30)


    def create(self):



    pass