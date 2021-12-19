from pygame import *
import pygame_gui, pygame

def mäng():
    import pygame

    #HELI
    pygame.mixer.init()
    kõndimine = pygame.mixer.Sound("footstep06.ogg")
    #kõndimine.play()
    kõndimine.set_volume(0.1)
    uks = pygame.mixer.Sound("doorOpen_1.ogg")
    uks.set_volume(0.1)
    musics = pygame.mixer.music.load("Twin Musicom - Stopping By the Inn.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)
    #FUNKTSIOONID

    def redrawWindow():
        screen.blit(bg, (0, 0))
        player.control(screen)
        pygame.display.flip()

    tegelane = "Poiss"
    #Tegelase valik?
    #ANIMEERIMINE

#vajalikud pildid võetud kaustast
    if tegelane == "Tüdruk":
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
    elif tegelane == "Poiss":
        walkLeft = [pygame.image.load("characters/poiss_left/p_left1.png"),pygame.image.load("characters/poiss_left/p_left2.png"),
                        pygame.image.load("characters/poiss_left/p_left3.png"),pygame.image.load("characters/poiss_left/p_left4.png")]
        walkRight = [pygame.image.load("characters/poiss_right/p_right1.png"), pygame.image.load("characters/poiss_right/p_right2.png"),
                        pygame.image.load("characters/poiss_right/p_right3.png"), pygame.image.load("characters/poiss_right/p_right4.png")]
        walkFront = [pygame.image.load("characters/poiss_front/p_front1.png"), pygame.image.load("characters/poiss_front/p_front2.png"),
                        pygame.image.load("characters/poiss_front/p_front3.png"), pygame.image.load("characters/poiss_front/p_front4.png")]
        walkBack = [pygame.image.load("characters/poiss_back/p_back1.png"), pygame.image.load("characters/poiss_back/p_back2.png"),
                        pygame.image.load("characters/poiss_back/p_back3.png"), pygame.image.load("characters/poiss_back/p_back4.png")]
        playerpilt = "characters/poiss_front/p_front1.png"
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
    sahver = sahver1
    köök = köök1

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
                if player.y < 1 and (player.x >= 562 and player.x<= 715):
                    player.y = 385
                    bg = magamistuba
                    uks.play()
                elif player.x < 5 and (player.y >= 320 and player.y <= 383):
                    bg = elutuba
                    player.x = 725
                    uks.play()
                    player.y = 300
            if bg == magamistuba:
                if player.y <= 80 and (player.x >= 544 and player.x <= 707):
                    bg = sahver
                    player.y = 433
                    uks.play()
                elif player.y > 385 and (player.x >= 544 and player.x<= 707):
                    bg = koridor
                    player.y = 2
                    uks.play()
            if bg == elutuba:
                if player.x > 730 and (player.y >= 274 and player.y <= 343):
                    bg = koridor
                    player.x =35
                    player.y = 360
                    uks.play()
                elif player.y <= 1 and (player.x >= 178 and player.x <= 230):
                    bg = köök
                    player.x = 254
                    player.y = 494
                    uks.play()
                elif player.y <= 150 and (player.x >= 410 and player.x <= 430):
                    bg = köök2
                    köök = köök2
                    player.x = 510
                    player.y = 484
                    uks.play()
            if bg == sahver:
                if player.x < 210 and (player.y > 216 and player.y < 260):
                    if sahver == sahver1:
                        uks.play()
                        bg = sahver2
                        sahver = sahver2
                if player.y > 435 and (player.x >= 545 and player.x <= 710):
                    bg = magamistuba
                    player.x = 600
                    player.y = 90
                    uks.play()
            if bg == köök:
                if player.y >= 505 and (player.x > 213 and player.x <= 290):
                    bg = elutuba
                    player.x = 204
                    player.y = 7
                    uks.play()
                    #köök
                elif player.y >= 490 and (player.x > 480 and player.x <= 520):
                    bg = elutuba
                    player.x = 420
                    player.y = 153
                    uks.play()
                    #salaruum
                    
            #KONTROLLID        
            
            if e.type == pygame.KEYDOWN: #Kui vajutatakse alla nuppu
                if e.key == pygame.K_UP: # and player.x > speed
                    player.vy -= player.speed
                    player.left = False
                    player.right = False
                    player.up = True
                    player.down = False
                    kõndimine.play(-1)
                    
                if e.key == pygame.K_DOWN:
                    player.vy += player.speed
                    player.left = False
                    player.right = False
                    player.up = False
                    player.down = True
                    kõndimine.play(-1)
                    
                if e.key == pygame.K_LEFT:
                    player.vx -= player.speed
                    player.left = True
                    player.right = False
                    player.up = False
                    player.down = False
                    kõndimine.play(-1)
                    
                if e.key == pygame.K_RIGHT:
                    player.vx += player.speed
                    player.left = False
                    player.right = True
                    player.up = False
                    player.down = False
                    kõndimine.play(-1)
                    
            if e.type == pygame.KEYUP: #kui enam ei vajutata seda
                if e.key == pygame.K_UP:
                    player.vy += player.speed
                    player.left = False
                    player.right = False
                    player.up = False
                    player.down = False
                    kõndimine.stop()
    #                 player.stayfront = False   
    #                 player.stayback = True
                   
                if e.key == pygame.K_DOWN:
                    player.vy -= player.speed
                    player.left = False
                    player.right = False
                    player.up = False
                    player.down = False
                    kõndimine.stop()
    #                 player.stayfront = True   
    #                 player.stayback = False
                    
                if e.key == pygame.K_LEFT:
                    player.vx += player.speed
                    player.left = False
                    player.right = False
                    player.up = False
                    player.down = False
                    kõndimine.stop()
                    
                if e.key == pygame.K_RIGHT:
                    player.vx -= player.speed
                    player.left = False
                    player.right = False
                    player.up = False
                    player.down = False
                    kõndimine.stop()
    #     color = bg.get_at((int(player.x), int(player.y)))
    #     print(color)
        #print(buttonspressed)
        #print(int(player.x), int(player.y))
        #asukoha kontrollimiseks
        dt = kell.tick()/500
        player.update(dt) #uuendame asukohta
        
        redrawWindow()
        screen.fill([255, 255, 255])
        
    pygame.quit()



pygame.init()
pygame.display.set_caption("Vöödinukk")
aken = pygame.display.set_mode([800, 600])
manager = pygame_gui.UIManager([800, 600])  # loome UIManager objekti

bglobby = pygame.image.load("Lobby.png")
bg = pygame.image.load("background.png")
#---music-------#

#---------------#

#------------------#
box = pygame.Rect((385, 230), (190, 80))
box2 = pygame.Rect((150,200),(500,200))
box3 = pygame.Rect((385, 300), (190, 80))
box4 = pygame.Rect((645, 200),(30, 30))
box5 = pygame.Rect((200,260),(330,35))
box6 = pygame.Rect((710,0),(90,35))
box7 = pygame.Rect((150,50),(500,200))
box8 = pygame.Rect((270,268),(250,20))
box9 = pygame.Rect((385, 370), (190, 80))
#------------------#
#----text-------#
t_settings = pygame_gui.elements.UITextBox("Settings",box2, manager)
t_settings.hide()
t_volume = pygame_gui.elements.UITextBox("Volume",box5, manager)
t_volume.hide()
#---------------#
#-------exit-----#
exit = pygame_gui.elements.UIButton(box4, "X", manager)
exit.hide()
#--------------#

#------lobby-------#
play = pygame_gui.elements.UIButton(box, "START", manager)
play.show()
credit = pygame_gui.elements.UIButton(box3, "CREDIT", manager)
credit.show()
guide = pygame_gui.elements.UIButton(box9,"GUIDE" ,manager)
väljundkast = pygame_gui.elements.UITextBox("Leia väljapääs<br>Kasuta nooleklahve et liikuda.", pygame.Rect((250, 300),(250, 100)), manager)
väljundkast.hide()
#-------------------#

#-----settings------#
settings = pygame_gui.elements.UIButton(box6, "Settings", manager)
settings.show()
liugur = pygame_gui.elements.UIHorizontalSlider(box8,50,(0,100),manager)
liugur.hide()
#-------------------#
#----credit-------#
credit_menu = pygame_gui.elements.UITextBox("""Credit<br> <br>Tegid:<br> <br>Robert Koor<br>Lisandra Sokk<br>Merit Hass<br>Aleksandra Spitsõna""",box2, manager)
credit_menu.hide()
#-----------------#


bgB =False

kell = pygame.time.Clock()
RUN = True
while RUN:
    dt = kell.tick()/1000
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            RUN = False
        if e.type == pygame.USEREVENT:
            if e.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if e.ui_element == play:
                    mäng()
            if e.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if e.ui_element == settings:
                    bgB = False
                    play.hide()
                    credit.hide()
                    settings.hide()
                    
                    t_settings.show()
                    t_volume.show()
                    liugur.show()
                    
                    if e.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                        if e.ui_element == liugur:
                            print("Music")
                            
                    exit.show()
            if e.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if e.ui_element == credit:
                    bgB = True
                    play.hide()
                    credit.hide()
                    settings.hide()
                    
                    exit.show()
                    credit_menu.show()
            if e.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if e.ui_element == exit:
                    bgB = False
                    play.show()
                    credit.show()
                    settings.show()
                    guide.show()
                    väljundkast.hide()
                    t_volume.hide()
                    t_settings.hide()
                    liugur.hide()
                    credit_menu.hide()
                    exit.hide()
            if e.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if e.ui_element == guide:
                    väljundkast.show()
                    play.hide()
                    credit.hide()
                    settings.hide()
                    guide.hide()
                    exit.show()
        manager.process_events(e)  # töötleb sündmusi
        
    aken.fill([255, 255, 255])
    
    if bgB:
        aken.blit(bg, (0, 0))
    else: 
        aken.blit(bglobby, (0, 0))
        
    manager.update(dt) #uuendame manager objekti
    manager.draw_ui(aken)  # joonistab UI elemendid aknasse
    pygame.display.flip()
pygame.quit()
