class Salida() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, salida) :
        self.salida = salida

class Salida_Consola() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, salida = "") :
        self.salida = salida

    def agregar(self, salida) :
        self.salida += salida
    def obtener(self) :
        return self.salida
    