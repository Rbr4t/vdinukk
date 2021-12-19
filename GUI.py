from pygame import *
import pygame_gui, pygame

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
                    print("Töötab")
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
                    
                    t_volume.hide()
                    t_settings.hide()
                    liugur.hide()
                    credit_menu.hide()
                    exit.hide()
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
