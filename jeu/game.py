import pygame, sys , jeu.room1 , jeu.room2 , jeu.combat.battle, menu.pause , math , jeu.fonction
def LancementJeu(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR):
    testpause = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    
    background = pygame.image.load("jeu\\image\\background.jpg")
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
    porte_rect = porte.get_rect(center=(740*LARGEUR/1920, 865*HAUTEUR/1080))

    player = pygame.Surface((dimmension_perso, dimmension_perso), pygame.SRCALPHA)
    player.fill(TRANSPARENT)
    player_rect = player.get_rect(center=(pos_player_x,pos_player_y))

    #Image joueur :
    imagesbas = pygame.image.load("jeu\\image\\player\\devant.png")
    imageplayer = imagesbas

    image_porte_close = pygame.image.load('jeu\\image\\porte_close.png')
    image_porte_open = pygame.image.load('jeu\\image\\porte.png')
    image_porte = image_porte_close

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    running = True
    last = "s"
    index_image = 0
    
    while running:
        key = pygame.key.get_pressed()
            
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2
        screen.blit(background, (screen_x, screen_y))
        #screen.blit(colision_background, (screen_x, screen_y))
        #pygame.draw.rect(screen, (255, 0, 0), player)
        pygame.draw.rect(porte, (0, 0, 255), porte.get_rect(), 3) 
        screen.blit(image_porte, porte_rect)
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
        screen.blit(imageplayer, player_rect)
        
        portemaison = jeu.fonction.EntryZone1600(player_rect.x,player_rect.y,550,700,600,660,HAUTEUR,LARGEUR)
        if portemaison == True:
            image_porte = image_porte_open
            if key[pygame.K_SPACE] == True:
                jeu.room1.Jeuroom1(screen, 260*LARGEUR/1920, 960*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR)
                running = False
        else:
            image_porte = image_porte_close
        
        
        if jeu.fonction.EntryZone1920(player_rect.x,player_rect.y,1920,680,1835,825,HAUTEUR,LARGEUR):
            jeu.room2.Jeuroom2(screen, 150*LARGEUR/1920, 765*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR)
            #jeu.combat.battle.battle(screen,150*LARGEUR/1920, 765*HAUTEUR/1080, HAUTEUR,LARGEUR)
            running = False
        
        #print(colision_background.get_at((player_rect.x, player_rect.y)))
        depinfo = jeu.fonction.deplacement(key, player_rect, VITESSE, 0, colision_background, HAUTEUR, LARGEUR, last, index_image)
        imageplayer = depinfo[0]
        last = depinfo[1]
        
        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False

        
        clock.tick(30)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

        
        pygame.display.flip()
        pygame.display.update()