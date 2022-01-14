from Borracho import BorrachoTradicional
from Campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio=campo.obtener_coordenada(borracho)
    for _ in range (pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))



def graficar (x,y):
    grafica = figure(title='Camino aleatorio',x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x,y, legend='distancia mediea')
    show(grafica)



def simular_caminata(pasos, numero_intentos,tipo_borracho):
    borracho=tipo_borracho(nombre='David')
    origen=Coordenada(0,0)
    distancias=[]

    for _ in range(numero_intentos):
        campo=Campo()
        campo.anadir_borracho(borracho,origen)
        simular_caminata=caminata(campo,borracho, pasos)
        distancias.append(round(simular_caminata,1))

    return distancias


def main(distancias_de_caminata, numero_intentos, tipo_borracho):
    distancias_media_por_caminata=[]

    for pasos in distancias_de_caminata:
        distancias  = simular_caminata(pasos, numero_intentos,tipo_borracho)
        distancia_media= round(sum(distancias)/len(distancias),4)
        distancia_maxima= max(distancias)
        dsitancia_minima=min(distancias)

        distancias_media_por_caminata.append(distancia_media) 
        
        print(f'{tipo_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'la distancia media es {distancia_media}')
        print(f'la distancia maxima es  {distancia_maxima}')
        print(f'la distancia minima es  {dsitancia_minima}')

    graficar(distancias_de_caminata,distancias_media_por_caminata)


if __name__=='__main__':

    distancias_de_caminata =[10, 100,1000,10000]
    numero_intentos=100
    main(distancias_de_caminata,numero_intentos, BorrachoTradicional)