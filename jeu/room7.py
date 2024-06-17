import pygame, sys , jeu.game , jeu.room5 , jeu.room8 , menu.pause , math , jeu.fonction
def Jeuroom7(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR,CLOCK):
    testpause = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    
    background = pygame.image.load("jeu\\image\\room7\\map_03.png")
    colision_background = pygame.image.load("jeu\\image\\room7\\map_03col.png")
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
    imagesbas = pygame.image.load("jeu\\image\\player\\devant1.png")
    imageplayer = imagesbas
    imagepnj = pygame.image.load("jeu\\image\\pnj\\pnj03\\pnj1.png")

    with open('donnee\\sauvegarde.txt', 'r') as file:
        stocke = []
        for line in file:
            stocke.append(line.replace("\n",""))

    for i in range(len(stocke)):
        if stocke[i] == "Niveau de Quetes:":
            NivQuete = stocke[i+1]

    running = True
    last = "z"
    index_image = 0
    
    while running:
        key = pygame.key.get_pressed()
            
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2
        screen.blit(background, (screen_x, screen_y))
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
        
        
        if NivQuete[0] == '1':
            screen.blit(imagepnj, (1060, 340))


        screen.blit(imageplayer, player_rect)
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
                testquit = menu.pause.Pause(7,player_rect.x,player_rect.y,screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False
        
        
        if 1840 < player_rect.x < 1900 and 330 < player_rect.y < 460:
            jeu.game.LancementJeu(screen, 100*LARGEUR/1920, 420*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR, CLOCK)
            running = False
        elif 0 < player_rect.x < 20 and 340 < player_rect.y < 500:
            jeu.room8.Jeuroom8(screen, 1800*LARGEUR/1920, 420*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR, CLOCK)
            running = False
        
        clock.tick(CLOCK)
        

        
        pygame.display.flip()
        pygame.display.update()