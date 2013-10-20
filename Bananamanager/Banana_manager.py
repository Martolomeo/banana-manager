#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Banana manager
 
# Módulos

import pygame, time, random
from pygame.locals import *
 
# Constantes

WIDTH = 1280
HEIGHT = 700
 
# Clases
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

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

    background_image = load_image('fondo.png')
    banana_image = load_image('banana.png', True)
    banner_image = load_image('banner.png', True)
    semilla_image = load_image('semilla.png', True)
    negro_image = load_image('negro.png', True)
    terreno_image = load_image('terreno.png', True)
    bot_semillas_image = load_image('bot_semillas.png', True)
    bot_negros_image = load_image('bot_negros.png', True)
    bot_tierras_image = load_image('bot_tierras.png', True)
    
    start = time.clock()
    tprod = start
    turno = 0
    bananas = 1000
    semillas = 0
    negros = 0
    terrenos = 0
    produccion = 1
    salir = 0
    tiempo = 0
    mojon = "banana"
    mouse_boton = pygame.mouse.get_pressed()
    pos_mouse = pygame.mouse.get_pos()
    anti_click = True
    
    while True:
        mouse_boton = pygame.mouse.get_pressed()
        pos_mouse = pygame.mouse.get_pos()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                pygame.display.quit()
                mojon = "monotriste"

        if mojon == "monotriste":
                break

        tiempo = int(time.clock() - start)
        turno = int(time.clock() - tprod)
        if turno == 1:
                bananas += produccion
                tprod = time.clock()

        if mouse_boton[0] and 10 < pos_mouse[0] < 190 and 330 < pos_mouse[1] < 440 and bananas >= 10 and anti_click:
                semillas += 1
                bananas -= 10
                anti_click = False
        if mouse_boton[0] and 10 < pos_mouse[0] < 190 and 460 < pos_mouse[1] < 570 and bananas >= 20 and anti_click:
                negros += 1
                bananas -= 20
                anti_click = False
        if mouse_boton[0] and 10 < pos_mouse[0] < 190 and 590 < pos_mouse[1] < 700 and bananas >= 5 and anti_click:
                terrenos += 1
                bananas -= 5
                anti_click = False
        if not mouse_boton[0]:
                anti_click = True
        tiempo_actual, tiempo_actual_rect = texto(str(tiempo),320,240, 30)
        banana_usables, pos_banana = texto(str(bananas), 120,50, 30)
        semilla_usables, pos_semilla = texto(str(semillas), 120,100, 30)
        negro_usables, pos_negro = texto(str(negros), 120,150, 30)
        terreno_usables, pos_terreno = texto(str(terrenos), 120,200, 30)

        screen.blit(background_image, (0,0))
        screen.blit(bot_semillas_image,(10,330))
        screen.blit(banner_image, (780, 536))
        screen.blit(tiempo_actual, (WIDTH/2,HEIGHT/2))
        screen.blit(banana_usables, pos_banana)
        screen.blit(banana_image, (10,5))
        screen.blit(semilla_usables, pos_semilla)
        screen.blit(semilla_image, (10,65))
        screen.blit(negro_usables, pos_negro)
        screen.blit(negro_image, (10,115))
        screen.blit(terreno_usables, pos_terreno)
        screen.blit(terreno_image, (10,165))
        screen.blit(bot_negros_image, (10,460))
        screen.blit(bot_tierras_image, (10,590))
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
