def determinar_pantalla(pos,mouse,anti_click,pantalla):
    if mouse[0] and anti_click and (1085 < pos[0] < 1270) and (10 < pos[1] < 140):
            if pantalla !=3:
                pantalla = 3
            else:
                pantalla = 0
    if mouse[0] and anti_click and (1085 < pos[0] < 1270) and (150 < pos[1] <  315):
            if pantalla !=1:
                pantalla = 1
            else:
                pantalla = 0
    if mouse[0] and anti_click and (1085 < pos[0] < 1270) and (325 < pos[1] <  465):
            if pantalla !=2:
                pantalla = 2
            else:
                pantalla = 0
    return pantalla
    
