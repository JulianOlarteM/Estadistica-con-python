codeclass Campo():

    def __init__(self):
        self.coordenadas_de_borrachos = {} #diccionario vacio para saber donde estan los borrachos 

    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada # "borracho es la llave del diccionario", y "coordenada es el valor de cada llve"

    def mover_borracho(self, borracho):
        delta_x,delta_y= borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x,delta_y)

        self.coordenadas_de_borrachos[borracho]=nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho] 