import pygame
from pygame.locals import *
from configuraciones import *
from Class_Personaje import *
from modo import *
from Class_nivel import *
from Class_Enemigo import *
from nivel_uno import *


pygame.init()
W, H = 1000, 800
FPS = 18
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))
bandera = True


nivel_actual = NivelUno(PANTALLA)

while bandera:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            bandera = False

    nivel_actual.update(eventos)
    
    pygame.display.update()