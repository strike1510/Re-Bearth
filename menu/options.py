import pygame, jeu.fonction
WHITE = (255, 255, 255)
TRANSPARENT = (255, 255, 255, 20)
BLACK = (0, 0, 0)

def parametre(screen,HAUTEUR,LARGEUR):
    pause = True
    test = False

    PauseFond = pygame.Surface((440*LARGEUR/1920, 540*HAUTEUR/1080), pygame.SRCALPHA)
    PauseFond.fill(TRANSPARENT)
    PauseFond_rect = PauseFond.get_rect(center=(960*LARGEUR/1920, 500*HAUTEUR/1080))
    imagePauseFond = jeu.fonction.redimensionner_image('menu\\image\\option.png', LARGEUR, HAUTEUR)
    bedit = pygame.Surface((50, 25), pygame.SRCALPHA)
    bedit.fill(TRANSPARENT)
    bedit1_rect = bedit.get_rect(center=(1050*LARGEUR/1920, 440*HAUTEUR/1080))
    bedit2_rect = bedit.get_rect(center=(1050*LARGEUR/1920, 475*HAUTEUR/1080))
    bedit3_rect = bedit.get_rect(center=(1050*LARGEUR/1920, 510*HAUTEUR/1080))
    bedit4_rect = bedit.get_rect(center=(1050*LARGEUR/1920, 545*HAUTEUR/1080))
    bedit5_rect = bedit.get_rect(center=(1050*LARGEUR/1920, 580*HAUTEUR/1080))
    bedit6_rect = bedit.get_rect(center=(1050*LARGEUR/1920, 615*HAUTEUR/1080))
    
    imageedit = pygame.image.load('menu\\image\\edit.png')
    image_PauseFond = pygame.transform.scale(imagePauseFond, (440*LARGEUR/1920, 540*HAUTEUR/1080))

    with open('donnee\\sauvegarde.txt', 'r') as file:
        stocke = []
        for line in file:
            stocke.append(line.replace("\n",""))


    for i in range(len(stocke)):
        if stocke[i] == "Touches:":
            TOUCHE_ID = stocke[i+1].split(";")

    class Bouton:
        def __init__(self):
            #690*LARGEUR/1600
            self.valeur = round(100*pygame.mixer.music.get_volume())
            self.rect = pygame.Rect((830 + ((1050*LARGEUR/1920)-(830*LARGEUR/1920))*pygame.mixer.music.get_volume())*LARGEUR/1920, 235*HAUTEUR/900, 40, 16)
            self.couleur = BLACK
            self.font = pygame.font.Font(None, 16)

        def afficher(self):
            pygame.draw.rect(screen, self.couleur, self.rect)
            texte = self.font.render(str(self.valeur), True, WHITE)
            screen.blit(texte, (self.rect.x + 20, self.rect.y + 5))

        def deplacer(self, pos_x):
            self.rect.x = pos_x
            if 830*LARGEUR/1920 >= self.rect.x:
                self.valeur = int(0)
            elif 1050*LARGEUR/1920 <= self.rect.x:
                self.valeur = int(100)
            else:
                self.valeur = int(round((((pos_x*LARGEUR/1920 - 830*LARGEUR/1920) / ((1050*LARGEUR/1920)-(830*LARGEUR/1920))))*100))
            pygame.mixer.music.set_volume(self.valeur/100)
    
    bouton = Bouton()
    clock = pygame.time.Clock()
    Bselection = 0
    while pause == True:
        pygame.display.flip()
        key = pygame.key.get_pressed()
        pygame.draw.rect(PauseFond, (0, 0, 255), PauseFond.get_rect(), 3) 
        screen.blit(image_PauseFond, PauseFond_rect)
        screen.blit(imageedit, bedit1_rect)
        screen.blit(imageedit, bedit2_rect)
        screen.blit(imageedit, bedit3_rect)
        screen.blit(imageedit, bedit4_rect)
        screen.blit(imageedit, bedit5_rect)
        screen.blit(imageedit, bedit6_rect)
        
        if key[pygame.K_ESCAPE] == True:
            if test == True:
                pause = False
                return True
        else:
            test = True
        
        
        newx, y = pygame.mouse.get_pos()

        # Limiter la position du bouton dans la fenêtre
        if newx < 830*LARGEUR/1920:
            newx = 830*LARGEUR/1920
        elif newx > 1050*LARGEUR/1920:
            newx = 1050*LARGEUR/1920
        
        
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x > 820*LARGEUR/1920 and x < 1100*LARGEUR/1920 and y > 275*HAUTEUR/1080 and y < 310*HAUTEUR/1080: 
                    bouton.deplacer(newx)
                if 870*LARGEUR/1920 <= x <= 1045*LARGEUR/1920 and 670*HAUTEUR/1080 <= y <= 715*HAUTEUR/1080:
                    pause = False
                    return True
                if bedit1_rect.collidepoint(event.pos):
                    Bselection = 1
                elif bedit2_rect.collidepoint(event.pos):
                    Bselection = 3
                elif bedit3_rect.collidepoint(event.pos):
                    Bselection = 2
                elif bedit4_rect.collidepoint(event.pos):
                    Bselection = 4
                elif bedit5_rect.collidepoint(event.pos):
                    Bselection = 5
                elif bedit6_rect.collidepoint(event.pos):
                    Bselection = 6
                else:
                    Bselection = 0

                    
           
            elif event.type == pygame.KEYDOWN:
                if Bselection > 0:
                    keys = pygame.key.get_pressed()
                    pressed_keys_indices = [i for i, v in enumerate(keys) if v]
                    if len(pressed_keys_indices) > 0:
                        binary_values = [bin(key_index) for key_index in pressed_keys_indices]
                    else:
                        binary_values = ['0']
                    print(f"Touche pressée : {binary_values[0]}")
                    print(TOUCHE_ID[Bselection-1])
                    TOUCHE_ID[Bselection-1] = str(binary_values[0])
                    testtemporaire = "Default"
                    with open('donnee\\sauvegarde.txt', 'w') as file:
                        for i in range (len(stocke)):
                            if testtemporaire == "Default":
                                text_a_ecrire = "{}\n".format(stocke[i])
                                if stocke[i] == "Touches:":
                                    testtemporaire = "T"
                                    file.write(text_a_ecrire)
                                else:
                                    file.write(text_a_ecrire)
                            elif testtemporaire == "T":
                                file.write("{};{};{};{};{};{}\n".format(TOUCHE_ID[0],TOUCHE_ID[1],TOUCHE_ID[2],TOUCHE_ID[3],TOUCHE_ID[4],TOUCHE_ID[5]))
                                testtemporaire = "Default"


        bouton.afficher()
        clock.tick(60)