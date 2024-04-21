import pygame, sys , jeu.room1 , menu.pause , math , jeu.fonction, time
def battle(screen,pos_player_x,pos_player_y,nombre_mob,IDmob,healthplayer, HAUTEUR,LARGEUR):
    testpause = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    dimmension_jaune = 60
    
    grille = pygame.image.load("jeu\\image\\combat\\grille.png")
    background = pygame.image.load("jeu\\image\\combat\\background\\bg1.png")
    clock = pygame.time.Clock()

    #TEST 
    rect_x = LARGEUR // 2
    rect_y = HAUTEUR // 2
    screen_x = 0
    screen_y = 0
    #background = pygame.image.load("jeu\\image\\background.jpg")
    background = pygame.transform.scale(background, (LARGEUR, HAUTEUR))

    player = pygame.Surface((dimmension_perso, dimmension_perso), pygame.SRCALPHA)
    player.fill(TRANSPARENT)

    #Image joueur :
    imagesbas = pygame.image.load("jeu\\image\\player\\devant.png")
    imageplayer = imagesbas

    running = True

    coo = [[0 for _ in range(16)] for _ in range(16)]
    for i in range (0 ,16):
        for j in range (0,16):
            coo[i][j] = (510*LARGEUR/1920)+i*60,(90*HAUTEUR/1080)+j*60
    
    j_liste = [pygame.Surface((dimmension_jaune, dimmension_jaune), pygame.SRCALPHA) for _ in range(49)]
    j_rect = [0 for _ in range(49)]
    for i in range(49):
        j_liste[i].fill(TRANSPARENT)
    
    mobcase_liste = [pygame.Surface((dimmension_jaune, dimmension_jaune), pygame.SRCALPHA) for _ in range(49)]
    m_rect = [0 for _ in range(9)]
    for i in range(9):
        mobcase_liste[i].fill(TRANSPARENT)
            
    cooplayerx = pos_player_x
    cooplayery = pos_player_y

    tempx , tempy = coo[cooplayerx][cooplayery]
    tempy -= 8*LARGEUR/1920
    

    
    imagesvide = pygame.image.load("jeu\\image\\combat\\vide.png")
    imagesjaune = pygame.image.load("jeu\\image\\combat\\casejaune.png")
    imagesrouge = pygame.image.load("jeu\\image\\combat\\caserouge.png")
    imagesattaque = pygame.image.load("jeu\\image\\combat\\attaque.png")
    
    IDarmes =0
    if IDarmes == 0:
        framearmes = 6
        imagesarmes = [pygame.image.load(f"jeu\\image\\combat\\objet\\epee\\epee{i}.png") for i in range(1, framearmes+1)]
    if IDmob == 0:
        framemob = 6
        imagesmob = [pygame.image.load(f"jeu\\image\\combat\\blob\\blob{i}.png") for i in range(1, framemob+1)]
        healthmob = 100
        mobattaque = 5
    maxhealthmob = healthmob
    maxhealthplayer = healthplayer
    green = (0, 200, 5)
    red = (240, 0, 0)
    orange = (200,130,30)
    def draw_health_bar(health,maxhealth,coox,cooy):
        coox = coox * 60 + 480 
        cooy = cooy * 60 + 60
        bar_length = 70
        bar_height = 10
        fill = (health / maxhealth) * bar_length
        outline_rect = pygame.Rect(coox - 5, cooy - 10, bar_length, bar_height)
        fill_rect = pygame.Rect(coox - 5, cooy - 10, fill, bar_height)
        if health/maxhealth < 0.3:
            pygame.draw.rect(screen, red, fill_rect)
        elif health/maxhealth < 0.7:
            pygame.draw.rect(screen, orange, fill_rect)
        else:
            pygame.draw.rect(screen, green, fill_rect)
        pygame.draw.rect(screen, BLACK, outline_rect, 2)
    def ennemi(pposx,pposy,eposx,eposy):
        if pposx < eposx:
            if pposx != eposx -1:
                resx = eposx -1
            else:
                resx = eposx
        elif pposx > eposx:
            if pposx != eposx +1:
                resx = eposx +1
            else:
                resx = eposx
        else:
            resx = eposx
        if pposy < eposy:
            if pposy != eposy -1:
                resy = eposy -1
            else:
                resy = eposy
        elif pposy > eposy:
            if pposy != eposy +1:
                resy = eposy +1
            else:
                resy = eposy
        else:
            resy = eposy
        
        return mob.get_rect(center=(coo[int(resx)][int(resy)]))

    mob = pygame.Surface((dimmension_jaune, dimmension_jaune), pygame.SRCALPHA)
    mob.fill(TRANSPARENT)
    mob_rect = mob.get_rect(center=(coo[15][15]))

    armesplayer = pygame.Surface((dimmension_perso, dimmension_perso), pygame.SRCALPHA)
    armesplayer.fill(TRANSPARENT)
    armesplayer_rect = armesplayer.get_rect(center=(coo[0][0]))

    degat = 10    
    attaque_sur_joueur = False   
    action = False
    frame = 0
    tempo_pour_frame = 0
    attaque_sur_mob = False
    _Itemp = 0
    while running:
        key = pygame.key.get_pressed()
        screen.fill((255,255,255))
            
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2
        screen.blit(background, (screen_x, screen_y))
        screen.blit(grille, (screen_x, screen_y))
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
        player_rect = player.get_rect(center=(coo[cooplayerx][cooplayery]))
        xtemp1,ytemp1 = coo[cooplayerx][cooplayery]
        armesplayer_rect = armesplayer.get_rect(center=(xtemp1 + 35,ytemp1 - 30))
        
        if action and attaque_sur_joueur:
            healthplayer -= mobattaque
            action = False
            attaque_sur_joueur = False
        
        valeur_temp = 0
        for i in range(cooplayerx-3, cooplayerx+4):
            for k in range(cooplayery-3, cooplayery+4):
                if ((cooplayerx-3 == i or cooplayerx+3 == i) and cooplayery == k) or ((cooplayerx-2 == i or cooplayerx+2 == i) and cooplayery-2 < k < cooplayery+2) or ((cooplayerx-1 == i or cooplayerx+1 == i) and cooplayery-3 < k < cooplayery+3) or (cooplayerx == i and cooplayery != k):
                    if i >= 0 and i < 16 and k >= 0 and k < 16:
                        if i == (mob_rect.x- 480)/60 and k == (mob_rect.y-60)/60:
                            j_rect[valeur_temp] = j_liste[valeur_temp].get_rect(center=(coo[i][k]))
                            screen.blit(imagesattaque, j_rect[valeur_temp])
                        else:
                            j_rect[valeur_temp] = j_liste[valeur_temp].get_rect(center=(coo[i][k]))
                            screen.blit(imagesjaune, j_rect[valeur_temp])
                    else:
                        j_rect[valeur_temp] = j_liste[valeur_temp].get_rect(center=(5000,5000))
                        screen.blit(imagesvide, j_rect[valeur_temp])
                else:
                    j_rect[valeur_temp] = j_liste[valeur_temp].get_rect(center=(5000,5000))
                    screen.blit(imagesvide, j_rect[valeur_temp])
                valeur_temp += 1
        
        cooxmob = int((mob_rect.x- 480)/60)
        cooymob = int((mob_rect.y-60)/60)
        
        clock.tick(30)
        action = False
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    for i in range (49):
                        if j_rect[i].collidepoint(event.pos):
                            action = True
                            if int((j_rect[i].x - 480)/60) == cooxmob and int((j_rect[i].y - 60)/60) == cooymob:
                                healthmob -= degat
                                attaque_sur_mob = True
                                mob_rect = ennemi(cooplayerx,cooplayery,(mob_rect.x- 480)/60,(mob_rect.y-60)/60)
                            else:
                                cooplayerx = int((j_rect[i].x - 480)/60)
                                cooplayery = int((j_rect[i].y - 60)/60)
                                mob_rect = ennemi(cooplayerx,cooplayery,(mob_rect.x- 480)/60,(mob_rect.y-60)/60)
        valeur_tempo = 0
        mouse_x, mouse_y = pygame.mouse.get_pos() 
        if mouse_x > mob_rect.x and mouse_x < mob_rect.x +60 and mouse_y > mob_rect.y and mouse_y < mob_rect.y +60:
            for j in range(cooxmob-1, cooxmob+2):
                for l in range(cooymob-1, cooymob+2):
                    if j >= 0 and j < 16 and l >= 0 and l < 16:
                        if cooxmob == j and cooymob == l:
                            m_rect[valeur_tempo] = mobcase_liste[valeur_tempo].get_rect(center=(5000,5000))
                            screen.blit(imagesvide, m_rect[valeur_tempo])
                        else:
                            m_rect[valeur_tempo] = mobcase_liste[valeur_tempo].get_rect(center=(coo[j][l]))
                            screen.blit(imagesrouge, m_rect[valeur_tempo])
                            draw_health_bar(healthmob,maxhealthmob,cooxmob,cooymob)
                    else:
                        m_rect[valeur_tempo] = mobcase_liste[valeur_tempo].get_rect(center=(5000,5000))
                        screen.blit(imagesvide, m_rect[valeur_tempo])
                    if valeur_tempo <8:
                        valeur_tempo += 1
        for j in range(cooxmob-1, cooxmob+2):
            for l in range(cooymob-1, cooymob+2):
                if j >= 0 and j < 16 and l >= 0 and l < 16:
                    if cooplayerx == j and cooplayery == l:
                        attaque_sur_joueur = True
        draw_health_bar(healthplayer,maxhealthplayer,cooplayerx,cooplayery)
        screen.blit(imageplayer, player_rect)
        if attaque_sur_mob and _Itemp < framearmes-1:
            _Itemp+=1
            screen.blit(imagesarmes[_Itemp],armesplayer_rect)
        else:
            attaque_sur_mob = False
            _Itemp = 0
            screen.blit(imagesarmes[0],armesplayer_rect)
        if nombre_mob == 1:
            if tempo_pour_frame > 30:
                tempo_pour_frame =0
                if frame < framemob -1:
                    frame +=1
                else:
                    frame = 0
                    
            else:
                tempo_pour_frame += 1
            screen.blit(imagesmob[frame], mob_rect)
        

        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False
        

        if nombre_mob == 1:
            if healthmob <= 0:
                running = False
        pygame.display.flip()
        pygame.display.update() 