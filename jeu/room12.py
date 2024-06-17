import pygame, sys , jeu.game , jeu.room11 , jeu.room7, jeu.room8 , menu.pause , math , jeu.fonction, jeu.combat.battle
def Jeuroom12(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR,CLOCK):
    testpause = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    
    backgroundbase = pygame.image.load("jeu\\image\\room7\\map_03futur.png")
    backgroundtexte = pygame.image.load("jeu\\image\\room7\\map_03textefutur.png")
    background = backgroundbase
    colision_background = pygame.image.load("jeu\\image\\room7\\map_03col.png")
    clock = pygame.time.Clock()
    image_monstre = [pygame.image.load(f"jeu\\image\\combat\\gblob\\gblob{i}.png") for i in range(1, 17)]
    imagepop = [pygame.image.load(f"jeu\\image\\combat\\pop{i}.png") for i in range(1, 4)]

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
    texte_affichage = 0
    donee = 0
    battle = False
    mob = image_monstre[0]
    imagemobframe = 0
    pop = 0
    while running:
        key = pygame.key.get_pressed()
            
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2
        screen.blit(background, (screen_x, screen_y))
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3) 
        if NivQuete[0] == '0' and NivQuete[1] == '1' and NivQuete[2] == '1' and NivQuete[4] == '1':
            if battle == False:
                screen.blit(mob, (1700,440)) 
        screen.blit(imageplayer, player_rect)
        
        with open('donnee\\sauvegarde.txt', 'r') as file:
            for line in file:
                if donee == 1:
                    TOUCHE_ID = line.split(";")
                if line.replace("\n","") == "Touches:":
                    donee = 1
                else:
                    donee = 0
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        pressed_keys_indices = [i for i, v in enumerate(keys) if v]
        if len(pressed_keys_indices) > 0:
            binary_values = [bin(key_index) for key_index in pressed_keys_indices]
        else:
            binary_values = ['0']
        if texte_affichage == 0 or texte_affichage == 1:
            depinfo = jeu.fonction.deplacement(binary_values,key, player_rect, VITESSE, 1, colision_background, HAUTEUR, LARGEUR, last, index_image, 64)
            imageplayer = depinfo[0]
            last = depinfo[1]
            index_image = depinfo[2]
        else:
            if NivQuete[0] == '0' and NivQuete[1] == '1' and NivQuete[2] == '1' and NivQuete[4] == '0':
                jeu.fonction.save(12,player_rect.x,player_rect.y,"0:0:0:0:1")
                NivQuete[4] = '1'
        if NivQuete[0] == '0' and NivQuete[1] == '1' and NivQuete[2] == '1' and NivQuete[4] == '1':
            if pop > 15:
                imagemobframe +=1
                if imagemobframe >= 149:
                    imagemobframe = 0 
                mob = image_monstre[imagemobframe%10]

            elif pop > 10:
                mob = imagepop[2]
                pop += 1
            elif pop > 5:
                mob = imagepop[1]
                pop += 1
            else:
                mob = imagepop[0]
                pop += 1

        keys = pygame.key.get_pressed()
        pressed_keys_indices = [i for i, v in enumerate(keys) if v]
        if len(pressed_keys_indices) > 0:
            binary_values = [bin(key_index) for key_index in pressed_keys_indices]
        else:
            binary_values = ['0']
        
        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(12,player_rect.x,player_rect.y,screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False
        if 1840 < player_rect.x < 1900 and 330 < player_rect.y < 460:
            if NivQuete[0] != '0' and NivQuete[1] != '1' and NivQuete[2] != '1' and NivQuete[4] != '1':
                jeu.room11.Jeuroom11(screen, 100*LARGEUR/1920, 420*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR, CLOCK)
                running = False
        elif 1650 < player_rect.x < 1740 and 385 < player_rect.y < 500:
            if battle == False and NivQuete[0] == '0' and NivQuete[1] == '1' and NivQuete[2] == '1' and NivQuete[4] == '1':
                battle = jeu.combat.battle.battle(screen,0, 0,1,1,100,HAUTEUR,LARGEUR)
                running = False
                if battle:
                    jeu.fonction.save(7,pos_player_x,pos_player_y,"1:-1:-1:0:-1")
                    jeu.room7.Jeuroom7(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR,CLOCK)
                else:
                    Jeuroom12(screen, pos_player_x, pos_player_y, VITESSE, HAUTEUR, LARGEUR, CLOCK)
                    
        elif 0 < player_rect.x < 120 and 340 < player_rect.y < 500:
            if int(NivQuete[1]) > 1:
                jeu.room8.Jeuroom8(screen, 1800*LARGEUR/1920, 420*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR, CLOCK)
                running = False
            else:
                if TOUCHE_ID[4] in binary_values:
                    if texte_affichage == 0 or texte_affichage == 1:
                        background = backgroundtexte
                        texte_affichage = 1
                    else:
                        if texte_affichage == 2:
                            background = backgroundbase
                            texte_affichage = 3
                else:
                    if texte_affichage == 1:
                        texte_affichage = 2
                    if texte_affichage == 3:
                        texte_affichage = 0

        clock.tick(CLOCK)
        
        if NivQuete[0] == '0' and NivQuete[1] == '1' and NivQuete[2] == '1' and NivQuete[4] == '1' and battle:
            NivQuete[4] = '2'

        
        pygame.display.flip()
        pygame.display.update()