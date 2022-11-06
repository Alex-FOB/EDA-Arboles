class nodo:
    __item = 0
    __izq = None
    __der = None
    def __init__(self, item=0, izq=None, der=None):
        self.__item = item
        self.__izq = izq
        self.__der = der
    def getItem(self):
        return self.__item
    def cargarItem(self, x=None):
        self.__item = x
    def cargarIzquierdo(self, puntero=None):
        self.__izq = puntero
    def obtenerIzquierdo(self):
        return self.__izq
    def cargarDerecho(self, puntero=None):
        self.__der = puntero
    def obtenerDerecho(self):
        return self.__der