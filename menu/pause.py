import pygame, sys, time, menu.options
WHITE = (255, 255, 255)
TRANSPARENT = (255, 255, 255, 20)
BLACK = (0, 0, 0)

def Pause(zone,posx,posy,screen,HAUTEUR,LARGEUR):
    pause = True
    test = False

    PauseFond = pygame.Surface((440*LARGEUR/1920, 540*HAUTEUR/1080), pygame.SRCALPHA)
    PauseFond.fill(TRANSPARENT)
    PauseFond_rect = PauseFond.get_rect(center=(960*LARGEUR/1920, 500*HAUTEUR/1080))
    imagePauseFond = pygame.image.load('menu\\image\\pause.png')
    image_PauseFond = pygame.transform.scale(imagePauseFond, (440*LARGEUR/1920, 540*HAUTEUR/1080))

    with open('donnee\\sauvegarde.txt', 'r') as file:
        stocke = []
        for line in file:
            stocke.append(line.replace("\n",""))

    pygame.mixer.music.pause()
    while pause == True:
        pygame.display.flip()
        key = pygame.key.get_pressed()
        pygame.draw.rect(PauseFond, (0, 0, 255), PauseFond.get_rect(), 3) 
        screen.blit(image_PauseFond, PauseFond_rect)
        if key[pygame.K_ESCAPE] == True:
            if test == True:
                pause = False
                pygame.mixer.music.unpause()
                return True
        else:
            test = True
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 795*LARGEUR/1920 <= x <= 1125*LARGEUR/1920 and 645*HAUTEUR/1080 <= y <= 740*HAUTEUR/1080:
                        return False
                    elif 795*LARGEUR/1920 <= x <= 1125*LARGEUR/1920 and 515*HAUTEUR/1080 <= y <= 610*HAUTEUR/1080:
                        pause = False
                        pygame.mixer.music.unpause()
                        menu.options.parametre(screen,HAUTEUR,LARGEUR)
                        return True
                    elif 795*LARGEUR/1920 <= x <= 1125*LARGEUR/1920 and 255*HAUTEUR/1080 <= y <= 358*HAUTEUR/1080:
                        pause = False
                        pygame.mixer.music.unpause()
                        return True
                    elif 795*LARGEUR/1920 <= x <= 1125*LARGEUR/1920 and 390*HAUTEUR/1080 <= y <= 485*HAUTEUR/1080:
                        image_PauseFond = pygame.image.load('menu\\image\\pauses.png')
                        testtemporaire = "Default"
                        with open('donnee\\sauvegarde.txt', 'w') as file:
                            for i in range (len(stocke)):
                                if testtemporaire == "Default":
                                    text_a_ecrire = "{}\n".format(stocke[i])
                                    if stocke[i] == "ID de Zone:":
                                        testtemporaire = "ZONEID"
                                        file.write(text_a_ecrire)
                                    else:
                                        file.write(text_a_ecrire)
                                elif testtemporaire == "ZONEID":
                                    file.write("{};{};{}\n".format(zone,posx,posy))
                                    testtemporaire = "Default"