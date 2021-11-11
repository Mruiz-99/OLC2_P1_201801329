
reservadas = {
    'print' : 'IMPRIMIR',
    'println' : 'IMPRIMIRSALTO',
    'while' : 'MIENTRAS',
    'if' : 'IF',
    'else' : 'ELSE',
    'elseif':'ELSEIF',
    'local' : 'LOCAL',
    'global' : 'GLOBAL',
    'nothing' : 'NULO',
    'true' : 'VERDADERO',
    'false' : 'FALSO',
    'int64' : 'ENTERO64',
    'float64' : 'DECIMAL64',
    'bool' : 'BOOLEANO',
    'char' : 'CHAR',
    'string' : 'STRING',
    'struct' : 'ESTRUCTURA',
    'mutable' : 'MUTABLE',
    'uppercase':'UPPER',
    'lowercase':'LOWER',
    'end':'END',
    'length':'LEN',
    'function':'FUNC',
    'return':'RETORNO',
    'break':'BREAK',
    'continue':'CONTINUE',
    'parse':'PARSE',
    'trunc':'TRUNC',
    'for':'FOR',
    'in':'IN'

}

tokens  = [
    'PTCOMA',
    'LLAVIZQ',
    'LLAVDER',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MENQUE',
    'MAYQUE',
    'MENIGQUE',
    'MAYIGQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'CARACTER',
    'ID',
    'DOSPT',
    'COMA',
    'MOD',
    'OR',
    'NOT',
    'AND',
    'POTENCIA',
    'PUNTOS',
    'PUNTO',
    'CORIZQ',
    'CORDER'
] + list(reservadas.values())

# Tokens
t_PTCOMA    = r';'
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_MENIGQUE  = r'<='
t_MAYIGQUE  = r'>='
t_IGUALQUE  = r'=='
t_NIGUALQUE = r'!='
t_DOSPT     = r'::'
t_PUNTOS     = r':'
t_PUNTO     = r'\.'
t_COMA      = r'\,'
t_NOT       = r'!'
t_AND       = r'&&'
t_OR        = r'\|\|'
t_MOD       =r'\%'
t_POTENCIA  =r'\^'
t_CORIZQ    =r'\['
t_CORDER  =r']'
#Funcion que reconoce numeros con decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t
#Funcion que reconoce numeros enteros
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

#Funcion que reconoce una cadena de caracteres
def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

#Funcion que reconoce un caracter
def t_CARACTER(t):
    r'\'.?\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

#Funcion que reconoce identificadores
def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"
#Funcion que reconoce los saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#Funcion para los errores lexicos     
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
from Instruction.Variables.Declaracion import Declaracion
import ply.lex as lex
from salida import Salida, Salida_Consola
from Instruction.Conditional.If import *
from Instruction.Loops.While import *
from Instruction.Loops.For import *
from Instruction.Loops.Break import *
from Instruction.Loops.Continue import *

from Instruction.Structs.AssignAccess import *
from Instruction.Structs.CreateStruct import *
from Instruction.Structs.DeclareStruct import *
from Instruction.Structs.StructAttr import *

from Instruction.Functions.Function import *
from Instruction.Functions.Param import *
from Instruction.Functions.ReturnST import *

from Abstract.Expresion import *
from Abstract.Return import *
from Abstract.Instruccion import *

from Expressions.Trunc import *
from Expressions.UpperCase import *
from Expressions.LowerCase import *
from Expressions.Logicas import *
from Expressions.Access import *
from Expressions.AccessVector import *
from Expressions.AccessStruct import *
from Expressions.Aritmeticas import *
from Expressions.CallFunc import *
from Expressions.Literal import *
from Expressions.Literal2 import *
from Expressions.Relacional import *
from Instruction.Print import *
from Instruction.Variables.Declaracion import *



lexer = lex.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','NOT'),
    ('left', 'IGUALQUE', 'NIGUALQUE', 'MENQUE', 'MAYQUE', 'MAYIGQUE', 'MENIGQUE'), 
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO','MOD'),
    ('nonassoc', 'POTENCIA'),
    ('right','UMENOS'),
    ('right','UNOT'),
    )

# Definición de la gramática

from expresiones import *


def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]


