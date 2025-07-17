
from src.texts_images_sounds import  *

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


    def check_cross_with_selfbarier(self, barrier_x, barrier_y):
        for i in range(len(self.lst_barier_x)):
            if barrier_x >= self.lst_barier_x[i] -70 and barrier_x <= self.lst_barier_x[i] + 70:
                for j in range(i, len(self.lst_barier_y)):
                    if barrier_y >= self.lst_barier_y[j] - 70 and barrier_y <= self.lst_barier_y[j] + 70:
                        return True
        return False

    def field(self, count_barriers):
        surface = pygame.display.get_surface()
        width_w = surface.get_width()
        height_w = surface.get_height()
        while len(self.lst_barier_x) < count_barriers:
            if len(self.lst_barier_x)==0:
                barrier_x = random.randint(40, (width_w - 40))
                barrier_y = random.randint(80, (height_w - 40))
            else:
                barrier_x = random.randint(40, (width_w - 40))
                barrier_y = random.randint(80, (height_w - 40))
                while self.check_cross_with_selfbarier(barrier_x, barrier_y):
                    barrier_x = random.randint(40, (width_w - 40))
                    barrier_y = random.randint(80, (height_w - 40))
            self.lst_barier_x.append(barrier_x)
            self.lst_barier_y.append(barrier_y)


        for i in range(len(self.lst_barier_x)):
            rect_position = self.lst_barier_x[i], self.lst_barier_y[i]
            rect = bariere_image.get_rect()
            rect.center = rect_position
            self.screen.blit(bariere_image, rect)
            barrier = pygame.draw.rect(self.screen, WHITE, rect, 1)
            self.barrier_list.append(barrier)
