from arbol import Arbol

def init():
    arbol = Arbol()
    lista = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 16]
    for dato in lista:
        arbol.insertar(dato)
    return arbol
if __name__ == '__main__':
    arbol = init()
    arbol.preOrden()
    arbol.insertar(12)
    #arbol.preOrden()
    print(arbol.buscar(10))
    print('Camino:', arbol.camino(8, 8))
    arbol.suprimir(8)
    #arbol.preOrden()
    print('Altura:', arbol.altura())
    arbol.insertar(17)
    print('Altura:', arbol.altura())
    arbol.insertar(15)
    print('Altura:', arbol.altura())