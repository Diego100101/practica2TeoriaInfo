from functools import reduce


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


def guarda(simbolos, nombreArchivo):
    divide = nombreArchivo.split(".")
    nuevoNombre = divide[0] + ".ziv"
    file = open(nuevoNombre, "w")
    file.write(simbolos)
    file.close()
    return nuevoNombre


def convierteBytes(bits):
    byte = bytearray()
    for i in range(0, len(bits), 8):
        byte.append(int(bits[i:i + 8], 2))
    return bytes(byte)

