palos=['espada', 'corazon', 'trebol']
valores = ['as','1','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_baraja():
    barajas=[]
    for palo in palos:
        for valor in valores:
            barajas.append((palo, valor)) # Creamos tuplas con todas las posibilidades 
    
    return barajas




if __name__=='__main__':

    barajas = crear_baraja()
    print(barajas)

