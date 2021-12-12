import pygame, sys


playerpilt = "t_front1.png"

pygame.init()
screen = pygame.display.set_mode([800, 600])
RUN = True

#tegin praegu selle klassi, sest ilma ma ei saa alustada mängu liikumise tegemisega
class Player:
    def __init__(self):
        self.x = 320
        self.y = 240
        self.vx = 0
        self.vy = 0
        self.img = pygame.image.load(playerpilt)  #sai korda
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
        
player = Player()

speed = 100
kell = pygame.time.Clock()

while RUN:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            RUN = False
        if e.type == pygame.KEYDOWN: #Kui vajutatakse alla nuppu
            if e.key == pygame.K_UP:
                player.vy -= speed
            if e.key == pygame.K_DOWN:
                player.vy += speed
            if e.key == pygame.K_LEFT:
                player.vx -= speed
            if e.key == pygame.K_RIGHT:
                player.vx += speed
        if e.type == pygame.KEYUP: #kui enam ei vajutata seda
            if e.key == pygame.K_UP:
                player.vy += speed
            if e.key == pygame.K_DOWN:
                player.vy -= speed
            if e.key == pygame.K_LEFT:
                player.vx += speed
            if e.key == pygame.K_RIGHT:
                player.vx -= speed
    
    dt = kell.tick()/1000
    screen.fill([255, 255, 255])
    
    player.update(dt) #uuendame asukohta
    
    player.draw(screen) #joonistame ekraanile
    
    pygame.display.flip()

pygame.quit()