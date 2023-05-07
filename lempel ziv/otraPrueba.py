from lempel import divideBits, codifica, guarda, convierteBytes
bits = '000000010011010010001001'
divide = [bits[i:i + 4] for i in range(0, len(bits), 4)]
secuencia = [n for n in range(1, len(divide) + 1)]

diccionario = dict(zip(secuencia, divide))
print(diccionario)

codificado = []
for valor in diccionario.values():
    bit = ''
    bit = valor[-1]
    bit1 = valor[:-1]
    #print(int(bit1, 2))
    if int(bit1, 2) == 0:
        codificado.append(bit)
        
    else:
        prefijo = diccionario[int(bit1,2)]
        print(prefijo)
        #codigo = prefijo + bit
        #codificado.append(codigo)

print(codificado)