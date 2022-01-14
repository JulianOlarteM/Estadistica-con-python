c'''
El objetivo de esta clase es determinar una manera aleatoria de hacer caminar 
a nuestro borracho, se implementaran 4 posibilidades de movimiento generados de 
manera aleatoria (coordenadas inmutables, o tuplas).

hacia donde se  mueve el borracho

'''
import random

class Borracho:
    
    def __init__ (self, nombre):
        self.nombre = nombre

class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)
    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)]) #4 posibilidades de movimiento del borracho de manera aleatoria.