def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : imprimir_instr
                        | definicion_instr
                        | asignacion_instr
                        | mientras_instr
                        | if_instr
                        | funcion_instr
                        | llamada_funcion_instr PTCOMA
                        | createStruct 
                        | declareStructST PTCOMA
                        | assignAccessST PTCOMA 
                        | retorno_inst
                        | break_inst
                        | continue_inst
                        | for_instr'''
    t[0] = t[1]

def p_instruccion_imprimir(t) :
    '''imprimir_instr     : IMPRIMIR PARIZQ expresion PARDER PTCOMA
                          | IMPRIMIRSALTO PARIZQ expresion PARDER PTCOMA
                          | IMPRIMIR PARIZQ l_exp PARDER PTCOMA
                          | IMPRIMIRSALTO PARIZQ l_exp PARDER PTCOMA
    '''
    
    if t[1] == 'print'  :t[0] = Print(t[3], t.lineno(1), t.lexpos(0))
    elif t[1] == 'println'  : t[0] = Print(t[3], t.lineno(1), t.lexpos(0), True)
        


def p_instruccion_retornar(t) :
    '''retorno_inst     : RETORNO  expresion  PTCOMA
                        | RETORNO  PTCOMA
    '''
    if len(t) == 3:
        t[0] = ReturnST(None, t.lineno(1), t.lexpos(1))
    else:
        t[0] = ReturnST(t[2], t.lineno(1), t.lexpos(1))

def p_instruccion_romper(t) :
    '''break_inst       : BREAK PTCOMA
    '''
    t[0] = Break(t.lineno(1),t.lexpos(1))

def p_instruccion_continuar(t) :
    '''continue_inst       : CONTINUE PTCOMA
    '''
    t[0] = Continue(t.lineno(1),t.lexpos(1))

def p_instruccion_definicion(t) :
    '''definicion_instr   : LOCAL asignacion_instr
                          | GLOBAL asignacion_instr
    '''
    #if t[1] == "global": t[0] =Global(t.lineno(1),t.lexpos(1),t[2])

def p_asignacion_instr(t) :
    '''asignacion_instr   : ID IGUAL expresion PTCOMA
                          | ID IGUAL expresion DOSPT tipo_var PTCOMA
                        
    '''
    if t[4] == ';': t[0] = Declaracion(t[1], t[3], None, t.lineno(1), t.lexpos(1))
    elif t[4] == '::'  :t[0] = Declaracion(t[1], t[3], t[5], t.lineno(1), t.lexpos(1))

        
        

def p_tipo_var(t) :
    '''tipo_var   : ENTERO64
                  | DECIMAL64
                  | BOOLEANO
                  | CHAR
                  | STRING
    '''
    if t[1] == 'int64': t[0] = Type.INT
    elif t[1] == 'float64': t[0] = Type.FLOAT
    elif t[1] == 'string': t[0] = Type.STRING
    elif t[1] == 'char': t[0] = Type.CHAR
    elif t[1] == 'bool': t[0] = Type.BOOLEAN
    
def p_mientras_instr(t) :
    'mientras_instr     : MIENTRAS expresion instrucciones END PTCOMA'
    t[0] = While(t[2], t[3], t.lineno(1), t.lexpos(1))

def p_for_instr(t) :
    '''for_instr     : FOR ID IN expresion PUNTOS expresion instrucciones END PTCOMA
                     | FOR ID IN expresion instrucciones END PTCOMA
                     '''
    if t[5] == ":": t[0] =For(t[2],t[4],t[6],t[7])
    else: t[0] =For(t[4],t[5], t.lineno(1), t.lexpos(1)) 
 
def p_if_instr(t) :
    'if_instr   : IF expresion instrucciones END PTCOMA'
    t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(1))

def p_if_else_instr(t) :
    'if_instr   : IF  expresion instrucciones ELSE instrucciones END PTCOMA'
    t[0] =If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])

def p_lista_elseif_instr(t) :
    '''if_instr    : IF expresion instrucciones elseIfList END PTCOMA'''
    t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])

def p_elseIfList(t):
    '''elseIfList   : ELSEIF expresion instrucciones
                    | ELSEIF expresion instrucciones ELSE instrucciones
                    | ELSEIF expresion instrucciones elseIfList'''
    if len(t) == 4:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(1))
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])
    elif len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])

# STRUCTS
# CREATE STRUCT
def p_createStruct(t):
    'createStruct : ESTRUCTURA ID attList END PTCOMA'
    t[0] = CreateStruct(t[2], t[3], t.lineno(1), t.lexpos(1))

def p_attList(t):
    '''attList :  attList PTCOMA ID DOSPT tipo_var PTCOMA
                | attList PTCOMA ID PTCOMA
                | ID
                | ID DOSPT tipo_var'''
    if len(t) == 4:
        t[0] = [StructAttr(t[1], t[3], t.lineno(1), t.lexpos(1))]
    elif len(t) == 2:
        t[0] = [StructAttr(t[1], None, t.lineno(1), t.lexpos(1))]
    elif len(t) == 5:
        t[1].append(StructAttr(t[3], None, t.lineno(1), t.lexpos(1)))
        t[0] = t[1]
    else:
        t[1].append(StructAttr(t[3], t[6], t.lineno(1), t.lexpos(1)))
        t[0] = t[1]

# DECLARE STRUCT
def p_declareStruct(t):
    'declareStructST : ID DOSPT ID'
    t[0] = DeclareStruct(t[1], t[3], t.lineno(1), t.lexpos(1))

# ASSIGN ACCESS
def p_assignAccess(t):
    'assignAccessST : ID PUNTO ID IGUAL expresion'
    t[0] = AssignAccess(t[1], t[3], t[5], t.lineno(1), t.lexpos(1))





def p_list_exp_instr(t) :
    '''l_exp      : l_exp COMA expresion 
    '''
    t[1].append(t[3])
    t[0] = t[1]


def p_expresiones_expresion(t) :
    'l_exp    : expresion '
    t[0] = [t[1]]


def p_funcion_instr(t) :
    '''funcion_instr   : FUNC ID PARIZQ PARDER DOSPT tipo_var instrucciones END PTCOMA
                       | FUNC ID PARIZQ parametros PARDER DOSPT tipo_var instrucciones END PTCOMA'''
    if len(t) == 8:
        t[0] = Function(t[2], [], t[6], t[7], t.lineno(1), t.lexpos(1))
    else:
        t[0] = Function(t[2], t[4], t[7], t[8], t.lineno(1), t.lexpos(1))

def p_decParams(t):
    '''parametros :       parametros COMA ID tipo_var
                        | ID tipo_var'''
    
    if len(t) == 3:
        t[0] = [Param(t[1], t[2], t.lineno(1), t.lexpos(1))]
    else:
        t[1].append(Param(t[3], t[4], t.lineno(1), t.lexpos(1)))
        t[0] = t[1]


def p_llamada_funcion_instr(t) :
    '''llamada_funcion_instr   :  ID PARIZQ PARDER
                                | ID PARIZQ expList PARDER '''
    if len(t) == 4:
        t[0] = CallFunc(t[1], [], t.lineno(1), t.lexpos(1))
    else:
        t[0] = CallFunc(t[1], t[3], t.lineno(1), t.lexpos(1)) 
    

# CALL PARAMS
def p_callparams(t):
    '''expList :  expList COMA expresion
                | expresion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]


