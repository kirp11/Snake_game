from constants import *
import os
import pygame
pygame.init()
pygame.mixer.init()

text_easy_level = "Идеальный выбор для начинающих"
text_medium_level = "Скорость выше + препятствия на поле"
text_hard_level = "Змейка сталкивается с собой"
text_winter_theme = "Тема холодной зимы"
text_summer_theme = "Тема жаркого лета"
text_voice_theme = "Озвучка голосом"


main_sound = pygame.mixer.Sound(os.path.join("sounds", "main.wav"))
food_sound = pygame.mixer.Sound(os.path.join('sounds', "food.wav"))
over_sound = pygame.mixer.Sound(os.path.join('sounds', "over.wav"))
press_sound = pygame.mixer.Sound(os.path.join('sounds', "press.wav"))
fast_sound = pygame.mixer.Sound(os.path.join('sounds', "fast.wav"))

voice_sound = []
for i in range(1,16):
    voice_sound.append(os.path.join("sounds/D_V_Rak", f"{i}.wav"))
over_voice = pygame.mixer.Sound(os.path.join('sounds/D_V_Rak', "over.wav"))

end_image = pygame.image.load(os.path.join('images','game_over.jpg'))
snake_head = pygame.image.load(os.path.join('images','snake_head.png'))
snake_head.set_colorkey((246,246,246))
snake_head_image = pygame.transform.scale(snake_head, (22, 22))

food = pygame.image.load(os.path.join('images','food.jpg'))
food.set_colorkey(WHITE)
food_image = pygame.transform.scale(food, (25, 25))

bariere = pygame.image.load(os.path.join('images','bariere.jpg'))
bariere.set_colorkey(WHITE)
bariere_image = pygame.transform.scale(bariere, (40, 40))

summer_img = pygame.image.load(os.path.join('images','summer.jpg'))
summer_image = pygame.transform.scale(summer_img, (600, 700))