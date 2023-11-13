import pygame
from modo import *
from Class_Personaje import *


class Nivel:#BASE PARA CONSTUIR NIVELES
    def __init__(self, pantalla, personaje_principal:Personaje, lista_plataformas, imagen_fondo):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
    
    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:#PRINTEAR LA UBICACION DEL CLIKEO EN PANTALLA
                print(evento.pos)
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        self.leer_inputs()
        self.actualizar_pantalla()
        

    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))

        for plataforma in self.plataformas:
            self._slave.blit(plataforma["superficie"], plataforma["rectangulo"])
            print(plataforma)

        #self.jugador.actualizar(self._slave, self.plataformas[0], self.plataformas)


    def leer_inputs(self):
        teclas = pygame.key.get_pressed()
    
        if teclas[pygame.K_RIGHT]:
            self.jugador  = "Derecha"
            if(teclas[pygame.K_SPACE]):
                self.jugador  = "Salta"

        elif teclas[pygame.K_LEFT]:
            self.jugador  = "Izquierda"
            if(teclas[pygame.K_SPACE]):
                self.jugador  = "Salta"

        elif(teclas[pygame.K_SPACE]):
            self.jugador  = "Salta"

        else:
            self.jugador   = "Quieto"


    def dibujar_rectangulos(self):
        if obtener_modo():
            for lado in self.jugador.rectangulos:
                pygame.draw.rect(self._slave, "blue", self.jugador.rectangulos[lado], 3)
            for plataforma in self.plataformas:
                pygame.draw.rect(self._slave, "red", plataforma["rectangulo"], 5)


