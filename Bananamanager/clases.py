class Boton:
        def __init__(self, posx1, posx2, posy1, posy2,boton):
                self.posx1 = posx1
                self.posx2 = posx2
                self.posy1 = posy1
                self.posy2 = posy2
                self.boton = boton
        def click(self,pos, anti_click, boton):
                if self.posx1 < pos[0] < self.posx2 and self.posy1 < pos[1] < self.posy2 and boton and anti_click:
                    return True
        def clickbananas(self,pos,mouse,anti_click,precio,recurso,bananas,cuanto):
            boton = self.boton*130
            if mouse[0] and 220 < pos[0] < 240 and 340+boton < pos[1] < 370+boton and anti_click and(bananas >=precio):
                bananas -= precio
                recurso += 1
            if mouse[0] and 280 < pos[0] < 310 and 340+boton < pos[1] < 370+boton and anti_click and(bananas >=precio*10):
                bananas -= precio*10
                recurso += 10
            if mouse[0] and 220 < pos[0] < 260 and 390+boton < pos[1] < 420+boton and anti_click and(bananas >=precio*100):
                bananas -= precio*100
                recurso += 100
            if mouse[0] and 275 < pos[0] < 325 and 390+boton< pos[1] < 420+boton and anti_click and(bananas >=precio*1000):
                bananas -= precio*1000
                recurso += 1000
            if mouse[0] and not (200 < pos[0] < 340) and not (460+boton < pos[1] < 565+boton) and anti_click and anti_click:
                cuanto = 0
            return bananas,recurso,cuanto
        
#CREAR RAZAS DE ARBOLES
        
    
                
