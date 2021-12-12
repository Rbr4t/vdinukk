import pygame, sys
#from klassid.py import *

playerpilt = "t_front1"

pygame.init()
screen = pygame.display.set_mode([800, 600])
RUN = True

class Player:
    def __init__(self):
        self.x = 320
        self.y = 240
        self.vx = 0
        self.vy = 0
        self.img = pygame.image.load(playerpilt)  #<----- see siin veel ei tööta
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
        
player = Player()

speed = 10
kell = pygame.time.Clock()

while RUN:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            RUN = False
        if e.type == pygame.KEYDOWN: #Kui vajutatakse alla nuppu
            if e.key == K_UP:
                player.vy += speed
            if e.key == K_DOWN:
                player.vy -= speed
            if e.key == K_LEFT:
                player.vx -= speed
            if e.key == K_RIGHT:
                player.vx += speed
        if e.type == pygame.UP: #kui enam ei vajutata seda
            if e.key == K_UP:
                player.vy -= speed
            if e.key == K_DOWN:
                player.vy += speed
            if e.key == K_LEFT:
                player.vx += speed
            if e.key == K_RIGHT:
                player.vx -= speed
    
    screen.fill([255, 255, 255])
    player.update(dt) #uuendame asukohta
    player.draw(screen) #joonistame ekraanile
    pygame.display.flip()

pygame.quit()