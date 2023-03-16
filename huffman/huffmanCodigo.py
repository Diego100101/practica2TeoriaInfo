from heapq import heappop, heappush, heapify
from collections import Counter


class Arbol:
    def __init__(self, caracter, frecuencia, izquierda=None, derecha=None):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = izquierda
        self.derecha = derecha

    def __lt__(self, other):
        return self.frecuencia < other.frecuencia


def construyeArbol(archivo):
    contador = Counter(archivo)
    heap = [Arbol(caracter, contador[caracter]) for caracter in contador]
    heapify(heap)
    while len(heap) > 1:
        izquierda = heappop(heap)
        derecha = heappop(heap)
        padre = Arbol(None, izquierda.frecuencia + derecha.frecuencia, izquierda, derecha)
        heappush(heap, padre)
    return heappop(heap)


def construyeMapa(arbol):
    def dfs(arbol, codigo, mapa):
        if arbol.caracter:
            mapa[arbol.caracter] = ''.join(codigo)
        else:
            codigo.append('0')
            dfs(arbol.izquierda, codigo, mapa)
            codigo.pop()
            codigo.append('1')
            dfs(arbol.derecha, codigo, mapa)
            codigo.pop()

    mapa = {}
    dfs(arbol, [], mapa)
    return mapa


def comprime(archivo):
    tuplas = obtenTuplas(archivo)
    arbol = construyeArbol(tuplas)
    mapa = construyeMapa(arbol)
    bytes = convierteBytes(''.join([mapa[caracter] for caracter in tuplas]))
    return bytes, arbol


def descomprime(codificado, arbol):
    bits = "".join([f"{n:08b}" for n in open(fr"{codificado}", "rb").read()])
    if arbol.caracter:
        return arbol.caracter * len(bits)
    decodificado = []
    nodo = arbol
    for bit in bits:
        if bit == "0":
            nodo = nodo.izquierda
        else:
            nodo = nodo.derecha
        if nodo.caracter:
            decodificado.append(nodo.caracter)
            nodo = arbol
    return ''.join(decodificado)


def convierteBytes(bits):
    byte = bytearray()
    for i in range(0, len(bits), 8):
        byte.append(int(bits[i:i + 8], 2))
    return bytes(byte)


def obtenTuplas(archivo):
    bits = "".join([f"{n:08b}" for n in open(rf"{archivo}", "rb").read()])
    tuplas = [bits[i:i + 16].zfill(16) for i in range(0, len(bits), 16)]
    return tuplas


def guarda(bytes, nombreArchivo):
    divide = nombreArchivo.split(".")
    nuevoNombre = divide[0] + "_comprimido.huff"
    file = open(nuevoNombre, "wb")
    file.write(bytes)
    file.close()
    return nuevoNombre


def guardaDescomprimido(bits, nombreArchivo):
    original = convierteBytes(bits)
    divide = nombreArchivo.split(".")
    nuevoNombre = divide[0] + "_descomprimido." + divide[1]
    archivo = open(nuevoNombre, "wb")
    archivo.write(original)
    archivo.close()