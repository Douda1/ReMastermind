import pygame
import random
from sys import exit
import time

pygame.init()
screen = pygame.display.set_mode((1000,800))
mouse_pos = pygame.mouse.get_pos()
clock = pygame.time.Clock()

# ---------------------------------------------------
reponse = False
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Code1 = random.choice(liste)
Code2 = random.choice(liste)
Code3 = random.choice(liste)
Code4 = random.choice(liste)
CodeComplete = [Code1] + [Code2] + [Code3] + [Code4]
Completion = [0, 0, 0, 0]
print(CodeComplete) # a retirer plus tard
#----------------------------------------------------   

                    
#-----------------------------------------------------
decaY = 40
decaX = 0

+ decaY

Fond_Jaune = pygame.image.load('graphiques/png/FondV.png')
Fond_Gris = pygame.image.load('graphiques/png/FondMetal.png')
Fond_Gris_Rect = Fond_Gris.get_rect(center = (500,400))
Fond_Noir = pygame.image.load('graphiques/png/FondNoir.png')
Fond_Noir_Rect = Fond_Noir.get_rect(center = (500,150))
Bouton1 = pygame.image.load('graphiques/png/Bouton1.png')
Bouton1_Rect = Bouton1.get_rect(center = (275+ decaX,600+ decaY))
Bouton2 = pygame.image.load('graphiques/png/Bouton2.png')
Bouton2_Rect = Bouton2.get_rect(center = (500+ decaX,600+ decaY))
Bouton3 = pygame.image.load('graphiques/png/Bouton3.png')
Bouton3_Rect = Bouton3.get_rect(center = (725+ decaX,600+ decaY))
Bouton4 = pygame.image.load('graphiques/png/Bouton4.png')
Bouton4_Rect = Bouton4.get_rect(center = (275+ decaX,450+ decaY))
Bouton5 = pygame.image.load('graphiques/png/Bouton5.png')
Bouton5_Rect = Bouton5.get_rect(center = (500+ decaX,450+ decaY))
Bouton6 = pygame.image.load('graphiques/png/Bouton6.png')
Bouton6_Rect = Bouton6.get_rect(center = (725+ decaX,450+ decaY))
Bouton7 = pygame.image.load('graphiques/png/Bouton7.png')
Bouton7_Rect = Bouton7.get_rect(center = (275+ decaX,300+ decaY))
Bouton8 = pygame.image.load('graphiques/png/Bouton8.png')
Bouton8_Rect = Bouton8.get_rect(center = (500+ decaX,300+ decaY))
Bouton9 = pygame.image.load('graphiques/png/Bouton9.png')
Bouton9_Rect = Bouton9.get_rect(center = (725+ decaX,300+ decaY))

apui = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
    if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if Bouton1_Rect.collidepoint(mouse_pos) & apui == False:
                    apui = True
                    print("appuie")

    
    
    
    screen.blit(Fond_Jaune,(0,0))
    screen.blit(Fond_Gris,Fond_Gris_Rect)
    screen.blit(Fond_Noir,Fond_Noir_Rect)
    screen.blit(Bouton1,Bouton1_Rect)
    screen.blit(Bouton2,Bouton2_Rect)
    screen.blit(Bouton3,Bouton3_Rect)
    screen.blit(Bouton4,Bouton4_Rect)
    screen.blit(Bouton5,Bouton5_Rect)
    screen.blit(Bouton6,Bouton6_Rect)
    screen.blit(Bouton7,Bouton7_Rect)
    screen.blit(Bouton8,Bouton8_Rect)
    screen.blit(Bouton9,Bouton9_Rect)
    pygame.display.update()
    clock.tick(60)