import random
import math
#from bokeh.plotting import figure, show


def media (X):
    return sum (X) / len(X)

def varianza(X):
    mu = media(X)
    acumulador = 0
    for x in X :
        acumulador += (x - mu )**2

    return acumulador/len(X)

def desviacion_estandar (X):
    return math.sqrt(varianza(X))

'''

def distribucion_normal (X):
    med = media(X)
    sigma = desviacion_estandar(X)
    lista_distr_normal=[]
    for x in X:
        distr_normal= (((1/(sigma*(math.sqrt(2*math.pi))))*(math.exp((-1/2)*((x - med)/ desviacion_estandar)**2))))
        lista_distr_normal.append(distr_normal)

    return lista_distr_normal 

def graficar (x,y):
    grafica = figure(title='Distribucion normal',x_axis_label='', y_axis_label='distribucion_normal')
    grafica.line(x,y)
    show(grafica)
'''

'''
if __name__=='__main__':

    X = [random.randint(1,21) for i in range (20)]
    mu = media(X)
    Var = varianza(X)
    Sigma = desviacion_estandar(X)
    
    dist_normal= distribucion_normal(X)
    print(dist_normal)
    graficar(X,dist_normal)

    print (f'Arreglo X: {X}')
    print (f'Media: {mu}')
    print(f'Varianza: {Var}')
    print(f'Desviacion_Estandar: {Sigma}')

'''