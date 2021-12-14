import pygame

#FUNKTSIOONID

def redrawWindow():
    global walkCount
    screen.blit(bg, (0, 0))
    if walkCount +1 >= 32:
        walkCount = 0
    if left:  #kui on vasakul
        screen.blit(walkLeft[walkCount//8], (player.x, player.y)) #siis näitame ekraanile vasakule liikuvad pildid
                                                    # järjekorranumbri, milleks on walkCOunt muutuja
        walkCount += 1                              #x ja y kordinaatidele
    elif right:
        screen.blit(walkRight[walkCount//8], (player.x, player.y))
        walkCount += 1
        
    elif up:
        screen.blit(walkBack[walkCount//8], (player.x, player.y))
        walkCount += 1
    elif down:
        screen.blit(walkFront[walkCount//8], (player.x, player.y))
        walkCount += 1
    else:
        player.draw(screen)
        
    pygame.display.flip()
    
#ANIMEERIMINE

#vajalikud pildid võetud kaustast
walkLeft = [pygame.image.load("characters/tüdruk_left/t_left1.png"),
            pygame.image.load("characters/tüdruk_left/t_left2.png"), pygame.image.load("characters/tüdruk_left/t_left3.png"),
            pygame.image.load("characters/tüdruk_left/t_left4.png")]
walkRight = [pygame.image.load("characters/tüdruk_right/t_right1.png"), pygame.image.load("characters/tüdruk_right/t_right2.png"),
             pygame.image.load("characters/tüdruk_right/t_right3.png"), pygame.image.load("characters/tüdruk_right/t_right4.png")]
walkFront = [pygame.image.load("characters/tüdruk_front/t_front1.png"), pygame.image.load("characters/tüdruk_front/t_front2.png"),
             pygame.image.load("characters/tüdruk_front/t_front3.png"), pygame.image.load("characters/tüdruk_front/t_front4.png")]
walkBack = [pygame.image.load("characters/tüdruk_back/t_back1.png"), pygame.image.load("characters/tüdruk_back/t_back2.png"),
            pygame.image.load("characters/tüdruk_back/t_back3.png"), pygame.image.load("characters/tüdruk_back/t_back4.png")]
playerpilt = "characters/tüdruk_front/t_front1.png"
char = pygame.image.load(playerpilt)
#KLASSID

#playeri klass, mainklass
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
        
#Mäng hakkab siit
pygame.init()

bg = pygame.Surface((0, 0)) #vajalik hilisemaks animeerimiseks

screen = pygame.display.set_mode([800, 600])

RUN = True
        
player = Player()

#tulevad animeerimisega seotud väärtused
left = False
right = False
up = False
down = False

speed = 100
walkCount= 0 #see muutuja on siin selle jaoks et hiljem saaks
kell = pygame.time.Clock()

while RUN:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            RUN = False
        if e.type == pygame.KEYDOWN: #Kui vajutatakse alla nuppu
            if e.key == pygame.K_UP: # and player.x > speed
                player.vy -= speed
                left = False
                right = False
                up = True
                down = False
            if e.key == pygame.K_DOWN:
                player.vy += speed
                left = False
                right = False
                up = False
                down = True
                
            if e.key == pygame.K_LEFT:
                player.vx -= speed
                left = True
                right = False
                up = False
                down = False

            if e.key == pygame.K_RIGHT:
                player.vx += speed
                left = False
                right = True
                up = False
                down = False
        if e.type == pygame.KEYUP: #kui enam ei vajutata seda
            if e.key == pygame.K_UP:
                player.vy += speed
                left = False
                right = False
                up = False
                down = False
            if e.key == pygame.K_DOWN:
                player.vy -= speed
                left = False
                right = False
                up = False
                down = False
            if e.key == pygame.K_LEFT:
                player.vx += speed
                left = False
                right = False
                up = False
                down = False
            if e.key == pygame.K_RIGHT:
                player.vx -= speed
                left = False
                right = False
                up = False
                down = False
    
    dt = kell.tick()/500
    
    player.update(dt) #uuendame asukohta
    
    redrawWindow()
    screen.fill([255, 255, 255])
    
pygame.quit()