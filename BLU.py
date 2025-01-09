import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 255,130), pygame.Rect(400, 300, 10, 10))

    pygame.display.flip()

