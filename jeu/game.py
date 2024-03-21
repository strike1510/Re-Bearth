import pygame, sys , jeu.room1 , menu.pause , math
def LancementJeu(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR):
    testpause = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    last = "z"
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
    colision_background = pygame.transform.scale(colision_background, (LARGEUR, HAUTEUR))

    collision_colors = [(206, 2, 207, 255), (0, 255, 0)]

    #porte = pygame.Rect((500, 500, 64, 64))
    porte = pygame.Surface((64, 64), pygame.SRCALPHA)
    porte.fill(TRANSPARENT)
    porte_rect = porte.get_rect(center=(740*LARGEUR/1920, 865*HAUTEUR/1080))

    player = pygame.Surface((dimmension_perso, dimmension_perso), pygame.SRCALPHA)
    player.fill(TRANSPARENT)
    player_rect = player.get_rect(center=(pos_player_x,pos_player_y))

    #Image joueur :
    imagesdroite = [pygame.image.load(f"jeu\\image\\player\\droite{i}.png") for i in range(1, 4)]
    imageshaut = pygame.image.load("jeu\\image\\player\\derriere.png")
    imagesbas = pygame.image.load("jeu\\image\\player\\devant.png")
    imagesgauche = pygame.image.load("jeu\\image\\player\\gauche.png")
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
    index_image = 1
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
        if player_rect.x > 550*LARGEUR/1600 and player_rect.x < 600*LARGEUR/1600 and player_rect.y < 700*HAUTEUR/900 and player_rect.y > 660*HAUTEUR/900:
            image_porte = image_porte_open
            if key[pygame.K_SPACE] == True:
                jeu.room1.Jeuroom1(screen, 260*LARGEUR/1920, 960*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR)
                running = False
        else:
            image_porte = image_porte_close
        
        #print(colision_background.get_at((player_rect.x, player_rect.y)))
            


        if (key[pygame.K_q] == True and key[pygame.K_z] == False and key[pygame.K_s] == False):
            if colision_background.get_at((player_rect.x, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y+dimmension_perso)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x, player_rect.y+dimmension_perso)) not in collision_colors:
                if player_rect.x > 10*LARGEUR/1920:
                    player_rect.move_ip(-VITESSE, 0)
                    imageplayer = imagesgauche
                    last = "q"
        elif key[pygame.K_d] == True and key[pygame.K_z] == False and key[pygame.K_s] == False:
            if colision_background.get_at((player_rect.x, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y+dimmension_perso)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x, player_rect.y+dimmension_perso)) not in collision_colors:
                if player_rect.x < 1800*LARGEUR/1920:
                    player_rect.move_ip(VITESSE, 0)
                    imageplayer = imagesdroite[index_image]
                    last = "d"
        elif key[pygame.K_z] == True and key[pygame.K_q] == False and key[pygame.K_d] == False:
            if colision_background.get_at((player_rect.x, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y+dimmension_perso)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x, player_rect.y+dimmension_perso)) not in collision_colors:
                if player_rect.y > 10*HAUTEUR/1080:
                    player_rect.move_ip(0, -VITESSE)
                    imageplayer = imageshaut
                    last = "z"
        elif key[pygame.K_s] == True and key[pygame.K_q] == False and key[pygame.K_d] == False:
            if colision_background.get_at((player_rect.x, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y+dimmension_perso)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x, player_rect.y+dimmension_perso)) not in collision_colors:
                if player_rect.y < 940*HAUTEUR/1080:
                    player_rect.move_ip(0, VITESSE)
                    imageplayer = imagesbas
                    last = "s"
        
        elif key[pygame.K_s] == True and key[pygame.K_q] == True and key[pygame.K_d] == False:
            if colision_background.get_at((player_rect.x, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y+dimmension_perso)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x, player_rect.y+dimmension_perso)) not in collision_colors:
                if player_rect.y < 1000*HAUTEUR/1080 and player_rect.x > 10*LARGEUR/1920:
                    player_rect.move_ip(0, round(VITESSE/math.sqrt(2)))
                    player_rect.move_ip(-round(VITESSE/math.sqrt(2)), 0)
                    imageplayer = imagesbas
                    last = "sq"
        
        elif key[pygame.K_s] == True and key[pygame.K_q] == False and key[pygame.K_d] == True:
            if colision_background.get_at((player_rect.x, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y+dimmension_perso)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x, player_rect.y+dimmension_perso)) not in collision_colors:
                if player_rect.y < 1000*HAUTEUR/1080 and player_rect.x < 1800*LARGEUR/1920:
                    player_rect.move_ip(0, round(VITESSE/math.sqrt(2)))
                    player_rect.move_ip(round(VITESSE/math.sqrt(2)), 0)
                    imageplayer = imagesbas
                    last = "sd"
        
        elif key[pygame.K_z] == True and key[pygame.K_q] == True and key[pygame.K_d] == False:
            if colision_background.get_at((player_rect.x, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y+dimmension_perso)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x, player_rect.y+dimmension_perso)) not in collision_colors:
                if player_rect.y > 10*HAUTEUR/1080 and player_rect.x > 10*LARGEUR/1920:
                    player_rect.move_ip(0, -round(VITESSE/math.sqrt(2)))
                    player_rect.move_ip(-round(VITESSE/math.sqrt(2)), 0)
                    imageplayer = imageshaut
                    last = "zq"
        
        elif key[pygame.K_z] == True and key[pygame.K_q] == False and key[pygame.K_d] == True:
            if colision_background.get_at((player_rect.x, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y+dimmension_perso)) not in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y)) not in collision_colors or colision_background.get_at((player_rect.x, player_rect.y+dimmension_perso)) not in collision_colors:
                if player_rect.y > 10*HAUTEUR/1080 and player_rect.x < 1800*LARGEUR/1920:
                    player_rect.move_ip(0, -round(VITESSE/math.sqrt(2)))
                    player_rect.move_ip(round(VITESSE/math.sqrt(2)), 0)
                    imageplayer = imageshaut
                    last = "zd"
        

        
        if colision_background.get_at((player_rect.x, player_rect.y)) in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y+dimmension_perso)) in collision_colors or colision_background.get_at((player_rect.x+dimmension_perso, player_rect.y)) in collision_colors or colision_background.get_at((player_rect.x, player_rect.y+dimmension_perso)) in collision_colors:
            if last == "z":
                player_rect.move_ip(0, VITESSE)
            elif last == "s":
                player_rect.move_ip(0, -VITESSE)
            elif last == "q":
                player_rect.move_ip(VITESSE, 0)
            elif last == "d":
                player_rect.move_ip(-VITESSE, 0)
            elif last == "zq":
                player_rect.move_ip(0, round(VITESSE/math.sqrt(2)))
                player_rect.move_ip(round(VITESSE/math.sqrt(2)), 0)
            elif last == "zd":
                player_rect.move_ip(0, round(VITESSE/math.sqrt(2)))
                player_rect.move_ip(-round(VITESSE/math.sqrt(2)), 0)
            elif last == "sq":
                player_rect.move_ip(0, -round(VITESSE/math.sqrt(2)))
                player_rect.move_ip(round(VITESSE/math.sqrt(2)), 0)
            elif last == "sd":
                player_rect.move_ip(0, -round(VITESSE/math.sqrt(2)))
                player_rect.move_ip(-round(VITESSE/math.sqrt(2)), 0)
            else:
                print("Error")
                    
        
        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False

        index_image = (index_image + 1) % len(imagesdroite)
        clock.tick(30)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

        
        pygame.display.flip()
        pygame.display.update()