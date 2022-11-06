from arbolBB import arbolBB

if __name__ == '__main__':
    arbol = arbolBB()
    arbol.insertar(9)
    arbol.insertar(4)
    arbol.insertar(13)
    arbol.insertar(2)
    arbol.insertar(15)
    arbol.insertar(5)
    arbol.insertar(10)
    hijo = int(input("Ingrese Nodo Hijo: "))
    padre = int(input("Ingrese segundo nodo para verificar si es padre del primer nodo: "))
    arbol.padre(padre,hijo)
    print("Altura del arbol: ", arbol.altura())
    print("Cantidad de Nodos en el arbol: ", arbol.contador())
    suces = int(input("Ingrese nodo para mostrar sucesores: "))
    arbol.sucesores(suces)