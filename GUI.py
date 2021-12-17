import pygame, pygame_gui

pygame.init()
pygame.display.set_caption("Vöödinukk")
aken = pygame.display.set_mode([800, 600])
manager = pygame_gui.UIManager([800, 600])  # loome UIManager objekti

bglobby = pygame.image.load("Lobby.png")
bg = pygame.image.load("background.png")

box = pygame.Rect((385, 230), (190, 80))
box2 = pygame.Rect((385, 315), (190, 80))
box3 = pygame.Rect((385, 400), (190, 80))
box4 = pygame.Rect((10, 10),(30, 30))

play = pygame_gui.elements.UIButton(box, "START", manager)
play.show()
settings = pygame_gui.elements.UIButton(box2, "SETTINGS", manager)
settings.show()
credit = pygame_gui.elements.UIButton(box3, "CREDIT", manager)
credit.show()
exit = pygame_gui.elements.UIButton(box4, "X", manager)
exit.hide()

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
                    bgB = True
                    play.hide()
                    credit.hide()
                    settings.hide()
                    exit.show()
            if e.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if e.ui_element == credit:
                    bgB = True
                    
                    play.hide()
                    credit.hide()
                    settings.hide()
                    exit.show()
            if e.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if e.ui_element == exit:
                    bgB = False
                    play.show()
                    credit.show()
                    settings.show()
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