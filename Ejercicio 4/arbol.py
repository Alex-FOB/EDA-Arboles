from nodo import Nodo

class Arbol:
    __raiz = None
    def __init__(self):
        self.__raiz = None
    def vacio(self):
        return self.__raiz == None
    def insertar(self, caracter, rep):
        if(self.vacio()):
            self.__raiz = Nodo(caracter, rep)
        else:
            nodo = Nodo(caracter, rep)
            if(rep < self.__raiz.getRepeticion()):
                aux = self.__raiz
                nodo.setSiguiente(aux)
                self.__raiz = nodo
            else:
                aux = self.__raiz
                band = False
                while not band and aux.getSiguiente() != None:
                    if(aux.getSiguiente() != None):
                        siguiente = aux.getSiguiente()
                        if(siguiente.getRepeticion() > rep):
                            band = True
                        else:
                            aux = aux.getSiguiente()
                    else:
                        aux = aux.getSiguiente()
                siguiente = aux.getSiguiente()
                nodo.setSiguiente(siguiente)
                aux.setSiguiente(nodo)
    def huffman(self):
        while self.__raiz.getSiguiente() != None:
            siguiente = self.__raiz.getSiguiente()

            nodo = Nodo()
            nodo.setIzq(self.__raiz)
            nodo.setDer(siguiente)
            nodo.setSiguiente(siguiente.getSiguiente())
            nodo.setDato(self.__raiz.getDato() + siguiente.getDato())
            nodo.setRepeticion(self.__raiz.getRepeticion() + siguiente.getRepeticion())

            self.__raiz = nodo
            #print('ANT', self.mostrar())
            self.ordenar()
            #print('DES', self.mostrar())
    def ordenar(self):
        aux = self.__raiz
        pos = self.__raiz.getSiguiente()
        if(pos != None and aux.getRepeticion() > pos.getRepeticion()):
            self.__raiz = pos
            band = False
            while not band:
                ant = pos
                if(ant.getSiguiente() != None):
                    pos = pos.getSiguiente()
                    if(pos.getRepeticion() >= aux.getRepeticion()):
                        aux.setSiguiente(pos)
                        ant.setSiguiente(aux)
                        band = True
                    elif(pos.getSiguiente() == None):
                        aux.setSiguiente(None)
                        pos.setSiguiente(aux)
                        band = True
                else:
                    aux.setSiguiente(None)
                    ant.setSiguiente(aux)
                    band = True
                
    #def contar(self):
        #long = 0
        #aux = self.__raiz
        #while aux != None:
            #long += 1
            #aux = aux.getSiguiente()
        #return long
    def mostrar(self):
        lista = []
        aux = self.__raiz
        while aux != None:
            lista.append(aux.getDato())
            aux = aux.getSiguiente()
        return lista

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