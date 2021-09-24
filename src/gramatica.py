
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
    'Struct' : 'ESTRUCTURA',
    'mutable' : 'MUTABLE',
    'log10' : 'LOG10',
    'log' : 'LOG',
    'sin' : 'SEN',
    'cos' : 'COS',
    'tan' : 'TAN',
    'sqrt' : 'SQRT',
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
    'float':'R_DECIMAL',
    'typeof':'TYPE',
    'push':'PUSH',
    'pop':'POP',
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
t_COMA      = r','
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
import ply.lex as lex
from salida import Salida, Salida_Consola
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
    )

# Definición de la gramática

from expresiones import *
from instrucciones import *


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
                        | if_else_instr
                        | if_elseif_instr
                        | funcion_instr
                        | llamada_funcion_instr PTCOMA
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
    if t[1] == 'print'  :t[0] = Imprimir(t[3])
    elif t[1] == 'println'  :t[0] = Imprimirln(t[3])


def p_instruccion_retornar(t) :
    '''retorno_inst     : RETORNO  expresion  PTCOMA
                        | RETORNO  PTCOMA
    '''
    if t[2] == ';'  :t[0] = Retorno(t.lineno(1),t.lexpos(1),ExpresionDobleComilla("nothing"))
    else: t[0] = Retorno(t.lineno(1),t.lexpos(1),t[2])

def p_instruccion_romper(t) :
    '''break_inst       : BREAK PTCOMA
    '''
    t[0] = Break(t.lineno(1),t.lexpos(1),"break")

def p_instruccion_continuar(t) :
    '''continue_inst       : CONTINUE PTCOMA
    '''
    t[0] = Continue(t.lineno(1),t.lexpos(1),"continue")

def p_instruccion_definicion(t) :
    '''definicion_instr   : LOCAL asignacion_instr
                          | GLOBAL asignacion_instr
    '''
    if t[1] == "global": t[0] =Global(t.lineno(1),t.lexpos(1),t[2])

def p_asignacion_instr(t) :
    '''asignacion_instr   : ID IGUAL expresion PTCOMA
                          | ID IGUAL expresion DOSPT tipo_var PTCOMA
                          | ID CORIZQ expresion CORDER IGUAL expresion PTCOMA
                        
    '''
    if t[4] == ';': t[0] =Asignacion(t[1], t[3], t.lineno(1),t.lexpos(1))
    elif t[4] == '::'  :t[0] = AsignacionTipo(t[1], t[3],t[5],t.lineno(1),t.lexpos(1))
    elif t[2] == '[' :t[0] = AsignacionArray(t[1],t[3], t[6],t.lineno(1),t.lexpos(1))
        


def p_asignacion_bi_instr(t) :
    '''asignacion_instr       : ID CORIZQ expresion CORDER CORIZQ expresion CORDER IGUAL expresion PTCOMA
    '''
    t[0] = AsignacionArrayBi(t[1],t[3], t[6], t[9],t.lineno(1),t.lexpos(1))

def p_asignacion_multi_instr(t) :
    '''asignacion_instr       : ID CORIZQ expresion CORDER CORIZQ expresion CORDER CORIZQ expresion CORDER IGUAL expresion PTCOMA
    '''
    t[0] = AsignacionArrayMulti(t[1],t[3], t[6], t[9], t[12],t.lineno(1),t.lexpos(1))

def p_tipo_var(t) :
    '''tipo_var   : ENTERO64
                  | DECIMAL64
                  | BOOLEANO
                  | CHAR
                  | STRING
    '''
    if t[1] == 'int64': t[0] = TIPO_DATO.INT
    elif t[1] == 'float64': t[0] = TIPO_DATO.FLOAT
    elif t[1] == 'string': t[0] = TIPO_DATO.STRING
    elif t[1] == 'char': t[0] = TIPO_DATO.CHAR
    elif t[1] == 'bool': t[0] = TIPO_DATO.BOOL
    
def p_mientras_instr(t) :
    'mientras_instr     : MIENTRAS expresion_logica instrucciones END PTCOMA'
    t[0] =Mientras(t[2], t[3])

