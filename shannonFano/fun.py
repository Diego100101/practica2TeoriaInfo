# La clase sirve para crear objetos que puedan almacenar tres valores muy importantes, los cuales son:
# símbolo, su probabilidad y su respectivo código
class simbolo:
    def __init__(self, simbolo, probabilidad):
        self.simbolo = simbolo
        self.probabilidad = probabilidad
        self.codigo = ''

# La función recibe una lista de objetos y la divide en dos partes casi equiprobables.
# También utiliza los objetos de la clase "simbolo" para almacenar el código dependiendo de la lista
# en la que quedó, ya sea la lista de los mayores (0) o la lista de los menores (1)
def divide(listaObjetos):
    mitad = 0.5
    listaObjetos.sort(key=lambda x: x.probabilidad)
    parte1 = []
    parte2 = []
    for i in listaObjetos:
        suma = sum(o.probabilidad for o in parte1) + i.probabilidad
        if suma <= mitad:
            parte1.append(i)
            i.codigo += '1'
        else:
            parte2.append(i)
            i.codigo += '0'
    if len(parte1) > 1:
        divide(parte1)
    if len(parte2) > 1:
        divide(parte2)
    return parte1, parte2




