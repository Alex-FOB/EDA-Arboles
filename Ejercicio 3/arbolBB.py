from nodo import nodo

class arbolBB:
    __raiz = None
    __cantidad = None
    def __init__(self):
        self.__raiz = None
        self.__cantidad = 0
    def vacio(self):
        return self.__raiz == None
    def obtenerRaiz(self):
        return self.__raiz
    def mostrarRaiz(self):
        return self.__raiz.getItem()
    def insertar(self, x):
        if self.vacio():
            self.__raiz = nodo(x)
        else:
            aux = self.posicion(x)
            if aux != None:
                celda = nodo(x)
                clave = aux[0].getItem()
                if clave > x:
                    aux[0].cargarIzquierdo(celda)
                elif clave < x:
                    aux[0].cargarDerecho(celda)
            else:
                print("ERROR")
    def suprimir(self, x):
        if not self.vacio():
            nodo = self.posicion(x)[0]
            if nodo.getItem() == x:
                aux = nodo.obtenerIzquierdo()
                if aux != None:
                    while aux.obtenerDerecho() != None:
                        aux = aux.obtenerDerecho()
                    camino = self.camino(x, aux.getItem())
                    padre = self.posicion(camino[len(camino) - 2])[0]
                    if self.__raiz.getItem() == x:
                        self.__raiz.cargarItem(aux.getItem())
                    else:
                        nodo.cargarItem(aux.getItem())
                    izq = padre.obtenerIzquierdo()
                    if izq.getItem() == aux.getItem():
                        padre.cargarIzquierdo(None)
                    else:
                        padre.cargarDerecho(None)
                else:
                    camino = self.camino(self.__raiz.getItem(), x)
                    padre = self.posicion(camino[len(camino) - 2])[0]
                    izq = padre.obtenerIzquierdo()
                    if izq.getItem() == x:
                        padre.cargarIzquierdo(None)
                    else:
                        padre.cargarDerecho(None)
            else:
                print("ERROR")
    def buscar(self, x):
        band = False
        elemento = self.posicion(x)[0]
        if elemento.getItem()==x:
            band = True
        return band
    def nivel(self, x):
        niv = 0
        elemento = self.posicion(x)
        if elemento[0].getItem()==x:
            niv = elemento[1]
        else:
            print("ERROR")
        return niv
    def hoja(self, x):
        band = False
        elemento = self.posicion(x)[0]
        if elemento.getItem()==x and elemento.obtenerIzquierdo() == None and elemento.obtenerDerecho()==None:
            band = True
        else:
            if elemento.getItem() != x:
                print("ERROR")
        return band
    def hijo(self, x, z):
        band = False
        celda = self.posicion(z)[0]
        if celda.getItem()==z:
            izq = celda.obtenerIzquierdo()
            if izq != None and izq.getItem()==x:
                band = True
            else:
                der = celda.obtenerDerecho()
                if der != None and der.getItem()==x:
                    band = True
        else:
            print("ERROR")
        return band
    def padre(self, z, x):
        band = False
        celda = self.posicion(z)[0]
        if celda.getItem() == z:
            izq = celda.obtenerIzquierdo()
            if izq != None and izq.getItem() == x:
                print("El Padre de {} es {}".format(x, celda.getItem()))
                i=celda.obtenerDerecho()
                print("El hermano de {} es {}".format(x, i.getItem()))
                band = True
            else:
                der = celda.obtenerDerecho()
                if der != None and der.getItem() == x:
                    print("El padre de {} es {}".format(x, celda.getItem()))
                    i=celda.obtenerIzquierdo()
                    print("El hermano de {} es {}".format(x, i.getItem()))
                    band = True
                else:
                    print("{} no es hijo de {}".format(x, z))
        else:
            print("No se encontro nodo Padre")
        return band
    def camino(self, x, z):
        lista = []
        nodo1 = self.posicion(x)[0]
        if nodo1.getItem() == x:
            nodo2 = self.posicion(z)[0]
            if nodo2.getItem() == z:
                band = False
                while not band:
                    dato1 = nodo1.getItem()
                    dato2 = nodo2.getItem()
                    if dato1 == dato2:
                        lista.append(dato1)
                        band = True
                    elif dato1 > dato2:
                        if nodo1.obtenerIzquierdo() == None:
                            band = True
                            lista = []
                        else:
                            lista.append(dato1)
                            nodo1 = nodo1.obtenerIzquierdo()
                    else:
                        if nodo1.obtenerDerecho() == None:
                            band = True
                            lista = []
                        else:
                            lista.append(dato1)
                            nodo1 = nodo1.obtenerDerecho()
            else:
                print("ERROR")
        else:
            print("ERROR")
        if (lista == []):
            print("ERROR")
        return lista
    def altura(self):
        if self.vacio():
            print("Arbol Vacio")
        else:
            aux = self.__raiz
            return self.calcAltura(aux, 0, 0)
    def calcAltura(self, nodo, altura, max):
        if (nodo != None):
            dato = self.calcAltura(nodo.obtenerIzquierdo(), altura + 1, max)
            if (altura > max):
                max = altura
            if (dato > max):
                max = dato
            dato = self.calcAltura(nodo.obtenerDerecho(), altura + 1, max)
            if (dato > max):
                max = dato
        return max
    def InOrden(self, raiz):
        if raiz != None:
            self.InOrden(raiz.obtenerIzquierdo())
            print(raiz.getItem())
            self.InOrden(raiz.obtenerDerecho())
    def PreOrden(self, raiz):
        if raiz != None:
            print(raiz.getItem())
            self.PreOrden(raiz.obtenerIzquierdo())
            self.PreOrden(raiz.obtenerDerecho())
    def PostOrden(self, raiz):
        if raiz != None:
            self.PostOrden(raiz.obtenerIzquierdo())
            self.PostOrden(raiz.obtenerDerecho())
            print(raiz.getItem())
    def sucesores(self, nodo):
        elemento = self.posicion(nodo)[0]
        if elemento.getItem() == nodo:
            self.PreOrden(elemento)
    def posicion(self, x, niv=0):
        if not self.vacio():
            posicion = [None, None]
            if self.__raiz.getItem()==x:
                posicion[0] = self.__raiz
                posicion[1] = niv
            else:
                aux = self.__raiz
                band = True
                while band:
                    clave = aux.getItem()
                    if clave == x:
                        band = False
                    elif clave > x:
                        if aux.obtenerIzquierdo()==None:
                            band = False
                        else:
                            niv += 1
                            aux = aux.obtenerIzquierdo()
                    else:
                        if aux.obtenerDerecho()==None:
                            band = False
                        else:
                            niv += 1
                            aux = aux.obtenerDerecho()
                posicion[0]=aux
                posicion[1]=niv
        return posicion
    def buscaHojas(self, nodo):
        if nodo != None:
            self.buscaHojas(nodo.obtenerIzquierdo())
            if nodo.obtenerIzquierdo() == None and nodo.obtenerDerecho() == None:
                print(nodo.getItem())
            self.buscaHojas(nodo.obtenerDerecho())
    def frontera(self):
        aux = self.__raiz
        self.buscaHojas(aux)
    def cuentaNodo(self, nodo):
        if nodo != None:
            self.cuentaNodo(nodo.obtenerIzquierdo())
            self.__cantidad += 1
            self.cuentaNodo(nodo.obtenerDerecho())
    def contador(self):
        aux = self.__raiz
        self.cuentaNodo(aux)
        return self.__cantidad