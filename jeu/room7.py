import pygame, sys , jeu.game , jeu.room5 , jeu.room8 , menu.pause , math , jeu.fonction
def Jeuroom7(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR):
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
    imagesbas = pygame.image.load("jeu\\image\\player\\devant.png")
    imageplayer = imagesbas
    

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    running = True
    last = "z"
    index_image = 0
    
    while running:
        key = pygame.key.get_pressed()
            
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2
        screen.blit(background, (screen_x, screen_y))
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
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
        depinfo = jeu.fonction.deplacement(binary_values,key, player_rect, VITESSE, 0, colision_background, HAUTEUR, LARGEUR, last, index_image)
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
            jeu.game.LancementJeu(screen, 100*LARGEUR/1920, 420*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR)
            running = False
        elif 0 < player_rect.x < 20 and 340 < player_rect.y < 500:
            jeu.room8.Jeuroom8(screen, 1800*LARGEUR/1920, 420*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR)
            running = False
        
        clock.tick(30)
        

        
        pygame.display.flip()
        pygame.display.update()