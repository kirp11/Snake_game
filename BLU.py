from venv import create

import os


import pygame
pygame.init()
pygame.mixer.init()
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox


from pygame.locals import *

import random

text_easy_level = "Идеальный выбор для начинающих"
text_medium_level = "Скорость выше + препятствия на поле"
text_hard_level = "Змейка сталкивается с собой"
text_winter_theme = "Тема холодной зимы"
text_summer_theme = "Тема жаркого лета"
text_voice_theme = "Озвучка голосом"


main_sound = pygame.mixer.Sound(os.path.join("src/sounds", "main.wav"))
food_sound = pygame.mixer.Sound(os.path.join('src/sounds', "food.wav"))
over_sound = pygame.mixer.Sound(os.path.join('src/sounds', "over.wav"))
press_sound = pygame.mixer.Sound(os.path.join('src/sounds', "press.wav"))
fast_sound = pygame.mixer.Sound(os.path.join('src/sounds', "fast.wav"))



FAKTOR = 5
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WBLUE = (123,200,246)
WGREEN = (153,255,153)
BGREEN = (0,69,36)
YELLOW = (255, 255, 0)
ORANGE = (255,165,0)
SANDY = (205,170,127)



end_image = pygame.image.load(os.path.join('src/images','game_over.jpg'))
snake_head = pygame.image.load(os.path.join('src/images','snake_head.png'))
snake_head.set_colorkey((246,246,246))
snake_head_image = pygame.transform.scale(snake_head, (22, 22))

food = pygame.image.load(os.path.join('src/images','food.jpg'))
food.set_colorkey(WHITE)
food_image = pygame.transform.scale(food, (25, 25))

bariere = pygame.image.load(os.path.join('src/images','bariere.jpg'))
bariere.set_colorkey(WHITE)
bariere_image = pygame.transform.scale(bariere, (40, 40))


summer_img = pygame.image.load(os.path.join('src/images','summer.jpg'))
summer_image = pygame.transform.scale(summer_img, (600, 700))

snowFall = []
for i in range(100):
    x = random.randrange(0, 600)
    y = random.randrange(50, 700)
    snowFall.append([x, y])


class Records:
    def __init__(self):
        self.result = ""
        self.records = [["",""],["",""],["",""],["",""],["",""]]
        self.name = ""

    def check_on_record(self):
        if self.result!= 0:
            i = 0
            if self.records[i][1] == "":
                return True
            while self.records[i][1] != "":
                if self.records[i][1] < self.result:
                    return True
                i += 1
            return False


    def add_result(self, name):
        if self.result!= 0:
            if self.records[0][1] == "":
                self.records[0][1] = self.result
                self.records[0][0] = name
                return
            for i in range(0, 5, 1):

                if self.records[i][1] < self.result or self.records[i][1] == "":
                    self.records.insert(i,[name, self.result])
                    self.records = self.records[:-1]
                    self.result = 0
                    return


