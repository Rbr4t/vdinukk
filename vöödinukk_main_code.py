import pygame, sys

pygame.init()
screen = pygame.display.set_mode([800, 600])
RUN = True

#siia tuleb nüüd teha karakter ja teised defineeritavad muutujad, sest see siin on ainult algus

while RUN:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            RUN = False
        if e.type == pygame.

pygame.quit()