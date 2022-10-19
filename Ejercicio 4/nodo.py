class Nodo:
    __dato = None
    __repeticion = None #ADICIONAL
    __siguiente = None
    __izq = None
    __der = None
    def __init__(self, dato = None, rep = None):
        self.__dato = dato
        self.__repeticion = rep
        self.__siguiente = None
        self.__izq = None
        self.__der = None
    def setDato(self, dato = None):
        self.__dato = dato
    def setIzq(self, izq = None):
        self.__izq = izq
    def setDer(self, der = None):
        self.__der = der
    def getDato(self):
        return self.__dato
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der

    def setRepeticion(self, rep = None):
        self.__repeticion = rep
    def getRepeticion(self):
        return self.__repeticion
    def setSiguiente(self, siguiente = None):
        self.__siguiente = siguiente
    def getSiguiente(self):
        return self.__siguiente