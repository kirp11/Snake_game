
from texts_images_sounds import  *
import pygame


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
