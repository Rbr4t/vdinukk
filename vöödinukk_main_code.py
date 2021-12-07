import pygame, sys

pygame.init()
screen = pygame.display.set_mode([800, 600])
RUN = True


while RUN:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            RUN = False
    

pygame.quit()