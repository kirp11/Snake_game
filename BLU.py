from venv import create

import pygame
pygame.init()
from pygame_widgets.button import Button, ButtonArray
import pygame_widgets

import random

text_easy_level = "Идеальный выбор для начинающих"
text_medium_level = "Скорость выше + препятствия на поле"
text_hard_level = "Змейка сталкивается с собой"
text_winter_theme = "Тема холодной зимы"
text_summer_theme = "Тема жаркого лета"
text_voice_theme = "Озвучка голосом"



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

end_image = pygame.image.load('game_over.jpg')
# snake_head_image = pygame.image.load('snake_head.png')
snake_head = pygame.image.load('snake_head.png')
snake_head.set_colorkey((246,246,246))
snake_head_image = pygame.transform.scale(snake_head, (22, 22))

food = pygame.image.load('food.jpg')
food.set_colorkey(WHITE)
food_image = pygame.transform.scale(food, (25, 25))

bariere = pygame.image.load('bariere.jpg')
bariere.set_colorkey(WHITE)
bariere_image = pygame.transform.scale(bariere, (40, 40))


summer_img = pygame.image.load('summer.jpg')
summer_image = pygame.transform.scale(summer_img, (600, 700))

snowFall = []
for i in range(100):
    x = random.randrange(0, 600)
    y = random.randrange(50, 700)
    snowFall.append([x, y])

