from huffmanCodigo import comprime, descomprime, guarda, guardaDescomprimido

archivo = input("Ingresa el archivo:\n")
codificado, arbol = comprime(archivo)
nombre = guarda(codificado, archivo)

decodificado = descomprime(nombre, arbol)
guardaDescomprimido(decodificado, archivo)
