
from src.constants import *
from src.texts_images_sounds import  *

import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox


class Window:
    def __init__(self, lenght=500, high=500, frase=None, color=None):
        self.__lenght = lenght
        self.__high = high
        self.__frase = frase
        self.__color = color
        self.__screen = pygame.display.set_mode((self.__lenght, self.__high))
        pygame.display.set_caption("Start")
        self.__level = "Не выбрано"
        self.__theme = "Не выбрано"
        self.__text = ""
        self.__flag = False

    def get_lenght(self):
        return self.__lenght

    def get_high(self):
        return self.__high

    def get_frase(self):
        return self.__frase

    def get_color(self):
        return self.__color

    def get_screen(self):
        return self.__screen

    def get_level(self):
        return self.__level

    def get_theme(self):
        return self.__theme

    def get_text(self):
        return self.__text

    def get_flag(self):
        return self.__flag

    def set_lenght(self, lenght):
        self.__lenght = lenght

    def set_high(self, high):
        self.__high = high

    def set_frase(self, frase):
        self.__frase = frase

    def set_color(self, color):
        self.__color = color

    def set_screen(self):
        lenght = self.get_lenght()
        high = self.get_high()
        self.__screen = pygame.display.set_mode((lenght, high))

    def set_level(self, level):
        self.__level = level

    def set_theme(self, theme):
        self.__theme = theme

    def set_text(self, text):
        self.__text = text

    def set_flag(self, flag):
        self.__flag = flag

    def view(self):
        self.__screen = pygame.display.set_mode((self.__lenght, self.__high))
        pygame.display.set_caption(self.__frase)
        self.__screen.fill(self.__color)


    def game(self):
        current_title, icon_title = pygame.display.get_caption()
        if current_title != "Snake game":
            self.__lenght = 600
            self.__high = 700
            self.__frase = "Snake game"
            self.__color = WGREEN
            self.view()
        esc_font_text = pygame.font.SysFont('Verdana', 16)
        esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, BLACK)
        self.__screen.blit(esc_text, (240, 20))

    def winter_theme_game(self):
        current_title, icon_title = pygame.display.get_caption()
        if current_title != "Snake game":
            self.__lenght = 600
            self.__high = 700
            self.__frase = "Snake game"
            self.__color = WBLUE
            self.view()
        esc_font_text = pygame.font.SysFont('Verdana', 16)
        esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, WHITE)
        self.__screen.blit(esc_text, (240, 20))


    def summer_theme_game(self):
        current_title, icon_title = pygame.display.get_caption()
        if current_title != "Snake game":
            self.__lenght = 600
            self.__high = 700
            self.__frase = "Snake game"
            self.__color = WHITE
            self.view()
        self.__screen.blit(summer_image, (0, 50))
        esc_font_text = pygame.font.SysFont('Verdana', 16)
        esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, BLACK)
        self.__screen.blit(esc_text, (240, 20))


    def snowFall(self):
        for j in range(len(snowFall)):
            pygame.draw.circle(self.__screen, WHITE, snowFall[j], 2)
            snowFall[j][1] += 1.5
            if snowFall[j][1] > self.__high:
                y = random.randrange(20, 50)
                snowFall[j][1] = y
                x = random.randrange(0, self.__lenght)
                snowFall[j][0] = x

        esc_font_text = pygame.font.SysFont('Verdana', 16)
        esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, BLACK)
        self.__screen.blit(esc_text, (240, 20))


    def menu(self):
        current_title, icon_title =  pygame.display.get_caption()
        if current_title == "Main menu":
            over_font = pygame.font.SysFont('Verdana', 30)
            text_surface = over_font.render('Выберите действие', False, GREEN)
            self.__screen.blit(text_surface, (100, 20))
            return
        self.__lenght = 500
        self.__high = 500
        self.__frase = "Main menu"
        self.__color = WHITE
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
        self.__screen.blit(text_mouse, (mouse_x - 110, mouse_y + 30))

    def setting_menu(self):
        current_title, icon_title = pygame.display.get_caption()
        if current_title == "Settings menu":
            comlex_font = pygame.font.SysFont('Verdana', 25)
            choose_level = comlex_font.render(self.__level, False, BLUE)
            choose_theme = comlex_font.render(self.__theme, False, BLUE)
            self.__screen.blit(choose_level, (40, 300))
            self.__screen.blit(choose_theme, (230, 300))
            comlex_font = pygame.font.SysFont('Verdana', 25)
            comlex_text_surface = comlex_font.render('Выберите уровень сложности:', False, BLACK)
            theme_font = pygame.font.SysFont('Verdana', 25)
            theme_text_surface = theme_font.render('Выберите тему оформления:', False, BLACK)
            choose_text_surface = theme_font.render('Выбран вариант игры:', False, BLACK)
            choose_font_comlex = pygame.font.SysFont('Verdana', 15)
            choose_text_comlex = choose_font_comlex.render('Сложность', False, BLACK)
            choose_font_theme = pygame.font.SysFont('Verdana', 15)
            choose_text_theme = choose_font_theme.render('Тема', False, BLACK)
            self.__screen.blit(comlex_text_surface, (100, 10))
            self.__screen.blit(theme_text_surface, (100, 130))
            self.__screen.blit(choose_text_surface, (100, 250))
            self.__screen.blit(choose_text_comlex, (70, 280))
            self.__screen.blit(choose_text_theme, (260, 280))
            return
        self.__lenght = 600
        self.__high = 350
        self.__frase = "Settings menu"
        self.__color = YELLOW
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
                                             pressedColour=WGREEN, text="Voice of D.V.Rak",
                                             onClick=lambda: self.set_theme("Voice of D.V.Rak"))

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
        if current_title != "Game over":
            self.__lenght = 400
            self.__high = 400
            self.__frase = "Game over"
            self.__color = BLUE
            self.view()
        over_font = pygame.font.SysFont('Verdana', 50)
        text_surface = over_font.render('GAME OVER', False, YELLOW)
        over_font_result = pygame.font.SysFont('Verdana', 25)
        text_surface_result = over_font_result.render("ВАШ РЕЗУЛЬТАТ: "+str(count), False, YELLOW)
        over_font_low = pygame.font.SysFont('Verdana', 20)
        text_surface_low = over_font_low.render('НАЧАТЬ ЗАНОВО?', False, GREEN)
        self.__screen.blit(text_surface, (40, 0))
        self.__screen.blit(end_image, (100, 80))
        self.__screen.blit(text_surface_result, (80, 220))
        self.__screen.blit(text_surface_low, (100, 260))

    def draw_over_button(self):

        yes_button = Button(self.__screen, 260, 320, 120, 50, inactiveColour=YELLOW, radius=50,
                            pressedColour=(0, 255, 0), hoverColour = GREEN, text="ДА", onClick=lambda: self.set_frase("Snake game"))
        no_button = Button(self.__screen, 30, 320, 120, 50, inactiveColour=YELLOW, radius=50,
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
            self.__screen.blit(in_surface1, (80, 60))
            self.__screen.blit(in_surface2, (15, 100))
            return

        self.__lenght = 600
        self.__high = 400
        self.__frase = "Input_record"
        self.__color = SANDY
        self.view()


        def draw_textbox():
            def set_text():
                self.__text = text__box.getText()
                self.__flag = True
                text__box.hide()
                self.set_frase("Game over")

            surface = pygame.display.get_surface()
            text__box = TextBox(surface, 30, 150, 500, 60, fontSize=30, borderColour=WHITE,
                                    textColour=BGREEN, onSubmit=set_text, radius=10, borderThickness=5,
                                    placeholderText="Игрок")
        draw_textbox()


    def records(self, list_records):
        current_title, icon_title =  pygame.display.get_caption()
        if current_title != "Records":
            self.__lenght = 600
            self.__high = 400
            self.__frase = "Records"
            self.__color = SANDY
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

        self.__screen.blit(text_surface_1, (80, 80))
        self.__screen.blit(text_surface_2, (80, 130))
        self.__screen.blit(text_surface_3, (80, 180))
        self.__screen.blit(text_surface_4, (80, 230))
        self.__screen.blit(text_surface_5, (80, 280))

        self.__screen.blit(place_surface, (60, 20))
        self.__screen.blit(name_surface, (250, 20))
        self.__screen.blit(res_surface, (410, 20))

    def draw_to_menu_button(self):
        to_menu_button = Button(self.__screen, 200, 330, 200, 60, inactiveColour=GREEN, radius=30,
                                pressedColour=WGREEN, text="В МЕНЮ", onClick=lambda: self.set_frase("Main menu"))

        to_menu_button.draw()
        events = pygame.event.get()
        pygame_widgets.update(events)

    def pause(self):
        current_title, icon_title = pygame.display.get_caption()
        if current_title != "Pause menu":
            self.__lenght = 400
            self.__high = 200
            self.__frase = "Pause menu"
            self.__color = BLUE
            self.view()
        question = pygame.font.SysFont('Verdana', 20)
        text_question = question.render('ВЫЙТИ ИЗ ИГРЫ?', False, YELLOW)
        self.__screen.blit(text_question, (110, 50))

    def draw_pause_button(self):
        output_button = Button(self.__screen, 210, 120, 160, 30, inactiveColour=YELLOW, radius=40,
                               pressedColour=RED, hoverColour = RED, text="ВЫЙТИ В МЕНЮ", onClick=lambda: self.set_frase("Main menu"))
        input_button = Button(self.__screen, 20, 120, 160, 30, inactiveColour=YELLOW, radius=40,
                              pressedColour=GREEN, hoverColour = GREEN, text="ВЕРНУТЬСЯ В ИГРУ", onClick=lambda: self.set_frase("Snake game"))

        output_button.draw()
        input_button.draw()
        events = pygame.event.get()
        pygame_widgets.update(events)

    def warning(self):

        current_title, icon_title = pygame.display.get_caption()
        if current_title != "Warning window":
            self.__lenght = 400
            self.__high = 200
            self.__frase = "Warning window"
            self.__color = BLUE
            self.view()
        warning_font_text = pygame.font.SysFont('Verdana', 15)
        warning_text = warning_font_text.render('ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ И / ИЛИ ТЕМУ', False, YELLOW)
        self.__screen.blit(warning_text, (15, 50))

    def draw_warning_button(self):
        output_button = Button(self.__screen, 210, 120, 160, 30, inactiveColour=YELLOW, radius=40,
                               pressedColour=RED, hoverColour = RED, text="НАЗАД В МЕНЮ", onClick=lambda: self.set_frase("Main menu"))
        input_button = Button(self.__screen, 20, 120, 160, 30, inactiveColour=YELLOW, radius=40,
                              pressedColour=GREEN, hoverColour = GREEN, text="К НАСТРОЙКАМ", onClick=lambda: self.set_frase("Settings menu"))

        output_button.draw()
        input_button.draw()
        events = pygame.event.get()
        pygame_widgets.update(events)



class Records:
    def __init__(self):
        self.__result = ""
        self.__records = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""]]
        self.__name = ""


    def get_result(self):
        return self.__result

    def get_records(self):
        return self.__records

    def get_name(self):
        return self.__name

    def set_result(self, result: int):
        self.__result = result

    def set_records(self, records:list):
        self.__records = records

    def set_name(self, name:str):
        self.__name = name

    def check_on_record(self):
        if self.__result!= 0:
            i = 0
            if self.__records[i][1] == "":
                return True
            while self.__records[i][1] != "":
                if self.__records[i][1] < self.__result:
                    return True
                i += 1
            return False


    def add_result(self, name):
        if self.__result!= 0:
            if self.__records[0][1] == "":
                self.__records[0][1] = self.__result
                self.__records[0][0] = name
                return
            for i in range(0, 5, 1):

                if self.__records[i][1] < self.__result or self.__records[i][1] == "":
                    self.__records.insert(i, [name, self.__result])
                    self.__records = self.__records[:-1]
                    self.__result = 0
                    return