class Window:
    def __init__(self, lenght=None, high=None, frase=None, color=None):
        self.lenght = lenght
        self.high = high
        self.frase = frase
        self.color = color
        self.screen = None
        self.level = "Не выбрано"
        self.theme = "Не выбрано"



    def view(self):
        self.screen = pygame.display.set_mode((self.lenght, self.high))
        pygame.display.set_caption(self.frase)
        self.screen.fill(self.color)

    def get_frase(self):
        return self.frase

    def set_frase(self, frase):
        self.frase = frase

    def game(self):
        self.lenght = 600
        self.high = 700
        self.frase = "Snake game"
        self.color = WGREEN
        self.view()
        esc_font_text = pygame.font.SysFont('Verdana', 16)
        esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, BLACK)
        self.screen.blit(esc_text, (240, 20))

    def winter_theme_game(self):
        self.lenght = 600
        self.high = 700
        self.frase = "Snake game"
        self.color = WBLUE
        self.view()
        esc_font_text = pygame.font.SysFont('Verdana', 16)
        esc_text = esc_font_text.render('Взять паузу/выйти в меню - нажмите Esc', False, WHITE)
        self.screen.blit(esc_text, (240, 20))


    def summer_theme_game(self):
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
        self.lenght = 500
        self.high = 500
        self.frase = "Main menu"
        self.color = WHITE
        self.view()
        over_font = pygame.font.SysFont('Verdana', 30)
        text_surface = over_font.render('Выберите действие', False, GREEN)

        game_button = Button(self.screen, 100, 80, 300, 80, inactiveColour=YELLOW, radius=40,
        pressedColour=(0, 255, 0), hoverColour = GREEN, text="НАЧАТЬ ИГРУ", onClick=lambda: self.set_frase("Snake game"))
        record_button = Button(self.screen, 100, 180, 300, 80, inactiveColour=YELLOW, radius=40,
        pressedColour=(0, 255, 0), hoverColour = GREEN, text="ТАБЛИЦА РЕКОРДОВ",onClick=None)
        setting_button = Button(self.screen, 100, 280, 300, 80, inactiveColour=YELLOW, radius=40,
        pressedColour=(0, 255, 0), hoverColour = GREEN, text="НАСТРОЙКИ",onClick=lambda: self.set_frase("Settings menu"))
        exit_button = Button(self.screen, 100, 380, 300, 80, inactiveColour=YELLOW, radius=40,
        pressedColour=(0, 255, 0), hoverColour = GREEN, text="ВЫХОД",onClick= lambda: self.set_frase("Quit"))
        game_button.draw()
        record_button.draw()
        setting_button.draw()
        exit_button.draw()

        self.screen.blit(text_surface, (100, 20))

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
        self.lenght = 600
        self.high = 350
        self.frase = "Settings menu"
        self.color = YELLOW
        self.view()

        comlex_font = pygame.font.SysFont('Verdana', 25)
        comlex_text_surface = comlex_font.render('Выберите уровень сложности:', False, BLACK)

        theme_font = pygame.font.SysFont('Verdana', 25)
        theme_text_surface = theme_font.render('Выберите тему оформления:', False, BLACK)


        choose_text_surface = theme_font.render('Выбран вариант игры:', False, BLACK)
        choose_font_comlex = pygame.font.SysFont('Verdana', 15)
        choose_text_comlex = choose_font_comlex.render('Сложность', False, BLACK)
        choose_font_theme = pygame.font.SysFont('Verdana', 15)
        choose_text_theme = choose_font_theme.render('Тема', False, BLACK)

        # comlex_button = ButtonArray(self.screen, 40, 60, 500, 80, (3, 1),
        # border=20,  texts=('НОВИЧОК', 'ЛЮБИТЕЛЬ', 'ПРОФИ'),onClicks=(None, None, None), color=WHITE)


        easy_comlex_button = Button(self.screen, 30, 60, 170, 50, inactiveColour=WHITE, radius=0,
        pressedColour=WGREEN, text="НОВИЧОК", onClick=lambda: self.set_level("НОВИЧОК"))
        medium_comlex_button = Button(self.screen, 220, 60, 170, 50, inactiveColour=WHITE, radius=0,
        pressedColour=WGREEN, text="ЛЮБИТЕЛЬ", onClick=lambda: self.set_level("ЛЮБИТЕЛЬ"))
        hard_comlex_button = Button(self.screen, 410, 60, 170, 50, inactiveColour=WHITE, radius=0,
        pressedColour=WGREEN, text="ПРОФИ", onClick=lambda: self.set_level("ПРОФИ"))


        winter_theme_button = Button(self.screen, 30, 180, 170, 50, inactiveColour=WHITE, radius=0,
        pressedColour=WGREEN, text="WINTER", onClick=lambda: self.set_theme("WINTER"))
        summer_comlex_button = Button(self.screen, 220, 180, 170, 50, inactiveColour=WHITE, radius=0,
        pressedColour=WGREEN, text="SUMMER", onClick=lambda: self.set_theme("SUMMER"))
        voice_theme_button = Button(self.screen, 410, 180, 170, 50, inactiveColour=WHITE, radius=0,
        pressedColour=WGREEN, text="Voice", onClick=lambda: self.set_theme("Voice"))

        to_menu_button = Button(self.screen, 460, 290, 130, 50, inactiveColour=GREEN, radius=30,
        pressedColour=WGREEN, text="В МЕНЮ", onClick=lambda: self.set_frase("Main menu"))

        easy_comlex_button.draw()
        medium_comlex_button.draw()
        hard_comlex_button.draw()
        to_menu_button.draw()
        winter_theme_button.draw()
        summer_comlex_button.draw()
        voice_theme_button.draw()

        choose_level = comlex_font.render(self.level, False, RED)
        choose_theme = comlex_font.render(self.theme, False, RED)


        self.screen.blit(comlex_text_surface, (100, 10))

        self.screen.blit(theme_text_surface, (100, 130))

        self.screen.blit(choose_text_surface, (100, 250))

        self.screen.blit(choose_text_comlex, (70, 280))

        self.screen.blit(choose_level, (40, 300))

        self.screen.blit(choose_text_theme, (260, 280))

        self.screen.blit(choose_theme, (230, 300))


        self.display_tooltip()

        events = pygame.event.get()
        pygame_widgets.update(events)


    def game_over(self, count):
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

        yes_button = Button(self.screen, 260, 320, 120, 50, inactiveColour=YELLOW, radius=50,
        pressedColour=(0, 255, 0), hoverColour = GREEN, text="ДА", onClick=lambda: self.set_frase("Snake game"))
        no_button = Button(self.screen, 30, 320, 120, 50, inactiveColour=YELLOW, radius=50,
        pressedColour=(0, 255, 0), hoverColour = RED, text="НЕТ", onClick=lambda: self.set_frase("Main menu"))
        yes_button.draw()
        no_button.draw()
        self.screen.blit(text_surface, (40, 0))
        self.screen.blit(end_image, (100, 80))
        self.screen.blit(text_surface_result, (80, 220))
        self.screen.blit(text_surface_low, (100, 260))
        events = pygame.event.get()
        pygame_widgets.update(events)



    def pause(self):
        self.lenght = 400
        self.high = 200
        self.frase = "Pause menu"
        self.color = BLUE
        self.view()

        question = pygame.font.SysFont('Verdana', 20)
        text_question = question.render('ВЫЙТИ ИЗ ИГРЫ?', False, YELLOW)
        output_button = Button(self.screen, 210, 120, 160, 30, inactiveColour=YELLOW, radius=40,
        pressedColour=RED, hoverColour = RED, text="ВЫЙТИ В МЕНЮ", onClick=lambda: self.set_frase("Main menu"))
        input_button = Button(self.screen, 20, 120, 160, 30, inactiveColour=YELLOW, radius=40,
        pressedColour=GREEN, hoverColour = GREEN, text="ВЕРНУТЬСЯ В ИГРУ", onClick=lambda: self.set_frase("Snake game"))

        output_button.draw()
        input_button.draw()

        self.screen.blit(text_question, (110, 50))
        events = pygame.event.get()
        pygame_widgets.update(events)


    def warning(self):
        self.lenght = 400
        self.high = 200
        self.frase = "Warning window"
        self.color = BLUE
        self.view()

        warning_font_text = pygame.font.SysFont('Verdana', 15)
        warning_text = warning_font_text.render('ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ И / ИЛИ ТЕМУ', False, YELLOW)
        output_button = Button(self.screen, 210, 120, 160, 30, inactiveColour=YELLOW, radius=40,
        pressedColour=RED, hoverColour = RED, text="НАЗАД В МЕНЮ", onClick=lambda: self.set_frase("Main menu"))
        input_button = Button(self.screen, 20, 120, 160, 30, inactiveColour=YELLOW, radius=40,
        pressedColour=GREEN, hoverColour = GREEN, text="К НАСТРОЙКАМ", onClick=lambda: self.set_frase("Settings menu"))

        output_button.draw()
        input_button.draw()

        self.screen.blit(warning_text, (15, 50))
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


    def control(self):
        if self.window.frase == "Snake game":
            self.generate_window()

        elif self.window.frase == "Game over":
            self.window.game_over(self.rezult)
        elif self.window.frase == "Main menu":
            self.window.menu()
        elif self.window.frase == "Warning window":
            self.window.warning()
        elif self.window.frase == "Pause menu":
            self.window.pause()
        elif self.window.frase == "Settings menu":
            self.window.setting_menu()
        # elif self.window.frase == "Quit":
        #     event.type = pygame.QUIT

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
        return (abs(self.food.food_x - self.snake.body[0].x) <= 2*FAKTOR and abs(self.food.food_y - self.snake.body[0].y)<= 2*FAKTOR)

    def counter(self):
        surface = pygame.display.get_surface()
        font_count = pygame.font.SysFont('Verdana', 30)
        text_count = font_count.render("Ваш счет: "+str(self.count), True, BLUE)
        surface.blit(text_count,(10,10))

    def cross_with_food(self):
        surface = pygame.display.get_surface()
        if self.condition_of_cross():
            self.snake.add_chain()
            self.count += 1
            self.food = Food(surface, self.snake.head.x, self.snake.head.y)

    def cross_barrier(self):
        if self.check_cross_frame() or self.check_cross_field_barrier():
            self.snake = Snake(self.window.screen)
            self.rezult = self.count
            self.window.set_frase("Game over")
            self.count = 0
            self.barrier.lst_barier_x = []
            self.barrier.lst_barier_y = []
            self.barrier.barrier_list = []


    def check_cross_frame(self):
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
            self.window.set_frase("Game over")
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
        elif pressed[pygame.K_RIGHT]:
            self.head.direction = "right"
        elif pressed[pygame.K_UP]:
            self.head.direction = "up"
        elif pressed[pygame.K_DOWN]:
            self.head.direction = "down"
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

    def create(self):
        surface = pygame.display.get_surface()
        width_w = surface.get_width()
        height_w = surface.get_height()
        while self.food_x == self.stop_x and self.food_y == self.stop_y:
            self.food_x = random.randint(20,(width_w-20))
            self.food_y = random.randint(70,(height_w-20))
        # pygame.draw.circle(self.screen, (0, 0, 128), (self.food_x, self.food_y), FAKTOR*2)
        self.screen.blit(food_image, dest=(self.food_x-10, self.food_y-10))

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

    def field(self, count_barriers):
        surface = pygame.display.get_surface()
        width_w = surface.get_width()
        height_w = surface.get_height()
        n = 0
        while n!= count_barriers:
            barrier_x = random.randint(20, (width_w - 20))
            self.lst_barier_x.append(barrier_x)
            barrier_y = random.randint(70, (height_w - 20))
            self.lst_barier_y.append(barrier_y)
            n +=1
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT or game.window.frase == "Quit":
            running = False

    pygame.time.delay(60)
    game.control()
    pygame.display.flip()


pygame.quit()

