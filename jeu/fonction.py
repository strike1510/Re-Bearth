import pygame, math, time

# Fonctionalité :
# appeller la fonction deplacement() pour stocker les infos de deplacement d'image
# Il y a 3 paramètres "PLAYER" correspond à l'entité créer donc le rectangle
# Ensuite il y a la vitesse qui est définie dans le main 
# Il y a 'perso' qui permet de mettre le skin du joueur (0 = par défaut)





def redimensionner_image(image_path, max_width, max_height):
    image = pygame.image.load(image_path)
    
    largeur, hauteur = image.get_size()
    ratio = min(max_width / largeur, max_height / hauteur)
    nouvelle_largeur = int(largeur * ratio)
    nouvelle_hauteur = int(hauteur * ratio)
    
    image_redimensionnee = pygame.transform.scale(image, (nouvelle_largeur, nouvelle_hauteur))
    
    return image_redimensionnee

def deplacement(touchepressed,key, PLAYER, VITESSE, perso, colision_background, HAUTEUR, LARGEUR, last, index_image, SCALE):
    # Skin 0 :
    coltest = False
    if perso == 0:
        imagesdroite = [pygame.image.load(f"jeu\\image\\player\\droite{i}.png") for i in range(2, 6)]
        imageshaut = [pygame.image.load(f"jeu\\image\\player\\derriere{i}.png") for i in range(2, 6)]
        imagesbas = [pygame.image.load(f"jeu\\image\\player\\devant{i}.png") for i in range(2, 6)]
        imagesgauche = [pygame.image.load(f"jeu\\image\\player\\gauche{i}.png") for i in range(2, 6)]
    elif perso == 1:
        imagesdroite = [pygame.image.load(f"jeu\\image\\player\\futur1\\droite{i}.png") for i in range(2, 5)]
        imageshaut = [pygame.image.load(f"jeu\\image\\player\\futur1\\derriere{i}.png") for i in range(2, 5)]
        imagesbas = [pygame.image.load(f"jeu\\image\\player\\futur1\\devant{i}.png") for i in range(2, 5)]
        imagesgauche = [pygame.image.load(f"jeu\\image\\player\\futur1\\gauche{i}.png") for i in range(2, 5)]
    dimmension_perso = SCALE
    with open('donnee\\sauvegarde.txt', 'r') as file:
        stocke = []
        for line in file:
            stocke.append(line.replace("\n",""))

    for i in range(len(stocke)):
        if stocke[i] == "Touches:":
            TOUCHE_ID = stocke[i+1].split(";")
    collision_colors = [(206, 2, 207, 255), (205, 2, 206, 255), (178, 0, 255, 255)]
    imageplayer = imagesbas[0]
    if touchepressed == [TOUCHE_ID[1]]:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.x > 10*LARGEUR/1920:
                if len(imagesgauche) <= index_image:
                    index_image = 0
                PLAYER.move_ip(-VITESSE, 0)
                imageplayer = imagesgauche[index_image]
                index_image = (index_image + 1) % len(imagesgauche)
                last = "q"
        else:
            coltest = True
    elif touchepressed == [TOUCHE_ID[3]]:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.x < 1850*LARGEUR/1920:
                if len(imagesdroite) <= index_image:
                    index_image = 0
                PLAYER.move_ip(VITESSE, 0)
                imageplayer = imagesdroite[index_image]
                index_image = (index_image + 1) % len(imagesdroite)
                last = "d"
        else:
            coltest = True
    elif [TOUCHE_ID[0]] == touchepressed:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.y > 10*HAUTEUR/1080:
                if len(imageshaut) <= index_image:
                    index_image = 0
                PLAYER.move_ip(0, -VITESSE)
                imageplayer = imageshaut[index_image]
                index_image = (index_image + 1) % len(imageshaut)
                last = "z"
        else:
            coltest = True
    elif touchepressed == [TOUCHE_ID[2]]:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.y < 1000*HAUTEUR/1080:
                if len(imagesbas) <= index_image:
                    index_image = 0
                PLAYER.move_ip(0, VITESSE)
                imageplayer = imagesbas[index_image]
                index_image = (index_image + 1) % len(imagesbas)
                last = "s"
        else:
            coltest = True
    elif TOUCHE_ID[1] in touchepressed and TOUCHE_ID[2] in touchepressed:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.y < 1000*HAUTEUR/1080 and PLAYER.x > 10*LARGEUR/1920:
                if len(imagesbas) <= index_image:
                    index_image = 0
                PLAYER.move_ip(0, round(VITESSE/math.sqrt(2)))
                PLAYER.move_ip(-round(VITESSE/math.sqrt(2)), 0)
                imageplayer = imagesbas[index_image]
                index_image = (index_image + 1) % len(imagesbas)
                last = "sq"
        else:
            coltest = True
    elif TOUCHE_ID[2] in touchepressed and TOUCHE_ID[3] in touchepressed:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.y < 1000*HAUTEUR/1080 and PLAYER.x < 1850*LARGEUR/1920:
                if len(imagesbas) <= index_image:
                    index_image = 0
                PLAYER.move_ip(0, round(VITESSE/math.sqrt(2)))
                PLAYER.move_ip(round(VITESSE/math.sqrt(2)), 0)
                imageplayer = imagesbas[index_image]
                index_image = (index_image + 1) % len(imagesbas)
                last = "sd"
        else:
            coltest = True
    elif TOUCHE_ID[1] in touchepressed and TOUCHE_ID[0] in touchepressed:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.y > 10*HAUTEUR/1080 and PLAYER.x > 10*LARGEUR/1920:
                if len(imageshaut) <= index_image:
                    index_image = 0
                PLAYER.move_ip(0, -round(VITESSE/math.sqrt(2)))
                PLAYER.move_ip(-round(VITESSE/math.sqrt(2)), 0)
                imageplayer = imageshaut[index_image]
                index_image = (index_image + 1) % len(imageshaut)
                last = "zq"
        else:
            coltest = True
    elif TOUCHE_ID[3] in touchepressed and TOUCHE_ID[0] in touchepressed:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.y > 10*HAUTEUR/1080 and PLAYER.x < 1850*LARGEUR/1920:
                if len(imageshaut) <= index_image:
                    index_image = 0
                PLAYER.move_ip(0, -round(VITESSE/math.sqrt(2)))
                PLAYER.move_ip(round(VITESSE/math.sqrt(2)), 0)
                imageplayer = imageshaut[index_image]
                index_image = (index_image + 1) % len(imageshaut)
                last = "zd"
        else:
            coltest = True
    else:
        index_image = 0
        if last == "z":
            if perso == 0:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\derriere1.png")
            elif perso == 1:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\futur1\\derriere1.png")
        elif last == "s":
            if perso == 0:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\devant1.png")
            elif perso == 1:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\futur1\\devant1.png")
        elif last == "q":
            if perso == 0:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\gauche1.png")
            elif perso == 1:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\futur1\\gauche1.png")
        elif last == "d":
            if perso == 0:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\droite1.png")
            if perso == 1:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\futur1\\droite1.png")
        elif last == "zq":
            if perso == 0:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\devant1.png")
            elif perso == 1:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\futur1\\devant1.png")
        elif last == "zd":
            if perso == 0:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\devant1.png")
            elif perso == 1:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\futur1\\devant1.png")
        elif last == "sq":
            if perso == 0:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\derriere1.png")
            elif perso == 1:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\futur1\\derriere1.png")
        elif last == "sd":
            if perso == 0:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\derriere1.png")
            elif perso == 1:
                imageplayer = pygame.image.load(f"jeu\\image\\player\\futur1\\derriere1.png")
        else:
            print("Error")
        

        
    if coltest == False:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) in collision_colors:
            if last == "z":
                PLAYER.move_ip(0, VITESSE)
            elif last == "s":
                PLAYER.move_ip(0, -VITESSE)
            elif last == "q":
                PLAYER.move_ip(VITESSE, 0)
            elif last == "d":
                PLAYER.move_ip(-VITESSE, 0)
            elif last == "zq":
                PLAYER.move_ip(0, round(VITESSE/math.sqrt(2)))
                PLAYER.move_ip(round(VITESSE/math.sqrt(2)), 0)
            elif last == "zd":
                PLAYER.move_ip(0, round(VITESSE/math.sqrt(2)))
                PLAYER.move_ip(-round(VITESSE/math.sqrt(2)), 0)
            elif last == "sq":
                PLAYER.move_ip(0, -round(VITESSE/math.sqrt(2)))
                PLAYER.move_ip(round(VITESSE/math.sqrt(2)), 0)
            elif last == "sd":
                PLAYER.move_ip(0, -round(VITESSE/math.sqrt(2)))
                PLAYER.move_ip(-round(VITESSE/math.sqrt(2)), 0)
            else:
                print("Error")
    
    imageplayer = pygame.transform.scale(imageplayer, (SCALE, SCALE))
    info = [imageplayer, last, index_image]

    return info


