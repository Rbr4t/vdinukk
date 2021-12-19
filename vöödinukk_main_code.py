import pygame

#FUNKTSIOONID

def redrawWindow():
    screen.blit(bg, (0, 0))
    player.control(screen)
    pygame.display.flip()
    
    
#ANIMEERIMINE

#vajalikud pildid võetud kaustast
walkLeft = [pygame.image.load("characters/tüdruk_left/t_left1.png"),pygame.image.load("characters/tüdruk_left/t_left2.png"),
            pygame.image.load("characters/tüdruk_left/t_left3.png"),pygame.image.load("characters/tüdruk_left/t_left4.png")]
walkRight = [pygame.image.load("characters/tüdruk_right/t_right1.png"), pygame.image.load("characters/tüdruk_right/t_right2.png"),
             pygame.image.load("characters/tüdruk_right/t_right3.png"), pygame.image.load("characters/tüdruk_right/t_right4.png")]
walkFront = [pygame.image.load("characters/tüdruk_front/t_front1.png"), pygame.image.load("characters/tüdruk_front/t_front2.png"),
             pygame.image.load("characters/tüdruk_front/t_front3.png"), pygame.image.load("characters/tüdruk_front/t_front4.png")]
walkBack = [pygame.image.load("characters/tüdruk_back/t_back1.png"), pygame.image.load("characters/tüdruk_back/t_back2.png"),
            pygame.image.load("characters/tüdruk_back/t_back3.png"), pygame.image.load("characters/tüdruk_back/t_back4.png")]
playerpilt = "characters/tüdruk_front/t_front1.png"
playerpilt2 = playerpilt
char = pygame.image.load(playerpilt)
char2 = pygame.image.load(playerpilt2)

#TAUST

elutuba = pygame.image.load("bg/elutuba.png")
köök1 = pygame.image.load("bg/köök1.png")
köök2 = pygame.image.load("bg/köök2.png")
koridor = pygame.image.load("bg/koridoor.png")
magamistuba = pygame.image.load("bg/magamistuba.png")
sahver1 = pygame.image.load("bg/sahver1.png")
sahver2 = pygame.image.load("bg/sahver2.png")

#KLASSID
#playeri klass, mainklass
class Player:
    def __init__(self):
        self.x = 320
        self.y = 240
        self.vx = 0
        self.vy = 0
        
        self.image = pygame.Surface([800, 600])  
        self.left = False  #tulevad animeerimisega seotud väärtused
        self.right = False
        self.up = False
        self.down = False
        self.front1 = False
        self.back1 = True
        self.speed = 100
        self.stayfront = False
        self.stayback = False
        self.walkCount = 0 
        
    def update(self, dt):
    
        if abs(self.vx) == abs(self.vy):
            
            pass          #Jätan nii et diagonaalselt ei saaks liikuda
        else:
            
            self.x += self.vx * dt
            #print(self.vx)
            self.y += self.vy * dt
            #print(self.vy)
        
        
    def draw(self, s):
        s.blit(self.image, [self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2])
        
    def control(self, screen):
        
        if self.walkCount >= 32:
            self.walkCount = 0
        if self.left:  #kui on vasakul
            screen.blit(walkLeft[self.walkCount//8], (self.x, self.y)) #siis näitame ekraanile vasakule liikuvad pildid
                                                        # järjekorranumbri, milleks on walkCount muutuja
            self.walkCount += 1                              #x ja y kordinaatidele
        elif self.right:
            screen.blit(walkRight[self.walkCount//8], (self.x, self.y))
            self.walkCount += 1
            
        elif self.up:
            screen.blit(walkBack[self.walkCount//8], (self.x, self.y))
            self.walkCount += 1
            self.stayfront = False   
            self.stayback = True
            
        elif self.down:
            screen.blit(walkFront[self.walkCount//8], (self.x, self.y))
            self.walkCount += 1
            self.stayfront = True
            self.stayback = False
        else:
            try:    #python andis siin errori, nii et ma lihtsalt ignoreerin seda siin try ja except käskudega lol
                if self.stayfront:
                    screen.blit(self.char, [self.x, self.y])
                if self.stayback:
                    screen.blit(self.char2, [self.x, self.y])
            except:
                screen.blit(char, [self.x, self.y])
            
#MÄNG HAKKAB SIIT
pygame.init()

bg = pygame.Surface((0, 0)) #vajalik hilisemaks animeerimiseks

screen = pygame.display.set_mode([800, 600])

RUN = True


listi = ["UP", "LEFT", "RIGHT", "DOWN"]
buttonspressed = []

player = Player()

kell = pygame.time.Clock()
player.stayfront = True
bg = koridor
while RUN:
    pygame.time.delay(17)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            RUN = False
        if bg == koridor:
            if player.x < 39 and ((player.y <= 441 and player.y >= 375) or (player.y <= 302 and player.y >= 130)):
                can_walk = False
                player.x = 39
            else:
                can_walk = True
        if e.type == pygame.KEYDOWN: #Kui vajutatakse alla nuppu
            if e.key == pygame.K_UP: # and player.x > speed
                player.vy -= player.speed
                player.left = False
                player.right = False
                player.up = True
                player.down = False
                buttonspressed.append("UP")
            if e.key == pygame.K_DOWN:
                player.vy += player.speed
                player.left = False
                player.right = False
                player.up = False
                player.down = True
                buttonspressed.append("DOWN")
            if e.key == pygame.K_LEFT:
                player.vx -= player.speed
                player.left = True
                player.right = False
                player.up = False
                player.down = False
                buttonspressed.append("LEFT")
            if e.key == pygame.K_RIGHT:
                player.vx += player.speed
                player.left = False
                player.right = True
                player.up = False
                player.down = False
                buttonspressed.append("RIGHT")
        if e.type == pygame.KEYUP: #kui enam ei vajutata seda
            if e.key == pygame.K_UP:
                player.vy += player.speed
                player.left = False
                player.right = False
                player.up = False
                player.down = False
#                 player.stayfront = False   
#                 player.stayback = True
                buttonspressed.remove("UP")
            if e.key == pygame.K_DOWN:
                player.vy -= player.speed
                player.left = False
                player.right = False
                player.up = False
                player.down = False
#                 player.stayfront = True   
#                 player.stayback = False
                buttonspressed.remove("DOWN")
            if e.key == pygame.K_LEFT:
                player.vx += player.speed
                player.left = False
                player.right = False
                player.up = False
                player.down = False
                buttonspressed.remove("LEFT")
            if e.key == pygame.K_RIGHT:
                player.vx -= player.speed
                player.left = False
                player.right = False
                player.up = False
                player.down = False
                buttonspressed.remove("RIGHT")
        
    #print(buttonspressed)
    print(int(player.x), int(player.y))
    #asukoha kontrollimiseks
    dt = kell.tick()/500
    player.update(dt) #uuendame asukohta
    
    redrawWindow()
    screen.fill([255, 255, 255])
    
pygame.quit()
