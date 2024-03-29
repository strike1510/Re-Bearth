import pygame
WHITE = (255, 255, 255)
TRANSPARENT = (255, 255, 255, 20)
BLACK = (0, 0, 0)

def parametre(screen,HAUTEUR,LARGEUR):
    pause = True
    test = False

    PauseFond = pygame.Surface((440*LARGEUR/1920, 540*HAUTEUR/1080), pygame.SRCALPHA)
    PauseFond.fill(TRANSPARENT)
    PauseFond_rect = PauseFond.get_rect(center=(960*LARGEUR/1920, 500*HAUTEUR/1080))
    imagePauseFond = pygame.image.load('menu\\image\\option.png')
    image_PauseFond = pygame.transform.scale(imagePauseFond, (440*LARGEUR/1920, 540*HAUTEUR/1080))

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
    while pause == True:
        pygame.display.flip()
        key = pygame.key.get_pressed()
        pygame.draw.rect(PauseFond, (0, 0, 255), PauseFond.get_rect(), 3) 
        screen.blit(image_PauseFond, PauseFond_rect)
        
        if key[pygame.K_ESCAPE] == True:
            if test == True:
                pause = False
                return True
        else:
            test = True
        
        
        pos_x = pygame.mouse.get_pos()
        newx, y = pygame.mouse.get_pos()

        # Limiter la position du bouton dans la fenêtre
        if newx < 830*LARGEUR/1920:
            newx = 830*LARGEUR/1920
        elif newx > 1050*LARGEUR/1920:
            newx = 1050*LARGEUR/1920
        
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(x,y)
                    if x > 820*LARGEUR/1920 and x < 1100*LARGEUR/1920 and y > 275*HAUTEUR/1080 and y < 310*HAUTEUR/1080: 
                        bouton.deplacer(newx)
                    if 870*LARGEUR/1920 <= x <= 1045*LARGEUR/1920 and 670*HAUTEUR/1080 <= y <= 715*HAUTEUR/1080:
                        pause = False
                        return True
        bouton.afficher()
        clock.tick(60)