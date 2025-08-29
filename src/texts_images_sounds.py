
import os
import random
import pygame

pygame.mixer.init()

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

# список снежка
snowfall = []
for i in range(100):
    x = random.randrange(0, 600)
    y = random.randrange(50, 700)
    snowfall.append([x, y])

text_easy_level = "Идеальный выбор для начинающих"
text_medium_level = "Скорость выше + препятствия на поле"
text_hard_level = "Змейка сталкивается с собой"
text_winter_theme = "Тема холодной зимы"
text_summer_theme = "Тема жаркого лета"
text_voice_theme = "Озвучка голосом преподавателя"


main_sound = pygame.mixer.Sound(os.path.join("resources\sounds", "main.wav"))
food_sound = pygame.mixer.Sound(os.path.join('resources\sounds', "food.wav"))
over_sound = pygame.mixer.Sound(os.path.join('resources\sounds', "over.wav"))
press_sound = pygame.mixer.Sound(os.path.join('resources\sounds', "press.wav"))
fast_sound = pygame.mixer.Sound(os.path.join('resources\sounds', "fast.wav"))


voice_sound = []
for i in range(1,16):
    voice_sound.append(os.path.join("resources/sounds/D_V_Rak", f"{i}.wav"))
over_voice = pygame.mixer.Sound(os.path.join('resources/sounds/D_V_Rak', "over.wav"))


end_image = pygame.image.load(os.path.join('resources/images','game_over.jpg'))
snake_head = pygame.image.load(os.path.join('resources/images','snake_head.png'))
snake_head.set_colorkey((246,246,246))
snake_head_image = pygame.transform.scale(snake_head, (22, 22))


food = pygame.image.load(os.path.join('resources/images','food.jpg'))
food.set_colorkey(WHITE)
food_image = pygame.transform.scale(food, (25, 25))


bariere = pygame.image.load(os.path.join('resources/images','bariere.jpg'))
bariere.set_colorkey(WHITE)
bariere_image = pygame.transform.scale(bariere, (40, 40))


summer_img = pygame.image.load(os.path.join('resources/images','summer.jpg'))
summer_image = pygame.transform.scale(summer_img, (600, 700))

# УРОВНИ СЛОЖНОСТИ

EASY = "НОВИЧОК"
MEDIUM = "ЛЮБИТЕЛЬ"
HARD = "ПРОФИ"

# ТЕМЫ

SUMMER = "SUMMER"
WINTER = "WINTER"
DVRAK = "Voice of D.V.Rak"

# НАЗВАНИЯ ОКОН

WARN_W = "Warning window"
SNAKE = "Snake game"
GAME_OVER = "Game over"
MAIN_MENU = "Main menu"
PAUSE = "Pause menu"
SETTING = "Settings menu"
RECORDS = "Records"
INPUT = "Input_record"
QUIT = "Quit"

LEVEL_SOUND_MAIN = 0.2
LEVEL_SOUND_FOOD = 1.0




