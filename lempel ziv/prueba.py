#------------------------------------------------------------------------------
# Universidad Autónoma Metropolitana: unidad Lerma
# Programador: Diego Cantoral González
# UEA: Teoría de la información y la codificación
# 16 de mayo de 2023
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
'''
Este código implemetna todas las funciones del archivo "lempel.py".
'''
#------------------------------------------------------------------------------

from lempel import divideBits, codifica, guarda, convierteBytes

# Se ingresa la ruta del archivo para comprimir.
archivo = input("Ingresa el nombre del archivo por codificar:\n")
bits = "".join([f"{b:08b}" for b in open(fr"{archivo}", "rb").read()])

# Se llama a la función para dividir los bits de acuerdo al algoritmo.
bitsDivididos = divideBits(bits)

# Se llama a la función para codificar los bits y se almacena en un archivo con extensión y nombre nuevos.
codificado, tamano = codifica(bitsDivididos)

nombre = guarda(codificado, archivo)
print(tamano)

#decodificadoBits = ''.join([bin(b)[2:].zfill(8) for b in codificado])
divide = [codificado[i:i + tamano].zfill(tamano) for i in range(0, len(codificado), tamano)]
secuencia = [f"{n:0b}".zfill(tamano - 1) for n in range(0, len(divide))]
diccionario = dict(zip(secuencia, divide))
print(diccionario)
