#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Banana manager
 
# Módulos

import pygame, time, random
from clases import *
from pygame.locals import *
from funciones import *
 
# Constantes

WIDTH = 1280
HEIGHT = 700
 
# Clases
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------

#Para cargar imágenes (aunque no lo crean)
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

#Para hacer un texto que cambia en pantalla
def texto(texto, posx, posy, tamano, color=(0, 0, 0)):  #Porque los negros son inferiores
    fuente = pygame.font.Font("DroidSans.ttf", tamano)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect
 
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Banana manager")

    background_image = load_image('Imagenes/fondo2.png')
    banana_image = load_image('Imagenes/banana.png', True)
    banner_image = load_image('Imagenes/banner.png', True)
    semilla_image = load_image('Imagenes/semilla.png', True)
    negro_image = load_image('Imagenes/negro.png', True)
    terreno_image = load_image('Imagenes/terreno.png', True)
    bot_semillas_image = load_image('Imagenes/bot_semillas.png', True)
    bot_negros_image = load_image('Imagenes/bot_negros.png', True)
    bot_tierras_image = load_image('Imagenes/bot_tierras.png', True)
    bot_manage_image = load_image('Imagenes/bot_manage.png', True)
    bot_status_image = load_image('Imagenes/bot_status.png', True)
    bot_minigame_image = load_image('Imagenes/bot_minigame.png', True)
    pant_status_image = load_image('Imagenes/pant_status.png', True)
    pant_minigame_image = load_image('Imagenes/pant_minigame.png', True)
    pant_manage_image = load_image('Imagenes/pant_manage.png', True)
    cuanto_comprar_image = load_image('Imagenes/cant_compra.png', True)

    #Tiempo
    start = time.clock()
    tprod = start
    tiempo = 0
    turno = 0
    #Cosas del save / recursos - objetos
    save = open("save.txt", "r")
    bananas = int(save.readline())
    semillas = int(save.readline())
    negros = int(save.readline())
    terrenos = int(save.readline())
    arboles = int(save.readline())
    granjas = int(save.readline())
    paises = int(save.readline())
    mundos = int(save.readline())
    produccion = 0
    cuanto = 0
    #Para salir
    mojon = "banana"
    #Control de botones grandes
    pantalla = 0
    #Cosas de mouse
    mouse_boton = pygame.mouse.get_pressed()
    pos_mouse = pygame.mouse.get_pos()
    anti_click = True
    #Botones
    cuanto1 = Boton(10,190,330,440,0)
    cuanto2 = Boton(10,190,460,570,1)
    cuanto3 = Boton(10,190,590,700,2)
    Manage = Boton(1085,1270,10,140,3)     
    #PRECIOS
    precio_semillas = 10
    precio_negros = 20
    precio_terrenos = 5
    #Calendario
    Mes=0
    Dia_anterior=0
    Anho = 2013
    Meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    while mojon == "banana":
        mouse_boton = pygame.mouse.get_pressed()
        pos_mouse = pygame.mouse.get_pos()
        #Cambiar producción
        produccion = 20 + 2*arboles + 15*granjas + 100*paises + 5000*mundos
        #Entregar bananas
        tiempo = int(time.clock() - start)
        turno = int(time.clock() - tprod)
        if turno == 1:
                bananas += produccion
                tprod = time.clock()
        #Pantalla
        pantalla = determinar_pantalla(pos_mouse,mouse_boton,anti_click,pantalla)
        #Clickear botones (deberíamos crear una clase botón que reciba posicion y tenga método clickeable)
        if cuanto1.click(pos_mouse, anti_click, mouse_boton[0]):
                if cuanto != 1:
                        cuanto = 1
                else:
                        cuanto = 0
                anti_click = False #tiene que ir acá para que funcione (1)
        if cuanto == 1:
               bananas,semillas,cuanto= cuanto1.clickbananas(pos_mouse,mouse_boton,anti_click,precio_semillas,semillas,bananas,cuanto)
        if cuanto2.click(pos_mouse, anti_click, mouse_boton[0]):
                if cuanto != 2:
                        cuanto = 2
                else:
                        cuanto = 0
                anti_click = False #tiene que ir acá para que funcione (2)
        if cuanto == 2:
                bananas,negros,cuanto = cuanto2.clickbananas(pos_mouse,mouse_boton,anti_click,precio_negros,negros,bananas,cuanto)
        if cuanto3.click(pos_mouse, anti_click, mouse_boton[0]):
                if cuanto != 3:
                        cuanto = 3
                else:
                        cuanto = 0
                anti_click = False #tiene que ir acá para que funcione (3)
        if cuanto == 3:
                bananas,terrenos,cuanto = cuanto3.clickbananas(pos_mouse,mouse_boton,anti_click,precio_terrenos,terrenos,bananas,cuanto)
        if mouse_boton[0] and 260 < pos_mouse[0] < 420 and 35 < pos_mouse[1] < 105 and anti_click and pantalla == 3 and semillas >= 10 and negros >= 2 and terrenos >= 1:
                arboles += 1
                semillas -= 10
                negros -= 2
                terrenos -= 1
        if mouse_boton[0] and 470 < pos_mouse[0] < 640 and 35 < pos_mouse[1] < 105 and anti_click and pantalla == 3 and semillas >= 50 and negros >= 5 and terrenos >= 5:
                granjas += 1
                semillas -= 50
                negros -= 5
                terrenos -= 5
        if mouse_boton[0] and 700 < pos_mouse[0] < 850 and 35 < pos_mouse[1] < 105 and anti_click and pantalla == 3 and semillas >= 500 and negros >= 20 and terrenos >= 10:
                paises += 1
                semillas -= 500
                negros -= 20
                terrenos -= 10
        if mouse_boton[0] and 875 < pos_mouse[0] < 1025 and 35 < pos_mouse[1] < 105 and anti_click and pantalla == 3 and semillas >= 5000 and negros >= 100 and terrenos >= 50:
                mundos += 1
                semillas -= 5000
                negros -= 100
                terrenos -= 50  
        if mouse_boton[0] and anti_click:
                anti_click = False
        if mouse_boton[0] and 810 < pos_mouse[0] < 1000 and 350 < pos_mouse[1] < 440 and pantalla == 1:
                bananas = 0
                terrenos = 0
                semillas = 0
                negros = 0
                arboles = 0
                granjas = 0
                paises = 0
                mundos = 0
                produccion  = 1
        if not mouse_boton[0]:
                anti_click = True
        #TIEMPO
        Dias,Mes,Anho = obtener_hora(tiempo,Anho)
        dia_actual, pos_dia = texto(str(Dias),330,665,30)
        mes_actual, pos_mes = texto(str(Meses[Mes]),440,665,30)
        anho_actual, pos_anho = texto(str(Anho),555,665,30)
        #Crear variables que cambian en pantalla                
        tiempo_actual, pos_tiempo_actual = texto(str(tiempo),120,250, 30)
        banana_usables, pos_banana = texto(str(bananas), 120,50, 30)
        semilla_usables, pos_semilla = texto(str(semillas), 120,100, 30)
        negro_usables, pos_negro = texto(str(negros), 120,150, 30)
        terreno_usables, pos_terreno = texto(str(terrenos), 120,200, 30)
        arbol_usables, pos_arbol = texto(str(arboles), 290,385, 30)
        granja_usables, pos_granja = texto(str(granjas), 520,385, 30)
        pais_usables, pos_pais = texto(str(paises), 735,385, 30)
        mundo_usables, pos_mundo = texto(str(mundos), 930,385, 30)
        #Dibuja en la pantalla las cosas en orden (más grandes primero)
        #Fondo (debe variar más adelante dependiendo de la cantidad de bananas)
        screen.blit(background_image, (0,0))
        #Banana banner holy shit
        screen.blit(banner_image, (780, 536))
        #Imagenes de botones que hacen aparecer pantallas
        if pantalla == 1:
                screen.blit(pant_status_image, (0,0))
        if pantalla == 2:
                screen.blit(pant_minigame_image, (0,0))
        if pantalla == 3:
                screen.blit(pant_manage_image, (0,0))
        #Tiempo (inútil aún)
        screen.blit(dia_actual,pos_dia)
        screen.blit(mes_actual,pos_mes)
        screen.blit(anho_actual,pos_anho)
        screen.blit(tiempo_actual, pos_tiempo_actual)
        #Recusos y sus imágenes
        screen.blit(banana_usables, pos_banana)
        screen.blit(banana_image, (10,5))
        screen.blit(semilla_usables, pos_semilla)
        screen.blit(semilla_image, (10,65))
        screen.blit(negro_usables, pos_negro)
        screen.blit(negro_image, (10,115))
        screen.blit(terreno_usables, pos_terreno)
        screen.blit(terreno_image, (10,165))
        #Propiedades / objetos
        if pantalla == 3:
                screen.blit(arbol_usables, pos_arbol)
                screen.blit(granja_usables, pos_granja)
                screen.blit(pais_usables, pos_pais)
                screen.blit(mundo_usables, pos_mundo)
        #Botones del juego
        screen.blit(bot_semillas_image,(10,330))
        if cuanto == 1:
                screen.blit(cuanto_comprar_image, (190, 330))
        screen.blit(bot_negros_image, (10,460))
        if cuanto == 2:
                screen.blit(cuanto_comprar_image, (190,460))
        screen.blit(bot_tierras_image, (10,590))
        if cuanto == 3:
                screen.blit(cuanto_comprar_image, (190, 590))
        screen.blit(bot_manage_image, (1085,5))
        screen.blit(bot_status_image, (1085, 150))
        screen.blit(bot_minigame_image, (1085, 320))
        #Muestra en pantalla lo dibujado
        pygame.display.flip()
        #Para salir del juego
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                pygame.display.quit()
                save.close()
                save = open("save.txt", "w")
                save.write(str(bananas)+"\n")
                save.write(str(semillas)+"\n")
                save.write(str(negros)+"\n")
                save.write(str(terrenos)+"\n")
                save.write(str(arboles)+"\n")
                save.write(str(granjas)+"\n")
                save.write(str(paises)+"\n")
                save.write(str(mundos)+"\n")                
                save.close()
                mojon = "caca"
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
