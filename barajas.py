import random
import collections  

palos=['espada', 'corazon','rombo',  'trebol']
valores = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_baraja():
    barajas=[]
    for palo in palos:
        for valor in valores:
            barajas.append((palo, valor)) # Creamos tuplas con todas las posibilidades 
    
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)# . sample nos permite obtener una muestra, sin opcion a repetirla.
    return mano

def probabilidad_pares_trios_poker(manos, intentos):
    pares = 0
    trios = 0
    poker = 0

    for mano in manos:
        val1=[]
        for val_carta in mano:
            val1.append(val_carta[1]) 

        counter1 = dict (collections.Counter(val1)) #generamos un contador de los valores de cada mano para determinar los pares.
        for val in counter1.values():
            if val == 2:
                pares += 1 
                break
            if val == 3:
                trios += 1
                break
            if val == 4:
                poker += 1
                break

    probabilidad_par = pares / intentos
    probabilidad_trios = trios / intentos
    probabilidad_cuarto = poker / intentos
    lista_probabilidades = [probabilidad_par,probabilidad_trios,probabilidad_cuarto]
    
    return lista_probabilidades

def funcion_probabilidad_doble_par(manos,intentos):
    doble_par = 0 

    for mano in manos:
        val2=[]
        for val_carta in mano:
            val2.append(val_carta[1])
        
        counter2 = dict(collections.Counter(val2))
        num_coincidencias = 0
        for val in counter2.values():
            if val == 2:
                num_coincidencias += 1
            if num_coincidencias ==2 : 
                doble_par += 1

    prob_dos_pares = doble_par / intentos
    return prob_dos_pares

def funcion_probabilidad_escalera(manos , intentos):
    escalera = 0
    for mano in manos:
        val3 = []
        for val_cart in mano :
            val3.append(val_cart[1])
        
        val_escalera = tuple(val3)
        posibilidades_de_escalera=[('as','2','3','4','5'),('2','3','4','5','6'),('3','4','5','6','7'),('4','5','6','7','8'),('5','6','7','8','9'),('6','7','8','9','10'),('7','8','9','10','jota'),('8','9','10','jota','reina'),('9','10','jota','reina','rey'),('10','jota','reina','rey','as'),('jota','reina','rey','as','2'),('reina','rey','as','2','3'),('rey','as','2','3','4')]
        for posibilidad in posibilidades_de_escalera:
            if sorted(posibilidad) == sorted(val_escalera):
                escalera += 1 
            
    probabilidad_escalera = escalera/intentos
    return  probabilidad_escalera

def funcion_probabilidad_color(manos, intentos):
    color = 0
    for mano in manos:
        val4=[]
        for val_cart in mano:
            val4.append(val_cart[0])
        
        counter4 = dict (collections.Counter(val4))
        for i in counter4.values():
            if i == 5:
                color += 1
                
    probabilidad_color= color/intentos
    return probabilidad_color

def funcion_probabilidad_fullhouse (manos, intentos):
    fullhaouse=0
    for mano in manos:
        par=0
        trio=0
        val5=[]
        for  val_cart in mano:
            val5.append(val_cart[1])
        
        counter5= dict(collections.Counter(val5))
        for i in counter5.values():
            if i == 2:
                par += 1
            if i == 3:
                trio += 1
            else:
                break
        
        if par == 1 and trio == 1:
            fullhaouse += 1

    probabilidad_fullhause = fullhaouse/intentos
    return probabilidad_fullhause

def funcion_probabilidad_escalera_color(manos, intentos):
    escalera_color = 0
    for mano in manos:

        val_palos = []
        val_valores=[]
        color = 0
        escalera = 0

        for valor_cart in mano:
            val_palos.append(valor_cart[0])
            val_valores.append(valor_cart[1])

        counter6 = dict (collections.Counter(val_palos))
        val_escalera = tuple(val_valores)
        posibilidades_de_escalera=[('as','2','3','4','5'),('2','3','4','5','6'),('3','4','5','6','7'),('4','5','6','7','8'),('5','6','7','8','9'),('6','7','8','9','10'),('7','8','9','10','jota'),('8','9','10','jota','reina'),('9','10','jota','reina','rey'),('10','jota','reina','rey','as'),('jota','reina','rey','as','2'),('reina','rey','as','2','3'),('rey','as','2','3','4')]
        
        for posibilidad in posibilidades_de_escalera:
            if sorted(posibilidad) == sorted(val_escalera):
                escalera += 1 
     

        for i in counter6.values():
            if i == 5:
                color += 1

        if color == 1 and escalera==1:
            escalera_color += 1
    
    probabilidad_escalera_color = escalera_color/intentos
    return probabilidad_escalera_color
                 
def funcion_probabilidad_escalera_real(manos,intentos):
    escalera_real = 0
    for mano in manos:

        val_palos = []
        val_valores=[]
  
        for valor_cart in mano:
            val_palos.append(valor_cart[0])
            val_valores.append(valor_cart[1])

        counter6 = dict (collections.Counter(val_palos))
        val_escalera = tuple(val_valores)
        posibilidad_de_escalera=('10','jota','reina','rey','as')
        
        if sorted(posibilidad_de_escalera) == sorted(val_escalera):
            for i in counter6.values():
                if i == 5:
                    escalera_real += 1

    probabilidad_escalera_real = escalera_real/intentos
    return probabilidad_escalera_real

def main (tamano_mano , intentos):
    barajas = crear_baraja()
    manos=[]
    for _ in range(intentos):
        mano = obtener_mano(barajas,tamano_mano) 
        manos.append(mano)  
               
    funcion_probabilidades = probabilidad_pares_trios_poker(manos,intentos)
    prob_pares = funcion_probabilidades[0]
    prob_tiros = funcion_probabilidades[1]
    prob_poker = funcion_probabilidades[2]

    probabilidad_dos_pares = funcion_probabilidad_doble_par(manos,intentos)
    probabilidad_de_escalera = funcion_probabilidad_escalera(manos,intentos)
    probabilidad_de_color = funcion_probabilidad_color(manos,intentos) 
    probabilidad_de_fullhause = funcion_probabilidad_fullhouse(manos,intentos) 
    probabilidad_de_escalera_color = funcion_probabilidad_escalera_color(manos,intentos) 
    probabilidad_de_escalera_reaal = funcion_probabilidad_escalera_real(manos,intentos) 

    print(f'La probabilidad de sacar una ESCALERA REAL con {tamano_mano} cartas es de {probabilidad_de_escalera_reaal}')
    print(f'La probabilidad de sacar una ESCALERA COLOR con {tamano_mano} cartas es de {probabilidad_de_escalera_color}')
    print(f'La probabilidad de sacar un POKER con {tamano_mano} cartas es de {prob_poker}')
    print(f'La probabilidad de sacar un FULLHAUSE con {tamano_mano} cartas es de {probabilidad_de_fullhause}')     
    print(f'La probabilidad de sacar un COLOR con {tamano_mano} cartas es de {probabilidad_de_color}')       
    print(f'La probabilidad de sacar una ESCALERA con {tamano_mano} cartas es de {probabilidad_de_escalera}')
    print(f'La probabilidad de sacar un TRIO con {tamano_mano} cartas es de {prob_tiros}')
    print(f'La probabilidad de sacar DOBLE PAR con {tamano_mano} cartas es de {probabilidad_dos_pares}')
    print(f'La probabilidad de sacar un PAR con {tamano_mano} cartas es de {prob_pares}')
    
if __name__=='__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuntos intentos para calcular la probabilidad: '))
    main(tamano_mano,intentos)