def p_for_instr(t) :
    '''for_instr     : FOR ID IN expresion PUNTOS expresion instrucciones END PTCOMA
                     | FOR ID IN expresion instrucciones END PTCOMA
                     '''
    if t[5] == ":": t[0] =ForRango(ExpresionDobleComilla(t[2]),t[4], t[6],t.lineno(1), t.lexpos(1),t[7])
    else: t[0] =ForExp(ExpresionDobleComilla(t[2]) ,t[4],t.lineno(1), t.lexpos(1),t[5])

def p_if_instr(t) :
    'if_instr           : IF expresion_logica instrucciones END PTCOMA'
    t[0] =If(t[2], t[3])
    

def p_if_else_instr(t) :
    'if_else_instr      : IF  expresion_logica instrucciones ELSE instrucciones END PTCOMA'
    t[0] =IfElse(t[2], t[3], t[5])

def p_lista_elseif_instr(t) :
    '''if_elseif_instr    : lista_elif   '''
    t[0] =Lista_elif(t.lineno(1),t.lexpos(1),t[1])

def p_elif_else_instr(t) :
    'lista_elif      : lista_elif ELSEIF expresion_logica instrucciones ELSE instrucciones END PTCOMA'
    t[1].append(IfElse(t[3], t[4], t[6]))
    t[0] = t[1]

def p_if_elseif_instr(t) :
    'lista_elif      : IF expresion_logica instrucciones '
    t[0] = [If(t[2], t[3])]

def p_elif_instr(t) :
    'lista_elif    : lista_elif ELSEIF expresion_logica instrucciones END PTCOMA'
    t[1].append(If(t[3], t[4]))
    t[0] = t[1]

def p_elif_recursivo_instr(t) :
    'lista_elif    : lista_elif ELSEIF expresion_logica instrucciones'
    t[1].append(If(t[3], t[4]))
    t[0] = t[1]


def p_list_exp_instr(t) :
    '''l_exp      : l_exp COMA expresion 
    '''
    t[1].append(t[3])
    t[0] = t[1]


def p_expresiones_expresion(t) :
    'l_exp    : expresion '
    t[0] = [t[1]]

def p_funcion_instr(t) :
    '''funcion_instr   : FUNC ID PARIZQ PARDER instrucciones END PTCOMA
                       | FUNC ID PARIZQ parametros PARDER instrucciones END PTCOMA'''
    if t[4] == ')': t[0] = Funcion(t[2],t.lineno(1), t.lexpos(1), [], t[5])
    else :t[0] = Funcion(t[2],t.lineno(1), t.lexpos(1), t[4], t[6])

def p_llamada_funcion_instr(t) :
    '''llamada_funcion_instr   : ID PARIZQ PARDER 
                       | ID PARIZQ l_exp PARDER '''
    if t[3] == ')': t[0] = LlamadaFuncion(t[1],t.lineno(1), t.lexpos(1), [])
    else :t[0] = LlamadaFuncion(t[1],t.lineno(1), t.lexpos(1), t[3])


def p_parametros_funcion_instr(t) :
    '''parametros   : parametros COMA ID '''
    t[1].append(Asignacion(t[3],ExpresionDobleComilla("nothing"), t.lineno(1),t.lexpos(1)))
    t[0] = t[1]


def p_parametros_parametro_instr(t) : 
    '''parametros   :  ID '''
    t[0] = [Asignacion(t[1],ExpresionDobleComilla("nothing"), t.lineno(1),t.lexpos(1))]
         
         

