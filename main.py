
from src.game import  Game
from src.texts_images_sounds import *
import pygame
pygame.init()
pygame.mixer.init()

class Programm:

    @staticmethod
    def main():
        running = True
        game = Game()
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or game.window.get_frase() == QUIT:
                    running = False

            pygame.time.delay(30)
            game.control()
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    session = Programm()
    session.main()