#fonction de detection de zone
# position x et y du joueur , puis zone x1 y1 et zone x2 y2, et la hauteur et largeur de l'écran  
def EntryZone1600(x,y,zonex1,zoney1,zonex2,zoney2,HAUTEUR,LARGEUR):
    if x > zonex1*LARGEUR/1600 and x < zonex2*LARGEUR/1600 and y < zoney1*HAUTEUR/900 and y > zoney2*HAUTEUR/900:
        return True
    else:
        return False

def EntryZone1920(x,y,zonex1,zoney1,zonex2,zoney2,HAUTEUR,LARGEUR):
    if x < zonex1*LARGEUR/1920 and x > zonex2*LARGEUR/1920 and y > zoney1*HAUTEUR/1080 and y < zoney2*HAUTEUR/1080:
        return True
    else:
        return False

def save(zone,posx,posy,addquette):
    if posx < 64:
        posx = 64
    else:
        if posx >1856:
            posx = 1856
    if posy < 64:
        posy = 64
    else:
        if posy > 1016:
            posy = 1016
    with open('donnee\\sauvegarde.txt', 'r') as file:
        stocke = []
        for line in file:
            stocke.append(line.replace("\n",""))
    quette = addquette.split(":")
    for k in range(len(stocke)):
        if stocke[k] == "Niveau de Quetes:":
            queteID = stocke[k+1].split(":")
    for j in range(0,5):
        queteID[j] = int(queteID[j])
        if quette[j] != 0:
            queteID[j]+= int(quette[j])
            
    with open('donnee\\sauvegarde.txt', 'w') as file:   
        for i in range(len(stocke)):
            if stocke[i] == "Niveau de Quetes:":
                stocke[i+1] = "{}:{}:{}:{}:{}".format(queteID[0],queteID[1],queteID[2],queteID[3],queteID[4])
            elif stocke[i] == "ID de Zone:" and zone != '-2':
                stocke[i+1] = "{};{};{}".format(zone,posx,posy)
            text_a_ecrire = "{}\n".format(stocke[i])
            print
            file.write(text_a_ecrire)

def chargement(screen,temp):
    if temp == 1:
        imagesload = [pygame.transform.scale(pygame.image.load(f"jeu\\image\\load\\load1\\load{i}.png"), (1920,1080)) for i in range(1, 5)]
        for i in range(0,4):
            screen.blit(imagesload[i], (0,0))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(1)
    elif temp ==2:
        imagesload = pygame.transform.scale(pygame.image.load(f"jeu\\image\\room7\\maya1.png"), (1920,1080))
        screen.blit(imagesload, (0,0))
        pygame.display.update()
        pygame.display.flip()
    elif temp ==3:
        imagesload = pygame.transform.scale(pygame.image.load(f"jeu\\image\\room7\\maya2.png"), (1920,1080))
        screen.blit(imagesload, (0,0))
        pygame.display.update()
        pygame.display.flip()
    elif temp ==4:
        imagesload = pygame.transform.scale(pygame.image.load(f"jeu\\image\\room7\\maya3.png"), (1920,1080))
        screen.blit(imagesload, (0,0))
        pygame.display.update()
        pygame.display.flip()