def p_expresion_binaria(t):
    '''expresion_numerica : expresion_numerica MAS expresion_numerica
                        | expresion_numerica MENOS expresion_numerica
                        | expresion_numerica POR expresion_numerica
                        | expresion_numerica POR expresion
                        | expresion_numerica DIVIDIDO expresion_numerica

                        | len_inst MAS expresion_numerica
                        | len_inst MENOS expresion_numerica
                        | len_inst POR expresion_numerica
                        | len_inst POR expresion
                        | len_inst DIVIDIDO expresion_numerica
                        
                        | expresion_numerica MOD expresion_numerica
                        | expresion_numerica POTENCIA expresion_numerica
                        | LOG10 PARIZQ expresion_numerica PARDER
                        | LOG PARIZQ expresion_numerica COMA expresion_numerica PARDER
                        | SEN PARIZQ expresion_numerica PARDER
                        | COS PARIZQ expresion_numerica PARDER
                        | TAN PARIZQ expresion_numerica PARDER
                        | SQRT PARIZQ expresion_numerica PARDER
                        '''
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '%': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MOD)
    elif t[2] == '^': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POTENCIAL)
    elif t[1] == 'log10': t[0] = ExpresionUnaria(t[3], OPERACION_ARITMETICA.LOG10)
    elif t[1] == 'log': t[0] = ExpresionBinaria(t[3],t[5], OPERACION_ARITMETICA.LOG)
    elif t[1] == 'sin': t[0] = ExpresionUnaria(t[3], OPERACION_ARITMETICA.SEN)
    elif t[1] == 'cos': t[0] = ExpresionUnaria(t[3], OPERACION_ARITMETICA.COS)
    elif t[1] == 'tan': t[0] = ExpresionUnaria(t[3], OPERACION_ARITMETICA.TAN)
    elif t[1] == 'sqrt': t[0] = ExpresionUnaria(t[3], OPERACION_ARITMETICA.SQRT)

def p_expresion_unaria(t):
    'expresion_numerica : MENOS expresion_numerica %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])

def p_expresion_agrupacion(t):
    'expresion_numerica : PARIZQ expresion_numerica PARDER'
    t[0] = t[2]

