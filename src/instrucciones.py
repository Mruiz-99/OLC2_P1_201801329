from tabla_simbolos import TIPO_DATO


class Instruccion:
    '''This is an abstract class'''

class Imprimir(Instruccion) :
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self,  cad) :
        self.cad = cad

class Imprimirln(Instruccion) :
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self,  cad) :
        self.cad = cad 

       

class Mientras(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class ForRango(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expDeclarativa, desde,hasta,linea,columna, instrucciones = []) :
        self.expDeclarativa = expDeclarativa
        self.desde = desde
        self.hasta = hasta
        self.linea = linea
        self.columna = columna
        self.instrucciones = instrucciones
class ForExp(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expDeclarativa, exp, linea, columna, instrucciones = []) :
        self.expDeclarativa = expDeclarativa
        self.exp = exp
        self.linea = linea
        self.columna = columna
        self.instrucciones = instrucciones

class Definicion(Instruccion) :
    '''
        Esta clase representa la instrucción de definición de variables.
        Recibe como parámetro el nombre del identificador a definir
    '''

    def __init__(self, id) :
        self.id = id

class Asignacion(Instruccion) :
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''
    def __init__(self, id, exp,linea, columna) :
        self.id = id
        self.exp = exp
        self.linea = linea
        self.columna = columna

class AsignacionArray(Instruccion) :
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''
    def __init__(self, id, indice, exp,linea, columna) :
        self.id = id
        self.indice = indice
        self.exp = exp
        self.linea = linea
        self.columna = columna

class AsignacionArrayBi(Instruccion) :
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''
    def __init__(self, id, indice, indice2, exp,linea, columna) :
        self.id = id
        self.indice = indice
        self.indice2 = indice2
        self.exp = exp
        self.linea = linea
        self.columna = columna

class AsignacionArrayMulti(Instruccion) :
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''
    def __init__(self, id, indice, indice2, indice3, exp,linea, columna) :
        self.id = id
        self.indice = indice
        self.indice2 = indice2
        self.indice3 = indice3
        self.exp = exp
        self.linea = linea
        self.columna = columna

class AsignacionTipo(Instruccion) :
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''
    def __init__(self, id, exp, tipo,linea, columna) :
        self.id = id
        self.exp = exp
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

class If(Instruccion) : 
    '''
        Esta clase representa la instrucción if.
        La instrucción if recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class IfElse(Instruccion) : 
    '''
        Esta clase representa la instrucción if-else.
        La instrucción if-else recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
        a ejecutar si la expresión lógica es falsa.
    '''

    def __init__(self, expLogica, instrIfVerdadero = [], instrIfFalso = []) :
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso

class IfElseIF(Instruccion) : 
    '''
        Esta clase representa la instrucción if-else.
        La instrucción if-else recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
        a ejecutar si la expresión lógica es falsa.
    '''

    def __init__(self, expLogica1, expLogica2, instrIfVerdadero = [], instrIfFalso = []) :
        self.expLogica1 = expLogica1
        self.expLogica2 = expLogica2
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso

class Funcion(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, id, linea , columna, parametros = [], instrucciones = []) :
        self.id = id
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

class LlamadaFuncion(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, id, linea , columna, parametros = []) :
        self.id = id
        self.parametros = parametros
        self.linea = linea
        self.columna = columna


class Retorno(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, linea , columna, exp) :
        self.exp = exp
        self.linea = linea
        self.columna = columna


class Break(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, linea , columna, exp) :
        self.exp = exp
        self.linea = linea
        self.columna = columna


class Continue(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, linea , columna, exp) :
        self.exp = exp
        self.linea = linea
        self.columna = columna

class Lista_elif(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, linea , columna, lista_elif = []) :
        self.lista_elif = lista_elif
        self.linea = linea
        self.columna = columna

class Global(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, linea , columna, exp ) :
        self.exp = exp
        self.linea = linea
        self.columna = columna