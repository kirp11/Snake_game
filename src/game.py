import sys

from venv import create
import os

from src.texts_images_sounds import *

from src.GUI import  Records, Window
from src.entyties import Snake, Chain, Food, Barrier

from pygame.locals import *

import random


class Game:
    def __init__(self):

        self.window = Window()
        self.window.menu()
        self.snake = Snake(self.window.get_screen())
        self.food = Food(self.window.get_screen(), self.snake.body[0].get_x(), self.snake.body[0].get_y())
        self.barrier = Barrier(self.window.get_screen())
        self.record = Records()
        self.__count = 0
        self.__rezult = 0
        self.__is_sound = False

    def get_count(self):
        return self.__count

    def get_rezult(self):
        return self.__rezult

    def get_is_sound(self):
        return self.__is_sound

    def set_count(self, count):
        self.__count += count

    def zero_count(self):
        self.__count = 0

    def set_rezult(self, rezult):
        self.__rezult = rezult

    def set_is_sound(self, is_sound):
        self.__is_sound = is_sound


    def add_main_sound(self):
        if  self.get_is_sound() == False:
            if self.window.get_level() == EASY:
                main_sound.set_volume(LEVEL_SOUND_MAIN)
                main_sound.play(loops=-1)
            else:
                fast_sound.set_volume(LEVEL_SOUND_MAIN)
                fast_sound.play(loops=-1)
        self.set_is_sound(True)

    def stop_main_sound(self):
        if self.get_is_sound() == True:
            if self.window.get_level() == EASY:
                main_sound.stop()
            else:
                fast_sound.stop()
        self.set_is_sound(False)

    def food_music(self):
        if self.window.get_theme() == DVRAK:
            song = random.choice(voice_sound)
            food_voice = pygame.mixer.Sound(song)
            food_voice.set_volume(LEVEL_SOUND_FOOD)
            food_voice.play()
            return
        food_sound.play()

    def finish_sound(self):
        if self.window.get_theme() == DVRAK:
            over_voice.set_volume(LEVEL_SOUND_FOOD)
            over_voice.play()
            return
        over_sound.play()

# основная распределительная функция

    def control(self):
        self.window.get_screen().fill(self.window.get_color())
        frase = self.window.get_frase()
        if frase == SNAKE:

            self.generate_window()

        elif frase == GAME_OVER:
            self.window.game_over(self.get_rezult())
            self.window.draw_over_button()
        elif frase == MAIN_MENU:
            self.window.menu()
            self.window.draw_menu_button()
        elif frase == WARN_W:
            self.window.warning()
            self.window.draw_warning_button()
        elif frase == PAUSE:
            self.stop_main_sound()
            self.window.pause()
            self.window.draw_pause_button()
        elif frase == SETTING:
            self.window.setting_menu()
            self.window.draw_setting_buttons()
        elif frase == RECORDS:
            self.window.records(self.record.get_records())
            self.window.draw_to_menu_button()
        elif frase == INPUT:
            self.window.input_record()
            if self.window.get_flag():
                self.record.add_result(self.window.get_text())
                self.window.set_flag(False)

# функция настроек окон

    def generate_window(self):
        if self.check_full():
            if self.window.get_theme() == SUMMER:
                self.window.create_game()
                self.barrier.summer_frame()
            elif self.window.get_theme() == WINTER:
                self.window.create_game()
                self.barrier.winter_frame()
                self.window.snow_fall()
            elif self.window.get_theme() == DVRAK:
                self.window.create_game()
                self.barrier.frame()
            self.add_main_sound()
            self.counter()
            self.snake.movie()
            self.food.create()
            self.cross_with_food()
            self.cross_barrier()
            self.check_on_pause()
            if self.window.get_level() == MEDIUM:
                self.snake.set_speed(10)
                self.barrier.field(5)
            elif self.window.get_level() == HARD:
                self.snake.set_speed(10)
                self.barrier.field(10)
                self.cross_with_self()

    def check_full(self):
        if self.window.get_level() == "Не выбрано" or self.window.get_theme() == "Не выбрано":
            self.window.set_frase(WARN_W)
            return False
        return True


    def check_on_pause(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.window.set_frase(PAUSE)


    def condition_of_cross(self):
        return (abs(self.food.get_food_x() - self.snake.body[0].get_x()) <= 3 * FAKTOR and abs(self.food.get_food_y() - self.snake.body[0].get_y()) <= 3 * FAKTOR)

    def counter(self):
        surface = pygame.display.get_surface()
        font_count = pygame.font.SysFont('Verdana', 30)
        text_count = font_count.render("Ваш счет: " + str(self.__count), True, BLUE)
        surface.blit(text_count,(10,10))

    def cross_with_food(self):
        surface = pygame.display.get_surface()
        if self.condition_of_cross():
            self.food_music()
            self.snake.add_chain()
            self.set_count(1)
            if self.window.get_level() == MEDIUM or self.window.get_level() == HARD:
                self.food = Food(surface, self.barrier.lst_barier_x, self.barrier.lst_barier_y)
            else:
                self.food = Food(surface, self.snake.head.get_x(), self.snake.head.get_y())
            self.food.__check = False


    def cross_barrier(self):
        if self.check_cross_frame() or self.check_cross_field_barrier():

            self.snake = Snake(self.window.get_screen())
            self.set_rezult(self.get_count())
            self.record.set_result(self.get_count())
            self.finish_sound()
            if self.record.check_on_record():
                self.window.set_frase(INPUT)
            else:
                self.window.set_frase(GAME_OVER)
            self.stop_main_sound()
            self.zero_count()
            self.barrier.lst_barier_x = []
            self.barrier.lst_barier_y = []
            self.barrier.barrier_list = []


    def check_cross_frame(self):
        if self.window.get_theme() == WINTER:
            return not self.barrier.winter_frame().collidepoint(self.snake.head.get_x(), self.snake.head.get_y())
        if self.window.get_theme() == SUMMER:
            return not self.barrier.summer_frame().collidepoint(self.snake.head.get_x(), self.snake.head.get_y())
        if self.window.get_theme() == DVRAK:
            return not self.barrier.frame().collidepoint(self.snake.head.get_x(), self.snake.head.get_y())


    def check_cross_field_barrier(self):
        for i in range(len(self.barrier.barrier_list)):
            if self.barrier.barrier_list[i].collidepoint(self.snake.head.get_x(), self.snake.head.get_y()):
                return True


    def condition_of_cross_self(self):
        for i in range(1, len(self.snake.body)):
            if self.snake.head.get_x() == self.snake.body[i].get_x() and self.snake.head.get_y() == self.snake.body[i].get_y():
                return True


    def cross_with_self(self):
        if self.condition_of_cross_self():

            self.snake = Snake(self.window.get_screen())
            self.set_rezult(self.get_count())
            self.finish_sound()
            if self.record.check_on_record():
                self.window.set_frase(INPUT)
            else:
                self.window.set_frase(GAME_OVER)
            self.stop_main_sound()
            self.zero_count()
            self.barrier.lst_barier_x = []
            self.barrier.lst_barier_y = []
            self.barrier.barrier_list = []