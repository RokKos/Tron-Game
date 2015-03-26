##############################################
#INICIALIZACIJA
import pygame, sys
from pygame.locals import *
import random

FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 5
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size" #preveri ce se izidejo celice
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"
CELLWIDTH = WINDOWWIDTH / CELLSIZE # number of cells wide
CELLHEIGHT = WINDOWHEIGHT / CELLSIZE # Number of cells high

#Colours
BackgroundBarva = (0,0,0,0)
BARVE = []
Bela = (255,255,255,255)
BARVE.append(Bela)
Crna = (0,0,0,255)
BARVE.append(Crna)
Rdeca = (255,0,0,255)
BARVE.append(Rdeca)
Modra = (0,0,255,255)
BARVE.append(Modra)
Rumena = (255,255,0,255)
BARVE.append(Rumena)
Oranzna = (255,128,0,255)
BARVE.append(Oranzna)
Zelena = (0,255,0,255)
BARVE.append(Zelena)
Roza=(255,0,255, 255)
BARVE.append(Roza)
Vijolicna= (127,0,255,255)
BARVE.append(Vijolicna)

###############################################
#BARVANJE - DRAWING ON SURFACE

def BarvajPolje(Polje):
    for x in range(CELLWIDTH):
        for y in range(CELLHEIGHT):
            ty = y * CELLSIZE
            tx = x * CELLSIZE
            if Polje[x][y]:
                pygame.draw.rect(DISPLAYSURF, Crna,(tx,ty, CELLSIZE, CELLSIZE)) #rect(Surface, color, Rect, width=0) -> tko ga izpolnes
            else:
                pygame.draw.rect(DISPLAYSURF, Bela,(tx,ty, CELLSIZE, CELLSIZE))
    return None

def InitPolje():
    Polje = []
    for y in range (CELLWIDTH):
        tp = []
        for x in range (CELLHEIGHT):
            tp.append(0)
        Polje.append(tp)
    return Polje

#Narise crte
def Narisi():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, Crna, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, Crna, (0,y), (WINDOWWIDTH, y))


#################################################
#MAIN FUNKCIJA

def main():
    pygame.init()
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    FPSclock = pygame.time.Clock()
    pygame.display.set_caption('TRON')

    DISPLAYSURF.fill(Bela) #fills the screen white
    Polje = InitPolje() #naredi polje z samimi niclami
    BarvajPolje(Polje) #Obarva zaslon

    Narisi()
    pygame.display.update()
    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
if __name__=='__main__':
    main()