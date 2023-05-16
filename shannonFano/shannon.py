#------------------------------------------------------------------------------
# Universidad Autónoma Metropolitana: unidad Lerma
# Programador: Diego Cantoral González
# UEA: Teoría de la información y la codificación
# 16 de mayo de 2023
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
'''
Este código implementa todas las funciones del archivo "fun.py".
'''
#------------------------------------------------------------------------------

from fun import simbolo, divide
from collections import Counter


# Se lee el nombre archivo en el teclado y se crea una variable con la cadena de bits.
# También se crean las tuplas de 16 bits.
archivo = input("Nombre o ruta del archivo: \n")
bits = "".join(f"{b:08b}" for b in open(rf"{archivo}", "rb").read())
simbolos = [bits[s:s+16].zfill(16) for s in range(0, len(bits), 16)]

total = len(simbolos)

# Se calculan las frecuencias de cada símbolo.
frecuencias = dict(Counter(simbolos))


objetos = [simbolo(simbolobyte, probabilidadbyte/total) for simbolobyte, probabilidadbyte in frecuencias.items()]
 
# Se llama a la función "divide" para dividir la lista de objetos.
p1, p2 = divide(objetos)

