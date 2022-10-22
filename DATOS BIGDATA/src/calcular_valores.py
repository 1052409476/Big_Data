from ast import arg
from tabnanny import verbose
from unittest import result
import numpy as np
import argparse


def calcular_suma(lista_numeros):
    '''
    calcula la suma de una lista de numeros
    Args: 
        lista_numeros : lista de numeros
    '''
    resultado = np.sum(lista_numeros)
    print('calcular_suma')
    print('suma', resultado)
    return resultado

def calcular_valores_centrales(lista_numeros):
    """calcular el valor media y desviacion estandar de una lista de numeros

    Args:
        lista_numeros (lista): lista de numeros con valores enteros

    Returns:
        tuple: (media, desviacion estandar)
    """
  
    media = np.mean(lista_numeros)
    dev_std = np.std(lista_numeros)
    
    print('calcular valores centrales')
    print('media', media)
    print('desv std', dev_std)
    return media, dev_std

def calcular_extremos(lista_numeros):
    """calcula el valor min y max de una lista de numeros

    Args:
        lista_numeros (lista): lista de numeros con valores enteros

    Returns:
        tuple: (min, max)
    """
    min_val = np.min(lista_numeros)
    max_val = np.max(lista_numeros)

    print('calcular valores extremos')
    print('min',min_val)
    print('max', max_val)

    return min_val, max_val

def calcular_valores(lista_numeros):
    suma = calcular_suma(lista_numeros)
    media, dev_std = calcular_valores_centrales(lista_numeros)
    min_val, max_val = calcular_extremos(lista_numeros)

    return suma, media, dev_std, min_val, max_val

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", type=int, default=1, help='para decidir si imprime informacion')

    args = parser.parse_args()
    verbose = args.verbose

    lista_numeros = [1, 2, 3, 4, 5, 6, 74, 3, 34, 13]
    suma, media, dev_std, min_val, max_val = calcular_valores(lista_numeros)
    print('DONE')

if __name__ == '__main__':
    main()
    