from nodo import Nodo

class Arbol:
    __raiz = None
    __altura = None #sirve para saber cual es la altura del arbol
    def __init__(self):
        self.__raiz = None
        self.__altura = 0
    def vacio(self):
        return self.__raiz == None
    def insertar(self, dato): #Inserta el dato en el arbol
        if(self.vacio()):
            self.__raiz = Nodo(dato)
        else:
            aux = self.busqueda(dato)
            if(aux != None):
                nodo = Nodo(dato)
                clave = aux[0].getDato()
                if(clave > dato):
                    if(aux[1]+1 > self.__altura):
                        self.__altura = aux[1]+1
                    aux[0].setIzq(nodo)
                elif(clave < dato):
                    if(aux[1]+1 > self.__altura):
                        self.__altura = aux[1]+1
                    aux[0].setDer(nodo)
            else:
                raise IndexError('ERROR: dato invalido')
    def suprimir(self, dato): #CRITERIO DE ELIMINACION: por izquierda
        if(not self.vacio()):
            nodo = self.busqueda(dato)[0]
            if(nodo.getDato() == dato):
                aux = nodo.getIzq()
                if(aux != None):
                    while aux.getDer() != None:
                        aux = aux.getDer()
                    camino = self.camino(dato, aux.getDato())
                    padre = self.busqueda(camino[len(camino)-2])[0] #el penultimo de la lista
                    if(self.__raiz.getDato() == dato):
                        self.__raiz.setDato(aux.getDato())
                    else:
                        nodo.setDato(aux.getDato())
                    izq = padre.getIzq()
                    if(izq.getDato() == aux.getDato()):
                        padre.setIzq(None)
                    else:
                        padre.setDer(None)
                else:
                    camino = self.camino(self.__raiz.getDato(), dato)
                    padre = self.busqueda(camino[len(camino)-2])[0] #el penultimo de la lista
                    izq = padre.getIzq()
                    if(izq.getDato() == dato):
                        padre.setIzq(None)
                    else:
                        padre.setDer(None)
            else:
                raise IndexError('ERROR.SUPRIMIR: nodo no encontrado')
    def buscar(self, clave): #busca el elemento en el arbol
        band = False
        aux = self.busqueda(clave)[0]
        if(aux.getDato() == clave):
            band = True
        return band
    def nivel(self, dato): #devuelve el nivel de nodo
        nivel = 0
        aux = self.busqueda(dato)
        if(aux[0].getDato() == dato):
            nivel = aux[1]
        else:
            raise IndexError('ERROR.NIVEL: el nodo no esta en el arbol')
        return nivel
    def hoja(self, dato): #devuelve Verdadero si el nodo a buscar es una hoja
        band = False
        aux = self.busqueda(dato)[0]
        if(aux.getDato() == dato and aux.getIzq() == None and aux.getDer() == None):
            band = True
        elif(aux.getDato() != dato):
            raise IndexError('ERROR.HOJA: el nodo no esta en el arbol')
        return band
    def hijo(self, hijo, padre): #PREGUNTAR
        band = False
        nodo = self.busqueda(padre)[0]
        if(nodo.getDato() == padre):
            izq = nodo.getIzq()
            if(izq != None and izq.getDato() == hijo):
                band = True
            else:
                der = nodo.getDer()
                if(der != None and der.getDato() == hijo):
                    band = True
        else:
            raise IndexError('ERROR.HIJO: nodo padre no encontrado')
        return band
    def padre(self, padre, hijo): #PREGUNTAR
        band = False
        nodo = self.busqueda(padre)[0]
        if(nodo.getDato() == padre):
            izq = nodo.getIzq()
            if(izq != None and izq.getDato() == hijo):
                band = True
            else:
                der = nodo.getDer()
                if(der != None and der.getDato() == hijo):
                    band = True
        else:
            raise IndexError('ERROR.HIJO: nodo padre no encontrado')
        return band
    def camino(self, inicio, final): #devuelve una lista con las claves de los nodos del camino (LISTA DE NODOS?)
        lista = []
        nodo1 = self.busqueda(inicio)[0]
        if(nodo1.getDato() == inicio):
            nodo2 = self.busqueda(final)[0]
            if(nodo2.getDato() == final):
                band = False
                while not band:
                    dato1 = nodo1.getDato()
                    dato2 = nodo2.getDato()
                    if(dato1 == dato2):
                        lista.append(dato1)
                        band = True
                    elif(dato1 > dato2):
                        if(nodo1.getIzq() == None):
                            band = True
                            lista = []
                        else:
                            lista.append(dato1)
                            nodo1 = nodo1.getIzq()
                    else:
                        if(nodo1.getDer() == None):
                            band = True
                            lista = []
                        else:
                            lista.append(dato1)
                            nodo1 = nodo1.getDer()
            else:
                raise IndexError('ERROR.CAMINO: el nodo final no esta en el arbol')
        else:
            raise IndexError('ERROR.CAMINO: el nodo inicial no esta en el arbol')
        if(lista == []):
            raise IndexError('ERROR.CAMINO: no hay camino')
        return lista
    def altura(self):
        if(not self.vacio()):
            return self.__altura
        else:
            raise TypeError('ERROR.ALTURA: arbol vacio')


    def preOrden(self):
        aux = self.__raiz
        print('Pre - Orden:\n', self.__raiz.getDato())
        self.recursiva(aux.getIzq())
        self.recursiva(aux.getDer())
    def inOrden(self):
        aux = self.__raiz
        print('In - Orden:\n')
        self.recursiva(aux.getIzq())
        print(self.__raiz.getDato())
        self.recursiva(aux.getDer())
    def postOrden(self):
        aux = self.__raiz
        print('Post - Orden:\n')
        self.recursiva(aux.getIzq())
        self.recursiva(aux.getDer())
        print(self.__raiz.getDato())
    
    #ADICIONAL
    def recursiva(self, nodo): #Analiza todo el arbol de manera recursiva
        if(nodo != None):
            self.recursiva(nodo.getIzq())
            print(nodo.getDato())
            self.recursiva(nodo.getDer())
    def busqueda(self, dato, nivel = 0):
        if(not self.vacio()):
            pos = [None, None]
            if(self.__raiz.getDato() == dato):
                pos[0] = self.__raiz
                pos[1] = nivel
            else:
                aux = self.__raiz
                band = False
                while not band:
                    clave = aux.getDato()
                    if(clave == dato):
                        band = True
                    elif(clave > dato):
                        if(aux.getIzq() == None):
                            band = True
                        else:
                            nivel += 1
                            aux = aux.getIzq()
                    else:
                        if(aux.getDer() == None):
                            band = True
                        else:
                            nivel += 1
                            aux = aux.getDer()
                pos[0] = aux
                pos[1] = nivel
        return pos
    def buscarHojas(self, nodo):
        if(nodo != None):
            self.buscarHojas(nodo.getIzq())
            if(nodo.getIzq() == None and nodo.getDer() == None):
                print(nodo.getDato())
            self.buscarHojas(nodo.getDer())
    def frontera(self):
        aux = self.__raiz
        print('Hojas:')
        self.buscarHojas(aux)