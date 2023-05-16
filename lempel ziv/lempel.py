from functools import reduce

# La función replica el algoritmo visto en clase. Para una cadena de bits, toma el primer bit y, si no lo conoce, lo almacena en "diccionario", si ya lo conoce
# avanza al siguiente bit y repite la misma condición, si ya existe en "diccionario", avanza al siguiente bit, así hasta haber almacenado toda la cadena. Para cada bit
# se incrementa en 1 el índice para poder realizar los prefijos.
def divideBits(bits):
    index = 1
    diccionario = {}
    bitTemp = ''
    for i in range(0, len(bits)):
        if bitTemp:
            bitTemp += bits[i]
            if bitTemp not in diccionario.keys():
                diccionario[bitTemp] = f"{index:0b}"
                bitTemp = ''
                index += 1
        else:
            if bits[i] not in diccionario.keys():
                diccionario[bits[i]] = f"{index:0b}"
                index += 1
            else:
                bitTemp = bits[i]
    return diccionario

# En esta función se utiliza el diccionario creado con los bits y su índice correspondiente para comenzar a codificar y obtener los prefijos de
# cada símbolo. Para esto, se toma el primer bit de cada símbolo y se concatena cada prefijo.
def codifica(diccionario):
    codificado = []
    for valor in diccionario.keys():
        bit = ''
        if len(valor) > 1:
            bit = valor[-1]
            # print(bit)
            bit1 = valor[:-1]
            # print(bit1)
            prefijo = diccionario[bit1]
            codigo = prefijo + bit
            codificado.append(codigo)
        else:
            codificado.append(valor)
    max = len(reduce(lambda x, y: x if len(x) > len(y) else y, codificado))
    return "".join([str(c).zfill(max) for c in codificado]), max

# La función decodifica el archivo con los nuevos bits. No tuve éxito.
def decodifica(diccionario):
    codificado = []
    for valor in diccionario.values():
        bit = ''
        bit = valor[-1]
            # print(bit)
        bit1 = valor[:-1]
            # print(bit1)
        prefijo = diccionario[bit1]
        codigo = prefijo + bit
        codificado.append(codigo)

    max = len(reduce(lambda x, y: x if len(x) > len(y) else y, codificado))
    return "".join([str(c).zfill(max) for c in codificado]), max


# La función guarda los símbolos obtenidos y lo almacena en un nuevo archivo con un nombre y extensión diferente
def guarda(simbolos, nombreArchivo):
    divide = nombreArchivo.split(".")
    nuevoNombre = divide[0] + ".ziv"
    file = open(nuevoNombre, "w")
    file.write(simbolos)
    file.close()
    return nuevoNombre

# Esta función convierte los bits a Bytes para almacenarlos en el archivo con nueva extensión.
def convierteBytes(bits):
    byte = bytearray()
    for i in range(0, len(bits), 8):
        byte.append(int(bits[i:i + 8], 2))
    return bytes(byte)

