'''
Conforme exitan mas datos simulados , mas cerca estaremos de allar la respuesta adecuada. 

'''
import random

def tirar_dado (numero_tiros):
    secuencia_de_tiros=[]    
    for _ in range (numero_tiros):
        tiro = random.choice([1,2,3,4,5,6]) 
        #se pudo utilizar random.randint(1,7)
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros


def main (numero_tiros,numero_intentos):
    tiros=[] #arreglo que guarda los resultados de cada intento
    for _ in range (numero_intentos):
        secuencia_de_tiros = tirar_dado(numero_tiros) #La funcion tirar_dado nos devuelve una secuencia de tiros
        tiros.append(secuencia_de_tiros)
    
    ##Probabilidad de que salga un 1

    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro: #Si 1 esta en el tiro
            tiros_con_1 += 1

    probabilidad_tiros_con_1 = (tiros_con_1 / numero_intentos)

    print(f'La probabilidad de obtener por lo menos un 1 en {numero_tiros} tiros = {probabilidad_tiros_con_1}  ')




if __name__== '__main__':
    numero_tiros=int(input('Ingrese cuantos  tiros hara con el dado: '))
    numero_intentos=int(input('Cuantas veces correra la simulacion: ')) #Entre mas muestras hallan de una poblacion, mas cerca estaremos del valor correcto de nuestra probabilidad "Ley de los Grandes Numero"  
    main(numero_tiros,numero_intentos)