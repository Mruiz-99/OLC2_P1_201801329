from enum import Enum



class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''
class ExpresionBooleana:
    '''
        Esta clase representa una expresión booleana
    '''    
class ExpresionBinaria(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Aritmética Binaria.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionUnaria(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Aritmética Binaria.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, operador) :
        self.exp1 = exp1
        self.operador = operador

class ExpresionNegativo(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Aritmética Negativa.
        Esta clase recibe la expresion
    '''
    def __init__(self, exp) :
        self.exp = exp




class ExpresionNumero(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, val = 0) :
        self.val = val

class ExpresionBooleano(ExpresionBooleana) :
    '''
        Esta clase representa una expresión booleana.
    '''

    def __init__(self, val = False) :
        self.val = val

class ExpresionIdentificador(ExpresionNumerica) :
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self, id = "") :
        self.id = id

class ExpresionCadena :
    '''
        Esta clase representa una Expresión de tipo cadena.
    '''

class ExpresionConcatenar(ExpresionCadena) :
    '''
        Esta clase representa una Expresión de tipo cadena.
        Recibe como parámetros las 2 expresiones a concatenar
    '''

    def __init__(self, exp1, exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionDobleComilla(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas doble.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, val) :
        self.val = val
class ExpresionDobleComillaPotencia(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas doble.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, val1,val2) :
        self.val1 = val1
        self.val2 = val2

class ExpresionComillasSimples(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, val) :
        self.val = val   

class ExpresionUpperCase(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, exp) :
        self.exp = exp 

class ExpresionLowerCase(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, exp) :
        self.exp = exp  
class ExpresionLength(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, exp) :
        self.exp = exp  


class ExpresionParse(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, exp,tipo, linea, columna) :
        self.exp = exp        
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

class ExpresionTrunc(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, exp, linea, columna) :
        self.exp = exp      
        self.linea = linea
        self.columna = columna

class ExpresionFloat(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, exp, linea, columna) :
        self.exp = exp      
        self.linea = linea
        self.columna = columna

class ExpresionString(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, exp, linea, columna) :
        self.exp = exp      
        self.linea = linea
        self.columna = columna
class ExpresionType(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, exp, linea, columna) :
        self.exp = exp      
        self.linea = linea
        self.columna = columna

class ExpresionArray(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, linea, columna, exp =[] ) :
        self.exp = exp      
        self.linea = linea
        self.columna = columna

class ExpresionArrayBi(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, linea, columna, exp =[[]] ) :
        self.exp = exp      
        self.linea = linea
        self.columna = columna
class ExpresionArrayMulti(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, linea, columna, exp =[[[]]] ) :
        self.exp = exp      
        self.linea = linea
        self.columna = columna

class LlamadaArray(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, id, indice, linea, columna ) :
        self.id = id  
        self.indice = indice      
        self.linea = linea
        self.columna = columna


class LlamadaArrayBi(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, id, indice, indice2, linea, columna ) :
        self.id = id  
        self.indice = indice  
        self.indice2 = indice2      
        self.linea = linea
        self.columna = columna

class LlamadaArrayMulti(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, id, indice, indice2, indice3, linea, columna ) :
        self.id = id  
        self.indice = indice  
        self.indice2 = indice2 
        self.indice3 = indice3     
        self.linea = linea
        self.columna = columna


class ExpresionCadenaNumerico(ExpresionCadena) :
    '''
        Esta clase representa una expresión numérica tratada como cadena.
        Recibe como parámetro la expresión numérica
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionCadenaBooleano(ExpresionCadena) :
    '''
        Esta clase representa una expresión booleana tratada como cadena.
        Recibe como parámetro la expresión numérica
    '''
    def __init__(self, exp) :
        self.exp = exp


class ExpresionLogica() :
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionRelacional() :
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
class ExpresionRelacionalUnario() :
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, operador) :
        self.exp1 = exp1
        self.operador = operador        