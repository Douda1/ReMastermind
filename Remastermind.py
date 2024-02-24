import pygame
import random
from sys import exit
import time

pygame.init()
screen = pygame.display.set_mode((1000,800))
mouse_pos = pygame.mouse.get_pos()
clock = pygame.time.Clock()
pygame.display.set_caption('Button Demo')
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
#----------------------------------------------------   

                    
#----------------------------------------------------
decaY = -15
decaX = -100

+ decaY

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

class Button():
    def __init__(self, x, y, image, val):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.val = val
        self.appui = False
        
    def draw(self):
        global CodeNumber
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.appui == False:
                self.appui = True
                Completion[CodeNumber] = self.val
                CodeNumber += 1
                print(Completion)
                if CodeNumber == 4:
                    CodeNumber = 0
                    
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.appui = False
        
        
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    

    
    
    
    screen.blit(Fond_Jaune,(0,0))
    screen.blit(Fond_Gris,Fond_Gris_Rect)
    screen.blit(Fond_Noir,Fond_Noir_Rect)
    Bouton1_.draw()
    Bouton2_.draw()
    Bouton3_.draw()
    Bouton4_.draw()
    Bouton5_.draw()
    Bouton6_.draw()
    Bouton7_.draw()
    Bouton8_.draw()
    Bouton9_.draw()
    pygame.display.update()
    clock.tick(60)