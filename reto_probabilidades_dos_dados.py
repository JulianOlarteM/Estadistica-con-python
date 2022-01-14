
import random
from estadisticas import media, varianza, desviacion_estandar


def tirar_dados (numero_tiros):
    secuencia_de_tiros=[]    
    for _ in range (numero_tiros):
        tiro_dado_1 = random.choice([1,2,3,4,5,6])
        tiro_dado_2 =  random.choice([1,2,3,4,5,6]) 
        suma_dos_dados = tiro_dado_1 + tiro_dado_2 
        secuencia_de_tiros.append(suma_dos_dados)

    return secuencia_de_tiros



def main (numero_tiros,numero_intentos):
    tiros=[] 
    for _ in range (numero_intentos):
        secuencia_de_tiros = tirar_dados(numero_tiros) 
        med= media(secuencia_de_tiros)
        tiros.append(secuencia_de_tiros)
    
    tiros_con_12 = 0
    for tiro in tiros:
        if 12 in tiro: 
            tiros_con_12 += 1

    probabilidad_tiros_con_12 = (tiros_con_12 / numero_intentos)
    print(f'La probabilidad de obtener por lo menos un 12 en {numero_tiros} tiros = {probabilidad_tiros_con_12}  ')

if __name__== '__main__':
    numero_tiros=int(input('Ingrese cuantos  tiros hara con el dado: '))
    numero_intentos=int(input('Cuantas veces correra la simulacion: ')) #Entre mas muestras hallan de una poblacion, mas cerca estaremos del valor correcto de nuestra probabilidad "Ley de los Grandes Numero"  
    main(numero_tiros,numero_intentos)