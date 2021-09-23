from enum import Enum

class TIPO_DATO(Enum) :
    INT = 1
    NULO = 2
    BOOL = 3
    FLOAT = 4
    STRING = 5
    CHAR = 6
    ARRAY = 7

class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, valor) :
        self.id = id
        self.tipo = tipo
        self.valor = valor

class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, anterior="", simbolos=[] ) :
        self.simbolos = simbolos
        self.anterior = anterior

    def agregar(self, simbolo) :
        self.simbolos.append(simbolo)

    def obtener(self, id) :
        for i in self.simbolos:
            if i.id == id:
                return i
        print('Error: variable ', id, ' no definida.')
        return "0"


    def buscar(self, id) :
        for i in self.simbolos:
            if i.id == id:
                return i
        return "0"

    def actualizar(self, simbolo) :
        aux = []
        for i in self.simbolos:
            if i.id == simbolo.id:
                aux.append(simbolo)
            else:
                aux.append(i)
        self.simbolos = aux