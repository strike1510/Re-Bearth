import pygame, sys , jeu.room12 , jeu.room9, jeu.room7 , jeu.room4, jeu.room6 , jeu.combat.battle, menu.pause , math , jeu.fonction
def Jeuroom11(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR,CLOCK):
    testpause = False
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    
    background = pygame.image.load("jeu\\image\\bgfutur.png")
    colision_background = pygame.image.load("jeu\\image\\CollisionMapProto.png")
    clock = pygame.time.Clock()

    #TEST 
    rect_x = LARGEUR // 2
    rect_y = HAUTEUR // 2
    screen_x = 0
    screen_y = 0
    #background = pygame.image.load("jeu\\image\\background.jpg")
    background = pygame.transform.scale(background, (LARGEUR, HAUTEUR))
    largeur_cible, hauteur_cible = background.get_size()
    colision_background = pygame.transform.scale(colision_background, (largeur_cible, hauteur_cible))

    #porte = pygame.Rect((500, 500, 64, 64))
    porte = pygame.Surface((64, 64), pygame.SRCALPHA)
    porte.fill(TRANSPARENT)

    player = pygame.Surface((dimmension_perso, dimmension_perso), pygame.SRCALPHA)
    player.fill(TRANSPARENT)
    player_rect = player.get_rect(center=(pos_player_x,pos_player_y))

    #Image joueur :
    imagesbas = pygame.image.load("jeu\\image\\player\\devant1.png")
    imageplayer = imagesbas

    
    with open('donnee\\sauvegarde.txt', 'r') as file:
        stocke = []
        for line in file:
            stocke.append(line.replace("\n",""))

    for i in range(len(stocke)):
        if stocke[i] == "ID de Zone:":
            ZONE_ID = stocke[i+1].split(";")
        if stocke[i] == "Niveau de Quetes:":
            NivQuete = stocke[i+1]

    running = True
    last = "s"
    index_image = 0
    framepnj = 0
    tempo = 0
    while running:
        key = pygame.key.get_pressed()
            
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2
        screen.blit(background, (screen_x, screen_y))
        #screen.blit(colision_background, (screen_x, screen_y))
        #pygame.draw.rect(screen, (255, 0, 0), player)
        if tempo > 29:
            tempo = 0
            if framepnj > 2:
                framepnj = 0
            else:
                framepnj +=1
        else:
            tempo += 1
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
        screen.blit(imageplayer, player_rect)
        
        action_terrain = NivQuete.split(":")
        if jeu.fonction.EntryZone1920(player_rect.x,player_rect.y,1920,680,1835,825,HAUTEUR,LARGEUR):
            jeu.room9.Jeuroom9(screen, 150*LARGEUR/1920, 815*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR, CLOCK)
            #jeu.combat.battle.battle(screen,0, 0,1,0,100,HAUTEUR,LARGEUR)
            running = False
        if jeu.fonction.EntryZone1920(player_rect.x,player_rect.y,1015,0,860,25,HAUTEUR,LARGEUR):
            if int(action_terrain[0]) > 0:
                #jeu.room4.Jeuroom4(screen, 950*LARGEUR/1920, 870*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR, CLOCK)
                running = False
        if jeu.fonction.EntryZone1920(player_rect.x,player_rect.y,1040,990,930,1100,HAUTEUR,LARGEUR):
            if int(action_terrain[0]) > 0:
                #jeu.room6.Jeuroom6(screen, 1000*LARGEUR/1920, 130*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR, CLOCK)
                running = False
        if jeu.fonction.EntryZone1920(player_rect.x,player_rect.y,20,330,0,470,HAUTEUR,LARGEUR):
            jeu.room12.Jeuroom12(screen, 1800*LARGEUR/1920, 440*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR, CLOCK)
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
        
        depinfo = jeu.fonction.deplacement(binary_values,key, player_rect, VITESSE, 0, colision_background, HAUTEUR, LARGEUR, last, index_image, 64)
        imageplayer = depinfo[0]
        last = depinfo[1]
        index_image = depinfo[2]
        
        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(11,player_rect.x,player_rect.y,screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False

        
        clock.tick(CLOCK)
        

        
        pygame.display.flip()
        pygame.display.update()