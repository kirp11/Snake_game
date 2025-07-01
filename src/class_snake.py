
from src.constants import *
from src.texts_images_sounds import  *

import pygame

class Chain:
    def __init__(self, x, y, direction):
        self.__x = x
        self.__y = y
        self.__direction = direction

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_direction(self):
        return self.__direction

    def set_x(self, x):
        self.__x = x

    def change_x(self, x):
        self.__x += x

    def change_y(self, y):
        self.__y += y

    def set_y(self, y):
        self.__y = y

    def set_direction(self, direction):
        self.__direction = direction


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.head = Chain(300, 300, "right")
        self.body = []
        self.way_head = [[]]
        self.__delta_x = 0
        self.__delta_y = 0
        self.__speed = 5
        self.body.append(self.head)

    def get_delta_x(self):
        return self.__delta_x

    def get_delta_y(self):
        return self.__delta_y

    def get_speed(self):
        return self.__speed


    def set_delta_x(self, delta_x):
        self.__delta_x = delta_x

    def set_delta_y(self, delta_y):
        self.__delta_y = delta_y

    def set_speed(self, speed):
        self.__speed = speed


    def movie(self):
        self.handler_direction_head()
        self.screen.blit(snake_head_image, dest = (self.body[0].get_x() - 10, self.body[0].get_y() - 10))
        for i in range(1, len(self.body)):
            self.body[i].set_x(self.way_head[i * int(20 / self.__speed)][0])
            self.body[i].set_y(self.way_head[i * int(20 / self.__speed)][1])

            pygame.draw.circle(self.screen, BGREEN, (self.body[i].get_x(), self.body[i].get_y()), FAKTOR * 2)


    def handler_direction_head(self):
        self.head.change_x(self.get_delta_x())
        self.head.change_y(self.get_delta_y())
        self.way_head.insert(0, [self.head.get_x(), self.head.get_y()])

        self.handler_press()


    def handler_press(self):
        pressed = pygame.key.get_pressed()
        if  pressed[pygame.K_LEFT]:
            self.head.set_direction("left")
            press_sound.set_volume(0.2)
            press_sound.play()
        elif pressed[pygame.K_RIGHT]:
            self.head.set_direction("right")
            press_sound.set_volume(0.2)
            press_sound.play()
        elif pressed[pygame.K_UP]:
            self.head.set_direction("up")
            press_sound.set_volume(0.2)
            press_sound.play()
        elif pressed[pygame.K_DOWN]:
            self.head.set_direction("down")
            press_sound.set_volume(0.2)
            press_sound.play()
        self.choose_head_direction()


    def choose_head_direction(self):
        if self.head.get_direction()== "right":
            self.set_delta_x(self.get_speed())
            self.set_delta_y(0)
        elif self.head.get_direction() == "left":
            self.set_delta_y(0)
            self.set_delta_x(-self.get_speed())
        elif self.head.get_direction() == "up":
            self.set_delta_x(0)
            self.set_delta_y(-self.get_speed())
        elif self.head.get_direction() == "down":
            self.set_delta_x(0)
            self.set_delta_y(self.get_speed())

    def add_chain(self):
        chain = Chain(None, None, None)
        self.body.append(chain)
