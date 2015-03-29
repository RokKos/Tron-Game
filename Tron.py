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
            if Polje[x][y] == 1:
                pygame.draw.rect(DISPLAYSURF, Rdeca,(tx,ty, CELLSIZE, CELLSIZE)) #rect(Surface, color, Rect, width=0) -> tko ga izpolnes
            elif Polje[x][y] == 2:
                pygame.draw.rect(DISPLAYSURF, Modra,(tx,ty, CELLSIZE, CELLSIZE))
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

def Veljaven(Polje, x,y, kamx, kamy):
	return ((x + kamx <= CELLWIDTH) and\
			 (x + kamx >= 0) and \
			 (y + kamy <= CELLHEIGHT) and\
			 (y + kamy >= 0) and\
			 (Polje[x + kamx][y + kamy] == 0))

def Premik(Polje, x, y, smerx, smery, vrednost):
	if(Veljaven(Polje, x, y, smerx, smery)):
		Polje[x+smerx][y+smery] = vrednost
		print x, y
		return Polje, x+smerx, y+smery
	else:
		return Polje, None, None

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
    igralec1sx = 0
    igralec1sy = 1 #premika se v desno
    igralec1x = 5
    igralec1y = 5
    igralec2sx = -1
    igralec2sy = 0 #premika se v levo
    igralec2x = 70
    igralec2y = 5
    while True: #main game loop
        ##############
        #Mechanicks
        if(igralec1x == None and igralec1y == None or igralec2x == None and igralec2y):
            print "Konec"
            break
        Polje, igralec1x, igralec1y = Premik(Polje, igralec1x, igralec1y, igralec1sx, igralec1sy, 1) #nova slika(nova generacija celic)
        Polje, igralec2x, igralec2y = Premik(Polje, igralec2x, igralec2y, igralec2sx, igralec2sy, 2) #nova slika(nova generacija celic)
        BarvajPolje(Polje)
        Narisi()
        pygame.display.update()
        FPSclock.tick(FPS)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                ###########################################
                #Igralec 1
            	if(event.key == K_DOWN):
            		igralec1sx = 0
            		igralec1sy = 1
            	elif(event.key == K_UP):
            		igralec1sx = 0
            		igralec1sy = -1
            	elif(event.key == K_LEFT):
            		igralec1sx = -1
            		igralec1sy = 0
            	elif(event.key == K_RIGHT):
            		igralec1sx = 1 
            		igralec1sy = 0
                ###########################################
                #Igralec 2
                if(event.key == K_s):
                    igralec2sx = 0
                    igralec2sy = 1
                elif(event.key == K_w):
                    igralec2sx = 0
                    igralec2sy = -1
                elif(event.key == K_a):
                    igralec2sx = -1
                    igralec2sy = 0
                elif(event.key == K_d):
                    igralec2sx = 1 
                    igralec2sy = 0
        
        
if __name__=='__main__':
    main()