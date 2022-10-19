from arbol import Arbol

def contador(text):
    lista = []
    caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for caracter in caracteres:
        j = 0
        for i in range(len(text)):
            if(text[i].lower() == caracter):
                j += 1
        if(j > 0):
            lista.append([caracter, j])
    return lista
if __name__ == '__main__':
    arbol = Arbol()
    with open('Ejercicio 4/text.txt') as archi:
        lista = contador(archi.read())
        print(lista)
        for caracter in lista:
            arbol.insertar(caracter[0], caracter[1])
        arbol.mostrar()
        arbol.huffman()
        arbol.mostrar()
        arbol.preOrden()