class Window:
    def __init__(self, lenght=500, high=500, frase=None, color=None):
        self.lenght = lenght
        self.high = high
        self.frase = frase
        self.color = color
        self.screen = pygame.display.set_mode((self.lenght, self.high))
        pygame.display.set_caption("Start")
        self.level = "Не выбрано"
        self.theme = "Не выбрано"
        self.text = ""
        self.flag = False



    def view(self):
        self.screen = pygame.display.set_mode((self.lenght, self.high))
        pygame.display.set_caption(self.frase)
        self.screen.fill(self.color)

    def get_frase(self):
        return self.frase


    def set_frase(self, frase):
        self.frase = frase


    def game(self):
        current_title, icon_title = pygame.display.get_caption()
        if current_title == "Snake game":

            esc_font_text = pygame.font.SysFont('Verdana', 16)
            esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, BLACK)
            self.screen.blit(esc_text, (240, 20))
            self.screen.fill(self.color)
            return
        self.lenght = 600
        self.high = 700
        self.frase = "Snake game"
        self.color = WGREEN
        self.view()
        esc_font_text = pygame.font.SysFont('Verdana', 16)
        esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, BLACK)
        self.screen.blit(esc_text, (240, 20))

    def winter_theme_game(self):
        current_title, icon_title = pygame.display.get_caption()
        if current_title == "Snake game":
            esc_font_text = pygame.font.SysFont('Verdana', 16)
            esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, WHITE)
            self.screen.blit(esc_text, (240, 20))
            return
        self.lenght = 600
        self.high = 700
        self.frase = "Snake game"
        self.color = WBLUE
        self.view()
        esc_font_text = pygame.font.SysFont('Verdana', 16)
        esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, WHITE)
        self.screen.blit(esc_text, (240, 20))


    def summer_theme_game(self):
        current_title, icon_title = pygame.display.get_caption()
        if current_title == "Snake game":
            self.screen.blit(summer_image, (0, 50))
            esc_font_text = pygame.font.SysFont('Verdana', 16)
            esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, BLACK)
            self.screen.blit(esc_text, (240, 20))
            return
        self.lenght = 600
        self.high = 700
        self.frase = "Snake game"
        self.color = WHITE
        self.view()

        self.screen.blit(summer_image, (0, 50))
        esc_font_text = pygame.font.SysFont('Verdana', 16)
        esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, BLACK)
        self.screen.blit(esc_text, (240, 20))


    def snowFall(self):

        # clock = pygame.time.Clock()
        for j in range(len(snowFall)):
            pygame.draw.circle(self.screen, WHITE, snowFall[j], 2)

            snowFall[j][1] += 1.5
            if snowFall[j][1] > self.high:
                y = random.randrange(20, 50)
                snowFall[j][1] = y

                x = random.randrange(0, self.lenght)
                snowFall[j][0] = x


        esc_font_text = pygame.font.SysFont('Verdana', 16)
        esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, BLACK)
        self.screen.blit(esc_text, (240, 20))


    def menu(self):
        current_title, icon_title =  pygame.display.get_caption()
        if current_title == "Main menu":

            over_font = pygame.font.SysFont('Verdana', 30)
            text_surface = over_font.render('Выберите действие', False, GREEN)

            self.screen.blit(text_surface, (100, 20))
            return

        self.lenght = 500
        self.high = 500
        self.frase = "Main menu"
        self.color = WHITE
        self.view()


    def draw_menu_button(self):
        surface = pygame.display.get_surface()

        game_button = Button(surface, 100, 80, 300, 80, inactiveColour=YELLOW, radius=40,
                             pressedColour=(0, 255, 0), hoverColour=GREEN, text="НАЧАТЬ ИГРУ",
                             onClick=lambda: self.set_frase("Snake game"))
        record_button = Button(surface, 100, 180, 300, 80, inactiveColour=YELLOW, radius=40,
                               pressedColour=(0, 255, 0), hoverColour=GREEN, text="ТАБЛИЦА РЕКОРДОВ",
                               onClick=lambda: self.set_frase("Records"))
        setting_button = Button(surface, 100, 280, 300, 80, inactiveColour=YELLOW, radius=40,
                                     pressedColour=(0, 255, 0), hoverColour=GREEN, text="НАСТРОЙКИ",
                                     onClick=lambda: self.set_frase("Settings menu"))
        exit_button = Button(surface, 100, 380, 300, 80, inactiveColour=YELLOW, radius=40,
                                  pressedColour=(0, 255, 0), hoverColour=GREEN, text="ВЫХОД",
                                  onClick=lambda: self.set_frase("Quit"))
        game_button.draw()
        record_button.draw()
        setting_button.draw()
        exit_button.draw()

        events = pygame.event.get()
        pygame_widgets.update(events)

    def set_level(self, level):
        self.level = level

    def set_theme(self, theme):
        self.theme = theme

    def display_tooltip(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        text_dir = "Наведите на кнопку для описания"
        if 30 <= mouse_x <= 200 and 60 <= mouse_y <= 110:
            text_dir = text_easy_level
        elif 220 <= mouse_x <= 390 and 60 <= mouse_y <= 110:
            text_dir = text_medium_level
        elif 410 <= mouse_x <= 580 and 60 <= mouse_y <= 110:
            text_dir = text_hard_level
        elif 30 <= mouse_x <= 200 and 180 <= mouse_y <= 230:
            text_dir = text_winter_theme
        elif 220 <= mouse_x <= 390 and 180 <= mouse_y <= 230:
            text_dir = text_summer_theme
        elif 410 <= mouse_x <= 580 and 180 <= mouse_y <= 230:
            text_dir = text_voice_theme

        font_mouse = pygame.font.SysFont(None, 28)
        text_mouse = font_mouse.render(text_dir, False, BLUE)

        self.screen.blit(text_mouse, (mouse_x-110, mouse_y+30))

    def setting_menu(self):
        current_title, icon_title = pygame.display.get_caption()
        if current_title == "Settings menu":
            comlex_font = pygame.font.SysFont('Verdana', 25)
            choose_level = comlex_font.render(self.level, False, BLUE)
            choose_theme = comlex_font.render(self.theme, False, BLUE)
            self.screen.blit(choose_level, (40, 300))
            self.screen.blit(choose_theme, (230, 300))
            comlex_font = pygame.font.SysFont('Verdana', 25)
            comlex_text_surface = comlex_font.render('Выберите уровень сложности:', False, BLACK)

            theme_font = pygame.font.SysFont('Verdana', 25)
            theme_text_surface = theme_font.render('Выберите тему оформления:', False, BLACK)

            choose_text_surface = theme_font.render('Выбран вариант игры:', False, BLACK)
            choose_font_comlex = pygame.font.SysFont('Verdana', 15)
            choose_text_comlex = choose_font_comlex.render('Сложность', False, BLACK)
            choose_font_theme = pygame.font.SysFont('Verdana', 15)
            choose_text_theme = choose_font_theme.render('Тема', False, BLACK)

            self.screen.blit(comlex_text_surface, (100, 10))

            self.screen.blit(theme_text_surface, (100, 130))

            self.screen.blit(choose_text_surface, (100, 250))

            self.screen.blit(choose_text_comlex, (70, 280))

            self.screen.blit(choose_text_theme, (260, 280))

            return


        self.lenght = 600
        self.high = 350
        self.frase = "Settings menu"
        self.color = YELLOW
        self.view()



    def draw_setting_buttons(self):
        try:
            surface = pygame.display.get_surface()

            easy_comlex_button = Button(surface, 30, 60, 170, 50, inactiveColour=WHITE, radius=0,
                                             pressedColour=WGREEN, text="НОВИЧОК",
                                             onClick=lambda: self.set_level("НОВИЧОК"))
            medium_comlex_button = Button(surface, 220, 60, 170, 50, inactiveColour=WHITE, radius=0,
                                               pressedColour=WGREEN, text="ЛЮБИТЕЛЬ",
                                               onClick=lambda: self.set_level("ЛЮБИТЕЛЬ"))
            hard_comlex_button = Button(surface, 410, 60, 170, 50, inactiveColour=WHITE, radius=0,
                                             pressedColour=WGREEN, text="ПРОФИ",
                                             onClick=lambda: self.set_level("ПРОФИ"))

            winter_theme_button = Button(surface, 30, 180, 170, 50, inactiveColour=WHITE, radius=0,
                                              pressedColour=WGREEN, text="WINTER",
                                              onClick=lambda: self.set_theme("WINTER"))
            summer_comlex_button = Button(surface, 220, 180, 170, 50, inactiveColour=WHITE, radius=0,
                                               pressedColour=WGREEN, text="SUMMER",
                                               onClick=lambda: self.set_theme("SUMMER"))
            voice_theme_button = Button(surface, 410, 180, 170, 50, inactiveColour=WHITE, radius=0,
                                             pressedColour=WGREEN, text="Voice",
                                             onClick=lambda: self.set_theme("Voice"))

            to_menu_button = Button(surface, 460, 290, 130, 50, inactiveColour=GREEN, radius=30,
                                         pressedColour=WGREEN, text="В МЕНЮ",
                                         onClick=lambda: self.set_frase("Main menu"))
            self.display_tooltip()
            easy_comlex_button.draw()
            medium_comlex_button.draw()
            hard_comlex_button.draw()
            to_menu_button.draw()
            winter_theme_button.draw()
            summer_comlex_button.draw()
            voice_theme_button.draw()
        except:
            pass

        events = pygame.event.get()
        pygame_widgets.update(events)


    def game_over(self, count):
        current_title, icon_title =  pygame.display.get_caption()
        if current_title == "Game over":
            over_font = pygame.font.SysFont('Verdana', 50)
            text_surface = over_font.render('GAME OVER', False, YELLOW)
            over_font_result = pygame.font.SysFont('Verdana', 25)
            text_surface_result = over_font_result.render("ВАШ РЕЗУЛЬТАТ: " + str(count), False, YELLOW)
            over_font_low = pygame.font.SysFont('Verdana', 20)
            text_surface_low = over_font_low.render('НАЧАТЬ ЗАНОВО?', False, GREEN)
            self.screen.blit(text_surface, (40, 0))
            self.screen.blit(end_image, (100, 80))
            self.screen.blit(text_surface_result, (80, 220))
            self.screen.blit(text_surface_low, (100, 260))
            return

        self.lenght = 400
        self.high = 400
        self.frase = "Game over"
        self.color = BLUE
        self.view()
        over_font = pygame.font.SysFont('Verdana', 50)
        text_surface = over_font.render('GAME OVER', False, YELLOW)
        over_font_result = pygame.font.SysFont('Verdana', 25)
        text_surface_result = over_font_result.render("ВАШ РЕЗУЛЬТАТ: "+str(count), False, YELLOW)
        over_font_low = pygame.font.SysFont('Verdana', 20)
        text_surface_low = over_font_low.render('НАЧАТЬ ЗАНОВО?', False, GREEN)
        self.screen.blit(text_surface, (40, 0))
        self.screen.blit(end_image, (100, 80))
        self.screen.blit(text_surface_result, (80, 220))
        self.screen.blit(text_surface_low, (100, 260))

    def draw_over_button(self):

        yes_button = Button(self.screen, 260, 320, 120, 50, inactiveColour=YELLOW, radius=50,
        pressedColour=(0, 255, 0), hoverColour = GREEN, text="ДА", onClick=lambda: self.set_frase("Snake game"))
        no_button = Button(self.screen, 30, 320, 120, 50, inactiveColour=YELLOW, radius=50,
        pressedColour=(0, 255, 0), hoverColour = RED, text="НЕТ", onClick=lambda: self.set_frase("Main menu"))
        yes_button.draw()
        no_button.draw()

        events = pygame.event.get()
        pygame_widgets.update(events)


    def input_record(self):

        events = pygame.event.get()
        pygame_widgets.update(events)

        current_title, icon_title = pygame.display.get_caption()
        if current_title == "Input_record":


            in_font = pygame.font.SysFont('Verdana', 20)
            in_surface1 = in_font.render('!! Вы попали в список рекордсменов !!', False, BLUE)
            in_surface2 = in_font.render('Впишите свое имя для отражения на доске почета:',
                                         False, BLUE)
            self.screen.blit(in_surface1, (80, 60))
            self.screen.blit(in_surface2, (15, 100))


            # pygame.display.update()

            return


        self.lenght = 600
        self.high = 400
        self.frase = "Input_record"
        self.color = SANDY
        self.view()
        # in_font = pygame.font.SysFont('Verdana', 20)
        # in_surface1 = in_font.render('!! Вы попали в список рекордсменов !!', False, BLUE)
        # in_surface2 = in_font.render('Впишите свое имя для отражения на доске почета:',
        #                              False, BLUE)
        # self.screen.blit(in_surface1, (80, 60))
        # self.screen.blit(in_surface2, (15, 100))

        def draw_textbox():
            def set_text():
                # nonlocal text__box
                txxxt = text__box.getText()

                self.text = txxxt
                self.flag = True
                text__box.hide()
                self.set_frase("Game over")

            surface = pygame.display.get_surface()
            text__box = TextBox(surface, 30, 150, 500, 60, fontSize=30, borderColour=WHITE,
                                    textColour=BGREEN, onSubmit=set_text, radius=10, borderThickness=5,
                                    placeholderText="Игрок")
            # events = pygame.event.get()
            # pygame_widgets.update(events)
            # self.screen.fill((255, 255, 255))

        draw_textbox()
        #
        # pygame_widgets.update(events)
        # pygame.display.update()







            # self.screen.fill(self.color)
            # text__box.draw()
            # to_menu_button = Button(self.screen, 200, 330, 200, 60, inactiveColour=GREEN, radius=30,
            # pressedColour=WGREEN, text="В МЕНЮ", onClick=lambda: self.set_frase("Main menu"))
            #
            # to_menu_button.draw()
            # self.screen.fill((255, 255, 255))

        # for event in events:
        #     # pygame_widgets.update(event)
        #     if event.type == pygame.K_RETURN:
        #         # running = False
        #         pygame_widgets.update(events)








    def records(self, list_records):
        current_title, icon_title =  pygame.display.get_caption()
        if current_title == "Records":
            rec_font = pygame.font.SysFont('Verdana', 20)
            place_surface = rec_font.render('МЕСТО', False, BLACK)
            name_surface = rec_font.render('ИМЯ', False, BLACK)
            res_surface = rec_font.render('РЕЗУЛЬТАТ', False, BLACK)
            res_font = pygame.font.SysFont('Verdana', 20)
            text_surface_1 = res_font.render(
                str(1) + "                      " + str(list_records[0][0]) + "                      " + str(
                    list_records[0][1]), True, WHITE)
            text_surface_2 = res_font.render(
                str(2) + "                      " + str(list_records[1][0]) + "                      " + str(
                    list_records[1][1]), True, WHITE)
            text_surface_3 = res_font.render(
                str(3) + "                      " + str(list_records[2][0]) + "                      " + str(
                    list_records[2][1]), True, WHITE)
            text_surface_4 = res_font.render(
                str(4) + "                      " + str(list_records[3][0]) + "                      " + str(
                    list_records[3][1]), True, WHITE)
            text_surface_5 = res_font.render(
                str(5) + "                      " + str(list_records[4][0]) + "                      " + str(
                    list_records[4][1]), True, WHITE)

            self.screen.blit(text_surface_1, (80, 80))
            self.screen.blit(text_surface_2, (80, 130))
            self.screen.blit(text_surface_3, (80, 180))
            self.screen.blit(text_surface_4, (80, 230))
            self.screen.blit(text_surface_5, (80, 280))

            self.screen.blit(place_surface, (60, 20))
            self.screen.blit(name_surface, (250, 20))
            self.screen.blit(res_surface, (410, 20))
            return

        self.lenght = 600
        self.high = 400
        self.frase = "Records"
        self.color = SANDY
        self.view()

        rec_font = pygame.font.SysFont('Verdana', 20)
        place_surface = rec_font.render('МЕСТО', False, BLACK)
        name_surface = rec_font.render('ИМЯ', False, BLACK)
        res_surface = rec_font.render('РЕЗУЛЬТАТ', False, BLACK)
        res_font = pygame.font.SysFont('Verdana', 20)
        text_surface_1 = res_font.render(str(1)+"                      "+str(list_records[0][0])+"                      "+str(list_records[0][1]), True, BLACK)
        text_surface_2 = res_font.render(str(2)+"                      "+str(list_records[1][0])+"                      "+str(list_records[1][1]), True, BLACK)
        text_surface_3 = res_font.render(str(3)+"                      "+str(list_records[2][0])+"                      "+str(list_records[2][1]), True, BLACK)
        text_surface_4 = res_font.render(str(4)+"                      "+str(list_records[3][0])+"                      "+str(list_records[3][1]), True, BLACK)
        text_surface_5 = res_font.render(str(5)+"                      "+str(list_records[4][0])+"                      "+str(list_records[4][1]), True, BLACK)

        self.screen.blit(text_surface_1, (80,80))
        self.screen.blit(text_surface_2, (80, 130))
        self.screen.blit(text_surface_3, (80, 180))
        self.screen.blit(text_surface_4, (80, 230))
        self.screen.blit(text_surface_5, (80, 280))

        self.screen.blit(place_surface, (60, 20))
        self.screen.blit(name_surface, (250, 20))
        self.screen.blit(res_surface, (410, 20))

    def draw_to_menu_button(self):
        to_menu_button = Button(self.screen, 200, 330, 200, 60, inactiveColour=GREEN, radius=30,
        pressedColour=WGREEN, text="В МЕНЮ", onClick=lambda: self.set_frase("Main menu"))

        to_menu_button.draw()

        events = pygame.event.get()
        pygame_widgets.update(events)

    def pause(self):
        current_title, icon_title = pygame.display.get_caption()
        if current_title == "Pause menu":
            question = pygame.font.SysFont('Verdana', 20)
            text_question = question.render('ВЫЙТИ ИЗ ИГРЫ?', False, YELLOW)
            self.screen.blit(text_question, (110, 50))
            return


        self.lenght = 400
        self.high = 200
        self.frase = "Pause menu"
        self.color = BLUE
        self.view()

        question = pygame.font.SysFont('Verdana', 20)
        text_question = question.render('ВЫЙТИ ИЗ ИГРЫ?', False, YELLOW)
        self.screen.blit(text_question, (110, 50))

    def draw_pause_button(self):
        output_button = Button(self.screen, 210, 120, 160, 30, inactiveColour=YELLOW, radius=40,
        pressedColour=RED, hoverColour = RED, text="ВЫЙТИ В МЕНЮ", onClick=lambda: self.set_frase("Main menu"))
        input_button = Button(self.screen, 20, 120, 160, 30, inactiveColour=YELLOW, radius=40,
        pressedColour=GREEN, hoverColour = GREEN, text="ВЕРНУТЬСЯ В ИГРУ", onClick=lambda: self.set_frase("Snake game"))

        output_button.draw()
        input_button.draw()

        events = pygame.event.get()
        pygame_widgets.update(events)

    def warning(self):

        current_title, icon_title = pygame.display.get_caption()
        if current_title == "Warning window":
            warning_font_text = pygame.font.SysFont('Verdana', 15)
            warning_text = warning_font_text.render('ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ И / ИЛИ ТЕМУ', False, YELLOW)
            self.screen.blit(warning_text, (15, 50))
            return

        self.lenght = 400
        self.high = 200
        self.frase = "Warning window"
        self.color = BLUE
        self.view()

        warning_font_text = pygame.font.SysFont('Verdana', 15)
        warning_text = warning_font_text.render('ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ И / ИЛИ ТЕМУ', False, YELLOW)
        self.screen.blit(warning_text, (15, 50))

    def draw_warning_button(self):
        output_button = Button(self.screen, 210, 120, 160, 30, inactiveColour=YELLOW, radius=40,
        pressedColour=RED, hoverColour = RED, text="НАЗАД В МЕНЮ", onClick=lambda: self.set_frase("Main menu"))
        input_button = Button(self.screen, 20, 120, 160, 30, inactiveColour=YELLOW, radius=40,
        pressedColour=GREEN, hoverColour = GREEN, text="К НАСТРОЙКАМ", onClick=lambda: self.set_frase("Settings menu"))

        output_button.draw()
        input_button.draw()

        events = pygame.event.get()
        pygame_widgets.update(events)



class Game:
    def __init__(self):

        self.window = Window()
        self.window.menu()
        self.snake = Snake(self.window.screen)
        self.food = Food(self.window.screen, self.snake.body[0].x, self.snake.body[0].y)
        self.barrier = Barrier(self.window.screen)
        self.count = 0
        self.rezult = 0
        self.record = Records()
        self.is_sound = False


    def add_main_sound(self):
        if  self.is_sound == False:
            if self.window.level == "НОВИЧОК":
                main_sound.play()
            else:
                fast_sound.play()
        self.is_sound = True

    def stop_main_sound(self):
        if self.is_sound == True:
            if self.window.level == "НОВИЧОК":
                main_sound.stop()
            else:
                fast_sound.stop()

        self.is_sound = False





    def control(self):
        self.window.screen.fill(self.window.color)
        if self.window.frase == "Snake game":
            self.add_main_sound()
            self.generate_window()

        elif self.window.frase == "Game over":
            self.window.game_over(self.rezult)
            self.window.draw_over_button()
        elif self.window.frase == "Main menu":
            self.window.menu()
            self.window.draw_menu_button()
        elif self.window.frase == "Warning window":
            self.window.warning()
            self.window.draw_warning_button()
        elif self.window.frase == "Pause menu":
            self.stop_main_sound()
            self.window.pause()
            self.window.draw_pause_button()
        elif self.window.frase == "Settings menu":
            self.window.setting_menu()
            self.window.draw_setting_buttons()
        elif self.window.frase == "Records":
            self.window.records(self.record.records)
            self.window.draw_to_menu_button()
        elif self.window.frase == "Input_record":
            self.window.input_record()
            if self.window.flag:
            # self.window.draw_to_menu_button()
            # self.window.draw_textbox()
                self.record.add_result(self.window.text)
                self.window.flag = False
            # self.window.set_frase("Game over")
        # elif self.window.frase == "Quit":
        #     event.type = pygame.QUIT
        # pygame_widgets.update(events)

    def generate_window(self):
        if self.check_full():
            if self.window.theme == "SUMMER":
                self.window.summer_theme_game()
                self.barrier.summer_frame()
            elif self.window.theme == "WINTER":
                self.window.winter_theme_game()
                self.barrier.winter_frame()
                self.window.snowFall()
            elif self.window.theme == "Voice":
                self.window.game()
                self.barrier.frame()
            self.counter()
            self.snake.movie()
            self.food.create()
            self.cross_with_food()
            self.cross_barrier()
            self.check_on_pause()
            if self.window.level == "ЛЮБИТЕЛЬ":
                self.snake.speed = 10
                self.barrier.field(5)
            elif self.window.level == "ПРОФИ":
                self.snake.speed = 10
                self.barrier.field(10)
                self.cross_with_self()



    def check_full(self):
        if self.window.level == "Не выбрано" or self.window.theme == "Не выбрано":
            self.window.set_frase("Warning window")
            return False
        return True


    def check_on_pause(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.window.set_frase("Pause menu")


    def condition_of_cross(self):
        return (abs(self.food.food_x - self.snake.body[0].x) <= 3*FAKTOR and abs(self.food.food_y - self.snake.body[0].y)<= 3*FAKTOR)

    def counter(self):
        surface = pygame.display.get_surface()
        font_count = pygame.font.SysFont('Verdana', 30)
        text_count = font_count.render("Ваш счет: "+str(self.count), True, BLUE)
        surface.blit(text_count,(10,10))

    def cross_with_food(self):
        surface = pygame.display.get_surface()
        if self.condition_of_cross():

            food_sound.play()
            self.snake.add_chain()
            self.count += 1
            if self.window.level == "ЛЮБИТЕЛЬ" or self.window.level == "ПРОФИ":
                self.food = Food(surface, self.barrier.lst_barier_x, self.barrier.lst_barier_y)
            else:
                self.food = Food(surface, self.snake.head.x, self.snake.head.y)
            self.food.check = False


    def cross_barrier(self):
        if self.check_cross_frame() or self.check_cross_field_barrier():

            self.snake = Snake(self.window.screen)
            self.rezult = self.count
            self.record.result = self.count
            # over_sound.play()
            if self.record.check_on_record():
                self.window.set_frase("Input_record")
            else:
                self.window.set_frase("Game over")
            self.stop_main_sound()
            over_sound.play()
            self.count = 0
            self.barrier.lst_barier_x = []
            self.barrier.lst_barier_y = []
            self.barrier.barrier_list = []


    def check_cross_frame(self):
        if self.window.theme == "WINTER":
            return not self.barrier.winter_frame().collidepoint(self.snake.head.x, self.snake.head.y)
        if self.window.theme == "SUMMER":
            return not self.barrier.summer_frame().collidepoint(self.snake.head.x, self.snake.head.y)
        if self.window.theme == "Voice":
            return not self.barrier.frame().collidepoint(self.snake.head.x, self.snake.head.y)



    def check_cross_field_barrier(self):
        for i in range(len(self.barrier.barrier_list)):
            if self.barrier.barrier_list[i].collidepoint(self.snake.head.x, self.snake.head.y):
                return True

    def condition_of_cross_self(self):
        for i in range(1, len(self.snake.body)):
            if self.snake.head.x == self.snake.body[i].x and self.snake.head.y == self.snake.body[i].y:
                return True

    def cross_with_self(self):
        if self.condition_of_cross_self():

            self.snake = Snake(self.window.screen)
            self.rezult = self.count
            if self.record.check_on_record():
                self.window.set_frase("Input_record")
            else:
                self.window.set_frase("Game over")
            self.stop_main_sound()
            over_sound.play()
            self.count = 0
            self.barrier.lst_barier_x = []
            self.barrier.lst_barier_y = []
            self.barrier.barrier_list = []



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
        self.speed = 5

    def movie(self):
        self.handler_direction_head()
        # pygame.draw.circle(self.screen, BLUE, (self.body[0].x, self.body[0].y), FAKTOR*2)
        self.screen.blit(snake_head_image, dest = (self.body[0].x-10, self.body[0].y-10))
        for i in range(1, len(self.body)):
            self.body[i].x = self.way_head[i*int(20/self.speed)][0]
            self.body[i].y = self.way_head[i*int(20/self.speed)][1]

            pygame.draw.circle(self.screen, BGREEN, (self.body[i].x, self.body[i].y), FAKTOR*2)


    def handler_direction_head(self):
        self.head.x += self.delta_x
        self.head.y += self.delta_y
        self.way_head.insert(0, [self.head.x, self.head.y])

        self.handler_press()


    def handler_press(self):
        pressed = pygame.key.get_pressed()
        if  pressed[pygame.K_LEFT]:
            self.head.direction = "left"
            press_sound.play()
        elif pressed[pygame.K_RIGHT]:
            self.head.direction = "right"
            press_sound.play()
        elif pressed[pygame.K_UP]:
            self.head.direction = "up"
            press_sound.play()
        elif pressed[pygame.K_DOWN]:
            self.head.direction = "down"
            press_sound.play()
        self.choose_head_direction()


    def choose_head_direction(self):
        if self.head.direction == "right":
            self.delta_x = self.speed
            self.delta_y = 0
        elif self.head.direction == "left":
            self.delta_y = 0
            self.delta_x = -self.speed
        elif self.head.direction == "up":
            self.delta_x = 0
            self.delta_y = -self.speed
        elif self.head.direction == "down":
            self.delta_x = 0
            self.delta_y = self.speed

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
        self.check = False

    def create(self):
        surface = pygame.display.get_surface()
        width_w = surface.get_width()
        height_w = surface.get_height()
        # for i in self.stop_x:
        #     if self.food_x <= i + 5:
        #         for j in self.stop_y:
        #             if self.food_y <= j + 5:
        #
        #             self.food_x = random.randint(20, (width_w - 20))
        #             self.food_y = random.randint(70, (height_w - 20))

        while not self.check:
            self.food_x = random.randint(30, (width_w - 30))
            self.food_y = random.randint(80, (height_w - 30))

            if isinstance(self.stop_x, int):
                if self.food_x <= self.stop_x + 40 and self.food_x >= self.stop_x - 40:
                    self.check = False
                else:
                    if self.food_y <= self.stop_y + 40 and self.food_y >= self.stop_y - 40:
                        self.check = False
                    else:
                        self.check = True
            else:

                for i in self.stop_x:
                    if self.food_x <= i + 40 and self.food_x >= i - 40:
                        self.check = False
                    else:
                        for j in self.stop_y:
                            if self.food_y <= j + 40 and self.food_y >= j - 40:
                                self.check = False
                            else:
                                self.check = True

        # while self.food_x == self.stop_x and self.food_y == self.stop_y:
        #     self.food_x = random.randint(30, (width_w - 30))
        #     self.food_y = random.randint(80, (height_w - 30))


        self.screen.blit(food_image, dest=(self.food_x - 10, self.food_y - 10))


class Barrier:
    def __init__(self, screen):
        self.screen = screen
        self.lst_barier_x = []
        self.lst_barier_y = []
        self.barrier_list = []

    def frame(self):

        width_w = self.screen.get_width()
        height_w = self.screen.get_height()-50
        frame = pygame.draw.rect(self.screen, (51,102,0), [0, 50, width_w, height_w], FAKTOR*2)
        return frame

    def winter_frame(self):

        width_w = self.screen.get_width()
        height_w = self.screen.get_height()-50
        frame = pygame.draw.rect(self.screen, WHITE, [0, 50, width_w, height_w], FAKTOR*2)
        return frame

    def summer_frame(self):

        width_w = self.screen.get_width()
        height_w = self.screen.get_height()-50
        frame = pygame.draw.rect(self.screen, ORANGE, [0, 50, width_w, height_w], FAKTOR*2)
        return frame


    def check_cross_with_selfbarier(self, barrier, list_barrier):
        for i in list_barrier:
            if barrier <= (i + 30) and barrier >= (i - 30):
                print("pppppp")
                return True
        print("nooooo")
        return False

    def field(self, count_barriers):
        surface = pygame.display.get_surface()
        width_w = surface.get_width()
        height_w = surface.get_height()
        # n = 0
        barrier_x = 0
        barrier_y = 0
        print(self.lst_barier_x)
        while len(self.lst_barier_x) <= count_barriers:
            if len(self.barrier_list)==0:
                barrier_x = random.randint(40, (width_w - 40))
                self.lst_barier_x.append(barrier_x)
                barrier_y = random.randint(80, (height_w - 40))
                self.lst_barier_y.append(barrier_y)
            else:
                while self.check_cross_with_selfbarier(barrier_x, self.lst_barier_x) + self.check_cross_with_selfbarier(barrier_y, self.lst_barier_y)==2:
                    print("lllllllllllll")
                    barrier_x = random.randint(40, (width_w - 40))
                    barrier_y = random.randint(80, (height_w - 40))

            self.lst_barier_x.append(barrier_x)
            self.lst_barier_y.append(barrier_y)

            # n +=1
        for i in range(count_barriers):
            rect_position = self.lst_barier_x[i], self.lst_barier_y[i]
                # , 25, 25]
            # barrier = pygame.draw.rect(self.screen, BLACK, rect_position)
            #
            # self.screen.blit(bariere_image, self.lst_barier_x[i], self.lst_barier_y[i])

            rect = bariere_image.get_rect()
            rect.center = rect_position
            self.screen.blit(bariere_image, rect)
            barrier = pygame.draw.rect(self.screen, WHITE, rect, 1)
            self.barrier_list.append(barrier)





running = True
game = Game()

while running:
    events = pygame.event.get()
    # pygame_widgets.update(events)
    for event in events:
        # pygame_widgets.update(event)
        if event.type == pygame.QUIT or game.window.frase == "Quit":
            running = False

    pygame.time.delay(30)
    game.control()
    # pygame.display.flip()


    pygame.display.update()
pygame.quit()

