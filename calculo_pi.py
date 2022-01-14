import random
import math
from estadisticas import media,varianza, desviacion_estandar

def aventar_agujas(numero_agujas):
    dentro_del_cirulo = 0
    for _ in range (numero_agujas):
        x = random.random() * random.choice([-1 , 1]) # . random envia un valor  aleatorio entre 1 y 0. .choice envia alguna de las dos opciones (1 o -1).  
        y = random.random() * random.choice([-1 , 1]) 
        ditancia_desde_el_centro = math.sqrt(y**2 + x**2)

        if ditancia_desde_el_centro <= 1:
            dentro_del_cirulo += 1

    return (4*dentro_del_cirulo / numero_agujas)

def estimacion(numero_agujas, numero_intentos):
    estimados=[] # estimaciones 
    for _ in range (numero_intentos):
        estimacion_pi=aventar_agujas(numero_agujas)
        estimados.append(estimacion_pi)
    
    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Estimado = {round(media_estimados,5)}, sigma = {round(sigma, 5)}, agujas= {numero_agujas} ')

    return (media_estimados,sigma)

def estimar_pi(precision, numero_intentos):
    #Regla empirica, para determinar que tenemos un 95% de confianza, esta confianza la encontramos a  1.96 desviaciones estadandar.  
    num_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96 : #si uilizamos la regla empirica para un 68% lo dividimos entre 1, para un 95% lo dividimos entre 1.96, para un 99.73 % lo dividimos entre 3
        media, sigma = estimacion(num_agujas, numero_intentos)
        num_agujas *= 2

    return media


if __name__ == '__main__':
    estimar_pi(0.01, 1000)