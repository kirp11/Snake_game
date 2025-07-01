
from texts_images_sounds import  *
import pygame

class Food:
    def __init__(self, screen, stop_x, stop_y):
        self.screen = screen
        self.__stop_x = stop_x
        self.__stop_y = stop_y
        self.__food_x = self.get_stop_x()
        self.__food_y = self.get_stop_y()
        self.__check = False

    def get_stop_x(self):
        return self.__stop_x

    def get_stop_y(self):
        return self.__stop_y

    def get_food_x(self):
        return self.__food_x

    def get_food_y(self):
        return self.__food_y

    def get_check(self):
        return self.__check

    def set_food_x(self, food_x):
        self.__food_x = food_x

    def set_food_y(self, food_y):
        self.__food_y = food_y

    def set_check(self, check):
        self.__check = check



    def create(self):
        surface = pygame.display.get_surface()
        width_w = surface.get_width()
        height_w = surface.get_height()


        while not self.get_check():
            self.set_food_x(random.randint(30, (width_w - 30)))
            self.set_food_y(random.randint(80, (height_w - 30)))

            if isinstance(self.get_stop_x(), int):
                if self.get_food_x() <= self.get_stop_x() + 40 and self.get_food_x() >= self.get_stop_x() - 40:
                    self.set_check(False)
                else:
                    if self.get_food_y() <= self.get_stop_y() + 40 and self.get_food_y() >= self.get_stop_y() - 40:
                        self.set_check(False)
                    else:
                        self.set_check(True)
            else:
                for i in self.get_stop_x():
                    if self.get_food_x() <= i + 40 and self.get_food_x() >= i - 40:
                        self.set_check(False)
                    else:
                        for j in self.__stop_y:
                            if self.get_food_y() <= j + 40 and self.get_food_y() >= j - 40:
                                self.set_check(False)
                            else:
                                self.set_check(True)
        self.screen.blit(food_image, dest=(self.get_food_x() - 10, self.get_food_y() - 10))

