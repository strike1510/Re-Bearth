import pygame, math


#Image joueur :

# Skin 0 :
imagesdroite = [pygame.image.load(f"jeu\\image\\player\\droite{i}.png") for i in range(2, 6)]
imageshaut = [pygame.image.load(f"jeu\\image\\player\\derriere{i}.png") for i in range(2, 6)]
imagesbas = [pygame.image.load(f"jeu\\image\\player\\devant{i}.png") for i in range(2, 6)]
imagesgauche = [pygame.image.load(f"jeu\\image\\player\\gauche{i}.png") for i in range(2, 6)]

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
    elif touchepressed == [TOUCHE_ID[3]]:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.x < 1850*LARGEUR/1920:
                if len(imagesdroite) <= index_image:
                    index_image = 0
                PLAYER.move_ip(VITESSE, 0)
                imageplayer = imagesdroite[index_image]
                index_image = (index_image + 1) % len(imagesdroite)
                last = "d"
    elif [TOUCHE_ID[0]] == touchepressed:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.y > 10*HAUTEUR/1080:
                if len(imageshaut) <= index_image:
                    index_image = 0
                PLAYER.move_ip(0, -VITESSE)
                imageplayer = imageshaut[index_image]
                index_image = (index_image + 1) % len(imageshaut)
                last = "z"
    elif touchepressed == [TOUCHE_ID[2]]:
        if colision_background.get_at((PLAYER.x, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y+dimmension_perso)) not in collision_colors or colision_background.get_at((PLAYER.x+dimmension_perso, PLAYER.y)) not in collision_colors or colision_background.get_at((PLAYER.x, PLAYER.y+dimmension_perso)) not in collision_colors:
            if PLAYER.y < 1000*HAUTEUR/1080:
                if len(imagesbas) <= index_image:
                    index_image = 0
                PLAYER.move_ip(0, VITESSE)
                imageplayer = imagesbas[index_image]
                index_image = (index_image + 1) % len(imagesbas)
                last = "s"
        
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
        index_image = 0
        if last == "z":
            imageplayer = pygame.image.load(f"jeu\\image\\player\\derriere1.png")
        elif last == "s":
            imageplayer = pygame.image.load(f"jeu\\image\\player\\devant1.png")
        elif last == "q":
            imageplayer = pygame.image.load(f"jeu\\image\\player\\gauche1.png")
        elif last == "d":
            imageplayer = pygame.image.load(f"jeu\\image\\player\\droite1.png")
        elif last == "zq":
            imageplayer = pygame.image.load(f"jeu\\image\\player\\devant1.png")
        elif last == "zd":
            imageplayer = pygame.image.load(f"jeu\\image\\player\\devant1.png")
        elif last == "sq":
            imageplayer = pygame.image.load(f"jeu\\image\\player\\derriere1.png")
        elif last == "sd":
            imageplayer = pygame.image.load(f"jeu\\image\\player\\derriere1.png")
        else:
            print("Error")
        

        
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