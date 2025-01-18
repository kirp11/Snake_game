import pygame
import random
pygame.init()



class Round:
    def __init__(self, drive):
        self.drive = drive


    def screen(self):
        weight_screen = 800
        hight_screen = 600
        screen = pygame.display.set_mode((weight_screen, hight_screen))
        return screen


    def play(self):
        pass

    def restart(self):
        pass

    def exit(self):
        pass


class Point:
    def __init__(self, x=None, y=None, color= None):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 5)



class Snake(Point):
    def __init__(self, len_ = 1, color = (0, 255,130)):
        self.x = 400
        self.y = 300
        self.len = len_
        self.color = color

    def change_dir(self, screen):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self.y -= 2
        elif pressed[pygame.K_DOWN]: self.y += 2
        elif pressed[pygame.K_LEFT]: self.x -= 2
        elif pressed[pygame.K_RIGHT]: self.x += 2



    def add_node(self):
        pass

    def count_food(self):
        pass

    pass

class Border(Point):
    def __init__(self, color = (130, 0,20)):
        self.color = color

    def create(self, screen):
        self.y = 1
        for self.x in range(0, 800, 5):
            Border.draw(self, screen)
        pygame.display.flip()

class Food(Point):
    def __init__(self, color = (10, 100,30)):
        self.color = color


    def create(self):
        pass


r1 = Round(True)
p1 = Point()
s1 = Snake()
b1 = Border()


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    b1.create(r1.screen())
    s1.change_dir(r1.screen())
    s1.draw(r1.screen())
    pygame.display.flip()

