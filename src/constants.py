import random

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
snowFall = []
for i in range(100):
    x = random.randrange(0, 600)
    y = random.randrange(50, 700)
    snowFall.append([x, y])