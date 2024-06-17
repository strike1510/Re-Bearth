import pygame, sys , jeu.room9 , menu.pause , math , jeu.fonction
def Jeuroom10(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR, CLOCK):
    testpause = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    
    background = pygame.image.load("jeu\\image\\room3\\bgfutur.png")
    colision_background = pygame.image.load("jeu\\image\\room3\\bg_collision.png")
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

    #Image joueur :
    imageplayer = pygame.transform.scale(pygame.image.load("jeu\\image\\player\\futur1\\derriere1.png"), (128, 128))

    #image pnj avec effet
    image_pnj = pygame.transform.scale(pygame.image.load('jeu\\image\\pnj\\pnj02\\pnj1.png'), (128, 128))
    image_excl = pygame.transform.scale(pygame.image.load('jeu\\image\\room3\\!.png'), (64, 64))
    image_montre = pygame.transform.scale(pygame.image.load('jeu\\image\\room3\\Montre_temporelle.png'), (960, 540))
    image_texte = pygame.transform.scale(pygame.image.load('jeu\\image\\room3\\texte.png'), (1920, 1080))
    
    running = True
    last = "z"
    index_image = 0

    set_cine_1 = 300
    test_texte_1 = 2

    with open('donnee\\sauvegarde.txt', 'r') as file:
        stocke = []
        for line in file:
            stocke.append(line.replace("\n",""))
    for i in range(len(stocke)):
        if stocke[i] == "Niveau de Quetes:":
            NivQuete = stocke[i+1].split(":")
        if stocke[i] == "Touches:":
            TOUCHE_ID = stocke[i+1].split(";")
    while running:
        key = pygame.key.get_pressed()
            
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2
        screen.blit(background, (screen_x, screen_y))
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
        
        
        
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
        

        #Animation du vieux qui donne la montre
        
        depinfo = jeu.fonction.deplacement(binary_values,key, player_rect, 18, 1, colision_background, HAUTEUR, LARGEUR, last, index_image, 128)
        imageplayer = depinfo[0]
        last = depinfo[1]
        index_image = depinfo[2]
        


        if test_texte_1 == 2 or test_texte_1 == 1:
            screen.blit(imageplayer, player_rect)
        else:
            screen.blit(image_pnj, (LARGEUR/2, 750))
            screen.blit(imageplayer, player_rect)
            screen.blit(image_texte, (0, 0))

        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(10,player_rect.x,player_rect.y,screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False
        if 840*LARGEUR/1920 < player_rect.x < 1045*LARGEUR/1920 and 900*HAUTEUR/1080 < player_rect.y < 1000*HAUTEUR/1080:
            with open('donnee\\sauvegarde.txt', 'r') as file:
                stocke = []
                for line in file:
                    stocke.append(line.replace("\n",""))
            for i in range(len(stocke)):
                if stocke[i] == "Touches:":
                    TOUCHE_ID = stocke[i+1].split(";")
            if TOUCHE_ID[4] in binary_values:
                jeu.room9.Jeuroom9(screen, 960*LARGEUR/1920, 600*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR, CLOCK)
                running = False
        clock.tick(CLOCK)
        

        
        pygame.display.flip()
        pygame.display.update()