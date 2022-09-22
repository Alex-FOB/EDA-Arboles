class Nodo:
    __dato = None
    __izq = None
    __der = None
    def __init__(self, dato = None, izq = None, der = None):
        self.__dato = dato
        self.__izq = izq
        self.__der = der
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