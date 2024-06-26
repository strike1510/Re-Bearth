import pygame, sys , jeu.room11, jeu.room10 , menu.pause , math , jeu.fonction
def Jeuroom9(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR,CLOCK):
    testpause = False
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    
    background = pygame.transform.scale(pygame.image.load("jeu\\image\\room2\\bgfutur.png"), (LARGEUR, HAUTEUR))
    colision_background = pygame.transform.scale(pygame.image.load("jeu\\image\\room2\\CollisionMap.png"), (LARGEUR, HAUTEUR))
    screen.blit(colision_background, (0,0))
    clock = pygame.time.Clock()

    #TEST 
    rect_x = LARGEUR // 2
    rect_y = HAUTEUR // 2
    screen_x = 0
    screen_y = 0
    #background = pygame.image.load("jeu\\image\\background.jpg")

    player = pygame.Surface((dimmension_perso, dimmension_perso), pygame.SRCALPHA)
    player.fill(TRANSPARENT)
    player_rect = player.get_rect(center=(pos_player_x,pos_player_y))

    image_porte_close = pygame.image.load('jeu\\image\\room2\\porte_close.png')
    image_porte_open = pygame.image.load('jeu\\image\\room2\\porte_open.png')
    image_porte = image_porte_close
    porte = pygame.Surface((1920, 1080), pygame.SRCALPHA)
    porte.fill(TRANSPARENT)
    porte_rect = porte.get_rect(center=(960*LARGEUR/1920, 540*HAUTEUR/1080))

    #Image joueur :
    imagesbas = pygame.image.load("jeu\\image\\player\\futur1\\devant1.png")
    imageplayer = imagesbas
    
    with open('donnee\\sauvegarde.txt', 'r') as file:
        stocke = []
        for line in file:
            stocke.append(line.replace("\n",""))
    for i in range(len(stocke)):
        if stocke[i] == "Niveau de Quetes:":
            NivQuete = stocke[i+1].split(":")
        if stocke[i] == "Touches:":
            TOUCHE_ID = stocke[i+1].split(";")


    running = True
    last = "z"
    index_image = 0
    
    while running:
        key = pygame.key.get_pressed()
            
        
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2

        screen.blit(background, (screen_x, screen_y))
        screen.blit(image_porte, porte_rect)
        screen.blit(imageplayer, player_rect)

        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
        
        
        
        if jeu.fonction.EntryZone1920(player_rect.x,player_rect.y,15,715,0,815,HAUTEUR,LARGEUR):
            jeu.room11.Jeuroom11(screen,1750*LARGEUR/1920,770*HAUTEUR/1080,VITESSE, HAUTEUR,LARGEUR, CLOCK)
            running = False
        
        #print(colision_background.get_at((player_rect.x, player_rect.y)))
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        pressed_keys_indices = [i for i, v in enumerate(keys) if v]
        if len(pressed_keys_indices) > 0:
            binary_values = [bin(key_index) for key_index in pressed_keys_indices]
        else:
            binary_values = ['0']
        depinfo = jeu.fonction.deplacement(binary_values,key, player_rect, VITESSE, 1, colision_background, HAUTEUR, LARGEUR, last, index_image, 64)
        imageplayer = depinfo[0]
        last = depinfo[1]
        index_image = depinfo[2]
        
        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(9,player_rect.x,player_rect.y,screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False

        if 910 < player_rect.x < 1010 and 500 < player_rect.y < 520:
            image_porte = image_porte_open
            with open('donnee\\sauvegarde.txt', 'r') as file:
                stocke = []
                for line in file:
                    stocke.append(line.replace("\n",""))

            for i in range(len(stocke)):
                if stocke[i] == "Touches:":
                    TOUCHE_ID = stocke[i+1].split(";")
            if TOUCHE_ID[4] in binary_values:
                jeu.room10.Jeuroom10(screen, 975*LARGEUR/1920, 890*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR, CLOCK)
                running = False
        else:
            image_porte = image_porte_close

        clock.tick(CLOCK)
        

        
        pygame.display.flip()
        pygame.display.update()