# expresiones como Array
def p_expresion_array_lista(t):
    '''expArray :  expArray COMA expresion
                | expresion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = Literal(t[1],Type.ARRAY, t.lineno(1), t.lexpos(1))

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion
                  | expresion OR expresion
                  | expresion AND expresion
                  | expresion IGUALQUE expresion
                  | expresion NIGUALQUE expresion
                  | expresion MAYQUE expresion
                  | expresion MENQUE expresion
                  | expresion MAYIGQUE expresion
                  | expresion MENIGQUE expresion
                  | expresion POTENCIA expresion
                  | expresion MOD expresion
                  | finalExp
                  '''
    if len(t) == 2: 
        t[0] = t[1]
    else:
        if t[2] == '+'  : 
            t[0] = Aritmeticas(t[1], t[3], OPERACION_ARITMETICA.MAS, t.lineno(2), t.lexpos(1))
        elif t[2] == '-':
            t[0] = Aritmeticas(t[1], t[3], OPERACION_ARITMETICA.MENOS, t.lineno(2), t.lexpos(1))
        elif t[2] == '*': 
            t[0] = Aritmeticas(t[1], t[3], OPERACION_ARITMETICA.POR, t.lineno(2), t.lexpos(1))
        elif t[2] == '/': 
            t[0] = Aritmeticas(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO, t.lineno(2), t.lexpos(1))
        elif t[2] == '^': 
            t[0] = Aritmeticas(t[1], t[3], OPERACION_ARITMETICA.POTENCIAL, t.lineno(2), t.lexpos(1))
        elif t[2] == '%': 
            t[0] = Aritmeticas(t[1], t[3], OPERACION_ARITMETICA.MOD, t.lineno(2), t.lexpos(1))
        elif t[2] == '==': 
            t[0] = Relacionales(t[1], t[3], OPERACION_RELACIONALES.IGUAL,t.lineno(2), t.lexpos(1) )
        elif t[2] == '!=': 
            t[0] = Relacionales(t[1], t[3], OPERACION_RELACIONALES.DIFERENTE,t.lineno(2), t.lexpos(1) )
        elif t[2] == '>': 
            t[0] = Relacionales(t[1], t[3], OPERACION_RELACIONALES.MAYOR_QUE,t.lineno(2), t.lexpos(1) )
        elif t[2] == '<': 
            t[0] = Relacionales(t[1], t[3], OPERACION_RELACIONALES.MENOR_QUE,t.lineno(2), t.lexpos(1) )
        elif t[2] == '>=': 
            t[0] = Relacionales(t[1], t[3], OPERACION_RELACIONALES.MAYORIG_QUE,t.lineno(2), t.lexpos(1) )
        elif t[2] == '<=':
            t[0] = Relacionales(t[1], t[3], OPERACION_RELACIONALES.MENORIG_QUE,t.lineno(2), t.lexpos(1) )
        elif t[2] == '||':
            t[0] = Logicas(t[1], t[3],OPERACION_LOGICAS.OR, t.lineno(2), t.lexpos(1))
        elif t[2] == '&&': 
            t[0] = Logicas(t[1], t[3],OPERACION_LOGICAS.AND, t.lineno(2), t.lexpos(1))