def p_expresion_agrupacion2(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion_numerica : ENTERO
                        | DECIMAL'''
    t[0] = ExpresionNumero(t[1])

def p_expresion_id(t):
    'expresion_numerica   : ID'
    t[0] = ExpresionIdentificador(t[1])

def p_expresion_array(t):
    'expresion_numerica   : ID CORIZQ expresion CORDER'
    t[0] = LlamadaArray(t[1], t[3], t.lineno(1),t.lexpos(1))

def p_expresion_arraybi(t):
    'expresion_numerica   : ID CORIZQ expresion CORDER CORIZQ expresion CORDER'
    t[0] = LlamadaArrayBi(t[1], t[3], t[6], t.lineno(1),t.lexpos(1))

def p_expresion_arraymulti(t):
    'expresion_numerica   : ID CORIZQ expresion CORDER CORIZQ expresion CORDER CORIZQ expresion CORDER'
    t[0] = LlamadaArrayMulti(t[1], t[3], t[6], t[9], t.lineno(1),t.lexpos(1))


def p_expresion_cadena(t) :
    'expresion     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])


def p_expresion_vector(t) :
    'expresion     : CORIZQ l_exp CORDER'
    t[0] = ExpresionArray(t.lineno(1), t.lexpos(1),t[2])

def p_lista_array(t):
    'expresion :   CORIZQ l_array_bidimencional CORDER'
    t[0] = ExpresionArrayBi(t.lineno(1), t.lexpos(1),t[2])

def p_expresion_vectorbi(t) :
    'l_array_bidimencional     :  l_array_bidimencional COMA expresion '
    t[1].append(t[3])
    t[0] = t[1]
    
def p_expresiones_expresion2(t) :
    'l_array_bidimencional    : expresion '
    t[0] = [t[1]]

def p_lista_array(t):
    'expresion :   CORIZQ l_array_multidimencional CORDER'
    t[0] = ExpresionArrayMulti(t.lineno(1), t.lexpos(1),t[2])

def p_expresion_vectorbi(t) :
    'l_array_multidimencional     :  l_array_multidimencional COMA expresion '
    t[1].append(t[3])
    t[0] = t[1]
    
def p_expresiones_expresion2(t) :
    'l_array_multidimencional    : expresion '
    t[0] = [t[1]]











def p_expresion_len(t) :
    'len_inst     : LEN PARIZQ expresion PARDER'
    t[0] = ExpresionLength(t[3])

def p_operacion_cadena(t) :
    '''expresion     : UPPER PARIZQ expresion PARDER
                     | LOWER PARIZQ expresion PARDER
                     | LEN PARIZQ expresion PARDER
                     | PARSE PARIZQ tipo_var COMA expresion PARDER
                     | TRUNC PARIZQ expresion PARDER
                     | R_DECIMAL PARIZQ expresion PARDER
                     | STRING PARIZQ expresion PARDER
                     | TYPE PARIZQ expresion PARDER
                     | PUSH PARIZQ expresion PARDER
                     | POP PARIZQ expresion PARDER
                     | llamada_funcion_instr
    '''
    if t[1] == "uppercase" :t[0] = ExpresionUpperCase(t[3])
    elif t[1] == "lowercase": t[0] = ExpresionLowerCase(t[3])
    elif t[1] == "length": t[0] = ExpresionLength(t[3])
    elif t[1] == "parse": t[0] = ExpresionParse(t[5],t[3],t.lineno(1),t.lexpos(1))
    elif t[1] == "trunc": t[0] = ExpresionTrunc(t[3],t.lineno(1),t.lexpos(1))
    elif t[1] == "float": t[0] = ExpresionFloat(t[3],t.lineno(1),t.lexpos(1))
    elif t[1] == "string": t[0] = ExpresionString(t[3],t.lineno(1),t.lexpos(1))
    elif t[1] == "typeof": t[0] = ExpresionType(t[3],t.lineno(1),t.lexpos(1))
    else:
        t[0] = t[1]


def p_expresion_cadena_potencia(t) :
    'expresion     : CADENA POTENCIA ENTERO'
    t[0] = ExpresionDobleComillaPotencia(t[1],t[3])
 

def p_expresion_caracter(t) :
    'expresion     : CARACTER'
    t[0] = ExpresionComillasSimples(t[1])

def p_expresion_nothing(t) :
    'expresion     : NULO'
    t[0] = ExpresionDobleComilla("nothing")

def p_expresion_cadena_numerico(t) :
    'expresion     : expresion_numerica'
    t[0] = ExpresionCadenaNumerico(t[1])

def p_expresion_cadena_logico(t) :
    'expresion     : expresion_logica'
    t[0] = ExpresionCadenaBooleano(t[1])

def p_expresion_booleana(t) :
    '''expresion_bool     : FALSO
                     | VERDADERO            
    '''
    if t[1] == "true": t[0] = ExpresionBooleano(True)
    elif t[1] == "false": t[0] = ExpresionBooleano(False)


def p_expresion_booleana_anadida(t) :
    'expresion_numerica     : expresion_bool        '
    t[0] = t[1]

def p_expresion_logica(t) :
    '''expresion_logica : expresion_logica AND expresion_logica
                        | expresion_logica OR expresion_logica
                        | NOT expresion_logica

                        | expresion_bool AND expresion_bool
                        | expresion_bool OR expresion_bool
                        | NOT expresion_bool

                        | expresion_logica AND expresion_bool
                        | expresion_logica OR expresion_bool

                        | expresion_bool AND expresion_logica
                        | expresion_bool OR expresion_logica

                        | PARIZQ expresion_logica PARDER
                        | expresion MAYQUE expresion
                        | expresion MENQUE expresion
                        | expresion IGUALQUE expresion
                        | expresion NIGUALQUE expresion
                        | expresion MENIGQUE expresion
                        | expresion MAYIGQUE expresion
                        
                        '''
    if t[2] == '>'    : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == '<'  : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == '==' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[1] == '(' : t[0] = t[2]
    elif t[2] == '!=' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE)
    elif t[2] == '<=' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENORIG_QUE)
    elif t[2] == '>=' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYORIG_QUE)
    elif t[2] == '&&' : t[0] = ExpresionRelacional(t[1], t[3], OPERACION_LOGICA.AND)
    elif t[2] == '||' : t[0] = ExpresionRelacional(t[1], t[3], OPERACION_LOGICA.OR)
    elif t[1] == '!' : t[0] = ExpresionRelacionalUnario(t[2], OPERACION_LOGICA.NOT)

def p_expresion_concatenacion(t) :
    'expresion     : expresion POR expresion'
    t[0] = ExpresionConcatenar(t[1], t[3])
    
def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)