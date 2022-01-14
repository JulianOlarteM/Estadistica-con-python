'''
Fibonachi:
Fn= Fn-1 + Fn-2

con elejemplo recursivo del curso anteriores muy ineficiente ya
que realiza el mismo computo de los numeros fibonachi varias veces.

Utilizaremos lo que se conoce como memoriztion

'''
import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

#Recibe un numero, y recibe el diccionario que vamos a ir generando
def fibonacci_dinamico(n , memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try: 
        return memo[n]
    except KeyError:
        resultado =  fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado
        return resultado


if __name__=='__main__':
    sys.setrecursionlimit(10002)
    num=int(input('ESCRIBE TU NUMERO: '))
    resultado = fibonacci_dinamico(num)
    print(resultado)