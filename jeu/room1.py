import pygame, sys , jeu.room1 , menu.pause , math , jeu.fonction
def Jeuroom1(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR):
    testpause = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    
    background = pygame.image.load("jeu\\image\\room1\\room.jpg")
    colision_background = pygame.image.load("jeu\\image\\room1\\roomCollision.png")
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

    player = pygame.Surface((dimmension_perso, dimmension_perso), pygame.SRCALPHA)
    player.fill(TRANSPARENT)
    player_rect = player.get_rect(center=(pos_player_x,pos_player_y))

    lettre = pygame.Surface((LARGEUR, HAUTEUR), pygame.SRCALPHA)
    lettre.fill(TRANSPARENT)
    imageslettre = [pygame.image.load(f"jeu\\image\\quete\\lettre_sceller.png"),pygame.image.load(f"jeu\\image\\quete\\lettre_open.png"),pygame.image.load(f"jeu\\image\\quete\\feuille0.png")]

    #Image joueur :
    imagesbas = pygame.image.load("jeu\\image\\player\\devant.png")
    imageplayer = imagesbas


    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)
    
    with open('donnee\\sauvegarde.txt', 'r') as file:
        stocke = []
        for line in file:
            stocke.append(line.replace("\n",""))

    for i in range(len(stocke)):
        if stocke[i] == "ID de Zone:":
            ZONE_ID = stocke[i+1].split(";")

    running = True
    last = "z"
    index_image = 0
    lettre_index = 0
    
    while running:
        key = pygame.key.get_pressed()
            
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2
        screen.blit(background, (screen_x, screen_y))
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
        screen.blit(imageplayer, player_rect)
        
        if player_rect.x > 600*LARGEUR/1920 and player_rect.x < 655*LARGEUR/1920 and player_rect.y < 750*HAUTEUR/1080 and player_rect.y > 715*HAUTEUR/1080:
            if key[pygame.K_SPACE] == True:
                jeu.game.LancementJeu(screen,740*LARGEUR/1920,940*HAUTEUR/1080,VITESSE, HAUTEUR,LARGEUR)
                running = False
        
        #print(colision_background.get_at((player_rect.x, player_rect.y)))
        
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 460<x<1450 and 315<y<760:
                    if lettre_index < 2:
                        lettre_index += 1
                    else:
                        testtemporaire = False
                        with open('donnee\\sauvegarde.txt', 'w') as file:
                            for i in range (len(stocke)):
                                if testtemporaire == False:
                                    text_a_ecrire = "{}\n".format(stocke[i])
                                    if stocke[i] == "ID de Zone:":
                                        testtemporaire = True
                                        file.write(text_a_ecrire)
                                    else:
                                        file.write(text_a_ecrire)
                                else:
                                    file.write("0;1068;455\n")
                                    testtemporaire = False
                        jeu.room1.Jeuroom1(screen, 1100*LARGEUR/1920, 485*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR)
                        running = False
        keys = pygame.key.get_pressed()
        pressed_keys_indices = [i for i, v in enumerate(keys) if v]
        if len(pressed_keys_indices) > 0:
            binary_values = [bin(key_index) for key_index in pressed_keys_indices]
        else:
            binary_values = ['0']
        depinfo = jeu.fonction.deplacement(binary_values,key, player_rect, VITESSE, 0, colision_background, HAUTEUR, LARGEUR, last, index_image)
        imageplayer = depinfo[0]
        last = depinfo[1]
        index_image = depinfo[2]
        if ZONE_ID[0] == "-1":
            screen.blit(imageslettre[lettre_index], (screen_x,screen_y))
            
        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(0,player_rect.x,player_rect.y,screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False
        clock.tick(30)
        pygame.display.flip()
        pygame.display.update()