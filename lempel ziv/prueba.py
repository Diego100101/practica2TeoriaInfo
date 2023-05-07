from lempel import divideBits, codifica, guarda, convierteBytes
#archivo = input("Ingresa el nombre del archivo por codificar:\n")
archivo = 'gato.jpeg'
bits = "".join([f"{b:08b}" for b in open(fr"{archivo}", "rb").read()])

bitsDivididos = divideBits(bits)

codificado, tamano = codifica(bitsDivididos)

nombre = guarda(codificado, archivo)
print(tamano)

#decodificadoBits = ''.join([bin(b)[2:].zfill(8) for b in codificado])
divide = [codificado[i:i + tamano].zfill(tamano) for i in range(0, len(codificado), tamano)]
secuencia = [f"{n:0b}".zfill(tamano - 1) for n in range(0, len(divide))]
diccionario = dict(zip(secuencia, divide))
print(diccionario)
#print(divide)

