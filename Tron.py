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