def p_finalExp(t):
    '''finalExp : llamada_funcion_instr
                | accessST'''
    if t.slice[1].type == "llamada_funcion_instr" or t.slice[1].type == "accessST":
        t[0] = t[1]

    

def p_accessST(t):
    '''accessST : ID PUNTO ID'''
    print('entro')
    t[0] = AccessStruct(t[1], t[3], t.lineno(1), t.lexpos(1))




#operador aritmetico UNOT
def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                    | NOT expresion %prec UNOT'''
    if t[1] == '-':
        t[0] = Aritmeticas(None, t[2], OPERACION_ARITMETICA.UMENOS, t.lineno(1), t.lexpos(1))
    elif t[1] == '!':
        t[0] = Logicas(t[2], None,OPERACION_LOGICAS.NOT,  t.lineno(1), t.lexpos(1))

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_identificador(t):
    'expresion : ID'
    t[0] = Access(t[1], t.lineno(1),t.lexpos(1))

def p_expresion_identificador_array(t):
    'expresion : ID CORIZQ ENTERO CORDER'
    t[0] = AccessVector(t[1], t[3],t.lineno(1),t.lexpos(1))

'''
def p_expresion_struct(t):
    'expresion : ID PUNTO asignacion_params'
    #t[0] = Struct(t[1], t.lineno(1), t.lexpos(1), t[3])
'''
def p_expresion_entero(t):
    'expresion : ENTERO'
    t[0] = Literal(int(t[1]), Type.INT, t.lineno(1), t.lexpos(1))

def p_expresion_vector(t):
    'expresion : CORIZQ l_exp CORDER'
    t[0] = Literal(t[2], Type.ARRAY, t.lineno(1), t.lexpos(1))


def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = Literal(float(t[1]), Type.FLOAT, t.lineno(1), t.lexpos(1))

def p_expresion_char(t):
    'expresion : CARACTER'
    t[0] = Literal(t[1], Type.CHAR, t.lineno(1), t.lexpos(1))

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = Literal(str(t[1]), Type.STRING, t.lineno(1), t.lexpos(1))

def p_expresion_true(t):
    'expresion : VERDADERO'
    t[0] = Literal(True,Type.BOOLEAN, t.lineno(1), t.lexpos(1))

def p_expresion_false(t):
    'expresion : FALSO'
    t[0] = Literal(False, Type.BOOLEAN, t.lineno(1), t.lexpos(1))





'''def p_expresion_len(t) :
    'len_inst     : LEN PARIZQ expresion PARDER'
    #t[0] = ExpresionLength(t[3])'''

def p_operacion_cadena(t) :
    '''expresion     : UPPER PARIZQ expresion PARDER
                     | LOWER PARIZQ expresion PARDER
                     | LEN PARIZQ expresion PARDER
                     | PARSE PARIZQ tipo_var COMA expresion PARDER
                     | TRUNC PARIZQ expresion PARDER
                     | STRING PARIZQ expresion PARDER'''
    
    if t[1] == "uppercase" :t[0] = UpperCase(t[3],Type.STRING, t.lineno(1), t.lexpos(1))
    elif t[1] == "lowercase": t[0] = LowerCase(t[3],Type.STRING, t.lineno(1), t.lexpos(1))
    #elif t[1] == "length": t[0] = ExpresionLength(t[3])
    #elif t[1] == "parse": t[0] = ExpresionParse(t[5],t[3],t.lineno(1),t.lexpos(1))
    elif t[1] == "trunc": t[0] = Trunc(t[3],t.lineno(1),t.lexpos(1))
    #elif t[1] == "string": t[0] = ExpresionString(t[3],t.lineno(1),t.lexpos(1))


def p_expresion_cadena_potencia(t) :
    '''expresion     : CADENA POTENCIA ENTERO'''
    t[0] = Literal2(t[1],t[3],Type.STRING,t.lineno(1), t.lexpos(1))

    
def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :

    return parser.parse(input)
'''
f = open("src/entrada.txt", "r")
entrada = f.read()
print("ARCHIVO DE ENTRADA:")
print("")
print(entrada)
print("")
print("ARCHIVO DE SALIDA:")
from Symbol.Generator import * 
genAux = Generator()
genAux.cleanAll()
generador = genAux.getInstance()
instruccion = parse(entrada)
env = Environment(None)
for inst in instruccion:
    valor = inst.compile(env)
print(str(instruccion))
'''