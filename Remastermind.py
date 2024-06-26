import pygame
import random
from sys import exit
import time

pygame.init()
screen = pygame.display.set_mode((1000,800))
mouse_pos = pygame.mouse.get_pos()
clock = pygame.time.Clock()
pygame.display.set_caption('ReMastermind')
# ---------------------------------------------------
reponse = False
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Code1 = random.choice(liste)
Code2 = random.choice(liste)
Code3 = random.choice(liste)
Code4 = random.choice(liste)
CodeComplete = [Code1] + [Code2] + [Code3] + [Code4]
Completion = [0, 0, 0, 0]
CodeNumber = 0
print(CodeComplete) # a retirer plus tard
coul = [(0, 254, 0), (0, 254, 0), (0, 254, 0), (0, 254, 0)]
#----------------------------------------------------   
NombreTourPos = [8,12,9,10,11,7]
NombreTour = random.choice(NombreTourPos)
fin = False
relai = 0
Ya = False
#----------------------------------------------------
decaY = -15
decaX = -100


Fond_Jaune = pygame.image.load('graphiques/png/FondV.png').convert_alpha()
Fond_Gris = pygame.image.load('graphiques/png/FondMetal.png').convert_alpha()
Fond_Gris_Rect = Fond_Gris.get_rect(center = (500,400))
Fond_Noir = pygame.image.load('graphiques/png/FondNoir.png').convert_alpha()
Fond_Noir_Rect = Fond_Noir.get_rect(center = (500,150))
Bouton1 = pygame.image.load('graphiques/png/Bouton1.png').convert_alpha()
Bouton2 = pygame.image.load('graphiques/png/Bouton2.png').convert_alpha()
Bouton3 = pygame.image.load('graphiques/png/Bouton3.png').convert_alpha()
Bouton4 = pygame.image.load('graphiques/png/Bouton4.png').convert_alpha()
Bouton5 = pygame.image.load('graphiques/png/Bouton5.png').convert_alpha()
Bouton6 = pygame.image.load('graphiques/png/Bouton6.png').convert_alpha()
Bouton7 = pygame.image.load('graphiques/png/Bouton7.png').convert_alpha()
Bouton8 = pygame.image.load('graphiques/png/Bouton8.png').convert_alpha()
Bouton9 = pygame.image.load('graphiques/png/Bouton9.png').convert_alpha()
LaFont = pygame.font.Font('font/digital.ttf',50) # je fait charger la font
son1 = pygame.mixer.Sound('Son/sound1.mp3')
son2 = pygame.mixer.Sound('Son/sound2.mp3')
son3 = pygame.mixer.Sound('Son/sound3.mp3')
son4 = pygame.mixer.Sound('Son/sound4.mp3')
son5 = pygame.mixer.Sound('Son/sound5.mp3')
BgMusique = pygame.mixer.Sound('Son/Brain Dance.mp3')
pygame.mixer.init(frequency=1)
BgMusique.set_volume(0.3)
BgMusique.play(loops = -1)
son = [son1,son2,son3,son4,son5]

class Button():
    def __init__(self, x, y, image, val):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.val = val
        self.appui = False
        
    def draw(self):
        global CodeNumber, reponse, NombreTour, Completion, relai
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.appui == False:
                self.appui = True
                Completion[CodeNumber] = self.val
                CodeNumber += 1
                random.choice(son).play()
                print(Completion)
                if CodeComplete == Completion :
                    reponse = True
                relai = 0
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.appui = False

def Couleurs():
    global coul
    for loop in range(4):
        if Completion[loop] == CodeComplete[loop]:
            coul[loop] = 'Green'
    for loop in range(4):
        for i in range(4):
            if Completion[loop] == CodeComplete[i] and coul[i] != 'Green' :
                coul[loop] = 'Orange'
    for loop in range(4):
        if coul[loop] != 'Green' and coul[loop] != 'Orange':
            coul[loop] = 'Red'

def javel():
    for loop in range(4):
        coul[loop] = (0, 254, 0)
            
def test():
    global CodeNumber, reponse, NombreTour, Completion, relai, Ya
    if CodeNumber == 4 and relai == 1:
        CodeNumber = 0
        Couleurs()
        Ya = True
    if CodeNumber == 4 and relai == 0:
        relai = 1


        

def retest():
    global CodeNumber, reponse, NombreTour, Completion, relai, Ya, BgMusique
    if Ya == True:
        NombreTour -=1

        tps1 = pygame.time.get_ticks()
        cooldown = False
        while cooldown == False:
            tps2 = pygame.time.get_ticks()
            if (tps2-tps1)>= 2000 :
                cooldown = True
        Completion = [0,0,0,0]
        Ya = False



#--------------------------------------------------------------------------------------------------

    



#--------------------------------------------------------------------------------------------------
Bouton1_ = Button(275+decaX,600+decaY,Bouton1, 1)
Bouton2_ = Button(500+decaX,600+decaY,Bouton2, 2)
Bouton3_ = Button(725+decaX,600+decaY,Bouton3, 3)
Bouton4_ = Button(275+decaX,450+decaY,Bouton4, 4)
Bouton5_ = Button(500+decaX,450+decaY,Bouton5, 5)
Bouton6_ = Button(725+decaX,450+decaY,Bouton6, 6)
Bouton7_ = Button(275+decaX,300+decaY,Bouton7, 7)
Bouton8_ = Button(500+decaX,300+decaY,Bouton8, 8)
Bouton9_ = Button(725+decaX,300+decaY,Bouton9, 9)


while True:
    screen.blit(Fond_Jaune,(0,0))
    screen.blit(Fond_Gris,Fond_Gris_Rect)
    screen.blit(Fond_Noir,Fond_Noir_Rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    if reponse == True and fin == False :
        print("gagné")
        fin = True
        
    
    if NombreTour == 0 and fin == False:
        print("perdu")
        fin = True
    test()
    chiffre_1_surf = LaFont.render(str(Completion[0]), False, coul[0])
    chiffre_1_rect = chiffre_1_surf.get_rect(center = (275,150))
    chiffre_2_surf = LaFont.render(str(Completion[1]), False, coul[1])
    chiffre_2_rect = chiffre_2_surf.get_rect(center = (400,150))
    chiffre_3_surf = LaFont.render(str(Completion[2]), False, coul[2])
    chiffre_3_rect = chiffre_3_surf.get_rect(center = (525,150))
    chiffre_4_surf = LaFont.render(str(Completion[3]), False, coul[3])
    chiffre_4_rect = chiffre_4_surf.get_rect(center = (650,150))

    

    Bouton1_.draw()
    Bouton2_.draw()
    Bouton3_.draw()
    Bouton4_.draw()
    Bouton5_.draw()
    Bouton6_.draw()
    Bouton7_.draw()
    Bouton8_.draw()
    Bouton9_.draw()
    
    

    screen.blit(chiffre_1_surf, chiffre_1_rect)
    screen.blit(chiffre_2_surf, chiffre_2_rect)
    screen.blit(chiffre_3_surf, chiffre_3_rect)
    screen.blit(chiffre_4_surf, chiffre_4_rect)
    test()
    
    
    pygame.display.update()
    retest()
    javel()
    clock.tick(60)