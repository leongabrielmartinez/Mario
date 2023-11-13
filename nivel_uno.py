from configuraciones import *
from Class_Personaje import * 
from Class_nivel import *

def crear_plataforma(visible,esPremio, tamaño,x, y, path="", ):
    plataforma = {}
    if visible:
        plataforma["superficie"] = pygame.image.load(path)
        plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"],tamaño)
    else:
        plataforma["superficie"] = pygame.Surface(tamaño)
    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y
    plataforma["premio"] = esPremio
    
    return plataforma


class NivelUno(Nivel):
    def __init__(self, pantalla:pygame.Surface):
        
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        #FONDO
        fondo = pygame.image.load("fondo.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))


        #ANIMACIONES
        diccionario_animaciones = {}
        diccionario_animaciones["Quieto"] = personaje_quieto
        diccionario_animaciones["Derecha"] = personaje_camina_derecha
        diccionario_animaciones["Izquierda"] = personaje_camina_izquierda
        diccionario_animaciones["Salta"] = personaje_salta

        diccionario_animaciones["Super_Derecha"] = super_mario_derecha
        diccionario_animaciones["Super_Izquierda"] = super_mario_izquierda
        diccionario_animaciones["Super_Quieto"] = super_mario_quieto
        diccionario_animaciones["Super_Salta"] = super_mario_salta


        #PLATAFORMAS 
        piso = crear_plataforma(False,False, (W,5), 0,733)#reposisionar
        plataforma_caño = crear_plataforma(True,False, (125,125), 250,608, "Caño(2).png")
        plataforma_invisible = crear_plataforma(False,False, (200,195), 735,542,"")
        plataforma_premio = crear_plataforma(False,True, (53,53),550,485, "")

        plataformas = [piso, plataforma_caño, plataforma_invisible, plataforma_premio]

        #MARIO
        mario = Personaje(diccionario_animaciones, (75,100), 0,500, 5) 
        #mario.rectangulo_principal.bottom = piso["rectangulo"].y #UBICAR A MARIO SOBRE EL PISO
        #mario.rectangulos["principal"].bottom = piso["rectangulo"].y

        #ENEMIGOS
        diccionario_animaciones = {"Izquierda":enemigo_camina, "aplasta":enemigo_aplasta}
        enemigo_uno = Enemigo(diccionario_animaciones, 500, (piso["rectangulo"].y - 50))
        enemigo_dos = Enemigo(diccionario_animaciones, 1000, (piso["rectangulo"].y - 50))

        d = {"aplasta":diccionario_animaciones["aplasta"]}
        reescalalar_imagenes(d,50,20)
        lista_enemigos = [enemigo_uno, enemigo_dos]

        #FLOR
        #TAREA AGREGAR ESTE COMPORTAMIENTO A UNA CLASE QUE SEA UNA CLASE QUE SEA PARA CREACION DE OBJETOS
        flor = {}
        flor["superficie"] = flor_fuego[0]
        flor["superficie"] = pygame.transform.scale(flor["superficie"], (50,50))
        flor["rectangulo"] = flor["superficie"].get_rect()
        #UBICAR LA FLOR
        flor["rectangulo"].midbottom = plataforma_premio["rectangulo"].midtop
        flor["descubierta"] = False
        flor["tocada"] = False
        super().__init__(pantalla, mario, plataformas, fondo)

