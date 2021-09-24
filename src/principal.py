
import math
from re import S
import types
from tabla_simbolos import *
from expresiones import *
from instrucciones import *
from App import *
from math import * 
import sys

pilaFuncion = []
pilaCiclos = []


sys.setrecursionlimit(100000) 

def procesar_imprimir(instr, ts, salida) :
    #TENEMOS QUE MANDAR A RESOLVER CADENA 
    print('>', str(resolver_cadena(instr.cad, ts, salida)), end=" ")
    salida.agregar('>'+ str(resolver_cadena(instr.cad, ts, salida)))
    #setConsola('>'+ resolver_cadena(instr.cad, ts))

 
def procesar_imprimirln(instr, ts, salida) :
    #TENEMOS QUE MANDAR A RESOLVER CADENA 
    
    print('> ', str(resolver_cadena(instr.cad, ts, salida)))
    salida.agregar('>'+ str(resolver_cadena(instr.cad, ts, salida)) +'~')
    #setConsola('>'+ resolver_cadena(instr.cad, ts)+"\n")

def procesar_global(instr, ts, salida) :
    while ts.anterior !="":
        if(ts.obtener(instr.exp.id) != "0"):
            procesar_asignacion(instr.exp, ts, salida)
            ts = ts.anterior
    if(ts.obtener(instr.exp.id) != "0"):
        return procesar_asignacion(instr.exp, ts, salida)

def procesar_definicion(instr, ts) :
    simbolo = Simbolo(instr.id, TIPO_DATO.NUMERO, 0)      # inicializamos con 0 como valor por defecto ID TIPO;
    ts.agregar(simbolo)

def procesar_asignacion(instr, ts, salida) :
    if isinstance(instr, Asignacion):
        val = resolver_cadena(instr.exp, ts, salida)
        if type(val) is int:
            tipo = TIPO_DATO.INT
        elif type(val) is float:
            tipo = TIPO_DATO.FLOAT
        elif type(val) is str:
            tipo = TIPO_DATO.STRING
        elif type(val) is bool:
            tipo = TIPO_DATO.BOOL
        elif type(val) is list:
            tipo = TIPO_DATO.ARRAY
        elif str.lower(val)=="nothing" :
            tipo = TIPO_DATO.NULO
        elif len(val) == 1:
            tipo = TIPO_DATO.CHAR  
        simbolo = Simbolo(instr.id, tipo, val)
        if ts.buscar(simbolo.id) == "0":    
            ts.agregar(simbolo)
            return
        else: 
            ts.actualizar(simbolo)
            return
    if isinstance(instr, AsignacionArray):
        val = resolver_cadena(instr.exp, ts, salida)
        indice = resolver_cadena(instr.indice,ts,salida)
        tipo = TIPO_DATO.ARRAY
        array = ts.obtener(instr.id).valor
        if array == "0":    
            print("Error semantico, el array no existe, verifique el nombre correspondiente")
            salida.agregar('>'+ "Error semantico, el array no existe, verifique el nombre correspondiente"+'~')
            return
        else: 
            if indice >= 0:
                c = 0
                val_actual =[]
                for i in array:
                    if c == (indice-1):
                        val_actual.append(val)
                        c=c+1
                    else:
                        val_actual.append(i)
                        c=c+1
                #print(val_actual)
                simbolo = Simbolo(instr.id, tipo, val_actual)
                ts.actualizar(simbolo)
                while ts.anterior !="":
                    ts = ts.anterior
                    ts.actualizar(simbolo)
                return
            else:
                print("Error semantico, el indice del array no debe ser negativo")
                salida.agregar('>'+ "Error semantico, el indice del array no debe ser negativo"+'~')
                return
    if isinstance(instr, AsignacionArrayBi):
        val = resolver_cadena(instr.exp, ts, salida)
        indice = resolver_cadena(instr.indice,ts,salida)
        indice2 = resolver_cadena(instr.indice2,ts,salida)
        tipo = TIPO_DATO.ARRAY
        array = ts.obtener(instr.id).valor
        if array == "0":    
            print("Error semantico, el array no existe, verifique el nombre correspondiente")
            salida.agregar('>'+ "Error semantico, el array no existe, verifique el nombre correspondiente"+'~')
            return
        else:       
            if indice >= 0 and indice2 >=0:
                c = 0
                c2 = 0
                val_actual =[[],[]]
                for i in array:
                    for j in i:
                        if c == (indice-1) and c2 == (indice2-1):
                            val_actual[c].append(val)
                            print(c, " ", c2)
                            c2=c2+1
                        else:
                            val_actual[c].append(j)
                            print(c, " ", c2)
                            c2=c2+1
                    c = c + 1
                    c2=0
                print(val_actual)
                simbolo = Simbolo(instr.id, tipo, val_actual)
                ts.actualizar(simbolo)
                while ts.anterior !="":
                    ts = ts.anterior
                    ts.actualizar(simbolo)
                return
            else:
                print("Error semantico, el indice del array no debe ser negativo")
                salida.agregar('>'+ "Error semantico, el indice del array no debe ser negativo"+'~')
                return
    if isinstance(instr, AsignacionArrayMulti):
        val = resolver_cadena(instr.exp, ts, salida)
        indice = resolver_cadena(instr.indice,ts,salida)
        indice2 = resolver_cadena(instr.indice2,ts,salida)
        indice3 = resolver_cadena(instr.indice3,ts,salida)
        tipo = TIPO_DATO.ARRAY
        array = ts.obtener(instr.id).valor
        if array == "0":    
            print("Error semantico, el array no existe, verifique el nombre correspondiente")
            salida.agregar('>'+ "Error semantico, el array no existe, verifique el nombre correspondiente"+'~')
            return
        else:       
            if indice >= 0 and indice2 >=0 and indice3:
                c = 0
                c2 = 0
                c3 = 0
                val_actual =[[[],[]],[[],[]]]
                for i in array:
                    for j in i:
                        for k in j:
                            if c == (indice-1) and c2 == (indice2-1) and c3 == (indice3 - 1):
                                val_actual[c][c2].append(val)
                                c3=c3+1
                            else:
                                val_actual[c][c2].append(k)
                                print(c, " ", c2)
                                c3=c3+1
                        c2 = c2 + 1  
                        c3=0  
                    c = c + 1
                    c2=0
                print(val_actual)
                simbolo = Simbolo(instr.id, tipo, val_actual)
                ts.actualizar(simbolo)
                while ts.anterior !="":
                    ts = ts.anterior
                    ts.actualizar(simbolo)
                return
            else:
                print("Error semantico, el indice del array no debe ser negativo")
                salida.agregar('>'+ "Error semantico, el indice del array no debe ser negativo"+'~')
                return
            
        
    elif isinstance(instr, AsignacionTipo) :
        val = resolver_cadena(instr.exp, ts, salida)
        if type(val) is int:
            if instr.tipo == TIPO_DATO.INT:
                res = True
            else:
                res = False
                print("Error semantico, el valor no corresponde al tipo de dato")
                salida.agregar('>'+ "Error semantico, el valor no corresponde al tipo de dato"+'~')

        elif type(val) is float:
            if instr.tipo == TIPO_DATO.FLOAT:
                res = True
            else:
                res = False
                print("Error semantico, el valor no corresponde al tipo de dato")
                salida.agregar('>'+ "Error semantico, el valor no corresponde al tipo de dato"+'~')
        elif type(val) is str:
            if instr.tipo == TIPO_DATO.STRING or instr.tipo == TIPO_DATO.CHAR:
                res = True
            else:
                res = False
                print("Error semantico, el valor no corresponde al tipo de dato")
                salida.agregar('>'+ "Error semantico, el valor no corresponde al tipo de dato"+'~')
        elif type(val) is bool:
            if instr.tipo == TIPO_DATO.BOOL:
                res = True
            else:
                res = False
                print("Error semantico, el valor no corresponde al tipo de dato")
                salida.agregar('>'+ "Error semantico, el valor no corresponde al tipo de dato"+'~')
        if res == True: 
            simbolo = Simbolo(instr.id, instr.tipo, val)
            if ts.buscar(simbolo.id) == "0":   
                ts.agregar(simbolo)
            else:
                ts.actualizar(simbolo)

def procesar_mientras(instr, ts, salida) :
    pilaCiclos.append("Ciclo")
    local = TablaDeSimbolos(ts,ts.simbolos)
    while resolver_expresion_logica(instr.expLogica, local, salida) :
        res =  procesar_instrucciones(instr.instrucciones, local, salida)
        if isinstance(res, Break):
            break
        elif isinstance(res, Continue):
            continue
        elif res:
            pilaCiclos.pop()
            return res
    ts.simbolos = local.simbolos
    pilaCiclos.pop()


def procesar_for_rango(instr, ts, salida) :
    pilaCiclos.append("Ciclo")
    local = TablaDeSimbolos(ts, ts.simbolos)
    desde = resolver_cadena(instr.desde,ts,salida)
    hasta = resolver_cadena(instr.hasta,ts, salida)
    procesar_asignacion(Asignacion(instr.expDeclarativa.val,instr.desde,0,0),local,salida)

    if desde < hasta:
        while resolver_expresion_logica(ExpresionLogica(ExpresionDobleComilla(local.obtener(instr.expDeclarativa.val).valor), ExpresionDobleComilla(hasta), OPERACION_LOGICA.MENORIG_QUE), local, salida) :
            res =  procesar_instrucciones(instr.instrucciones, local, salida)
            procesar_asignacion(Asignacion(instr.expDeclarativa.val,ExpresionDobleComilla(local.obtener(instr.expDeclarativa.val).valor+1),0,0),local,salida)
            if isinstance(res, Break):
                break
            elif isinstance(res, Continue):
                continue
            elif res:
                pilaCiclos.pop()
                return res
    else:
        while resolver_expresion_logica(ExpresionLogica(ExpresionDobleComilla(local.obtener(instr.expDeclarativa.val).valor), ExpresionDobleComilla(hasta), OPERACION_LOGICA.MAYORIG_QUE), local, salida) :
            res =  procesar_instrucciones(instr.instrucciones, local, salida)
            procesar_asignacion(Asignacion(instr.expDeclarativa.val,ExpresionDobleComilla(local.obtener(instr.expDeclarativa.val).valor-1),0,0),local,salida)
            if isinstance(res, Break):
                break
            elif isinstance(res, Continue):
                continue
            elif res:
                pilaCiclos.pop()
                return res
    ts.simbolos = local.simbolos
    pilaCiclos.pop()


def procesar_for_expresion(instr, ts, salida) :
    pilaCiclos.append("Ciclo")
    local = TablaDeSimbolos(ts, ts.simbolos)
    cadena = resolver_cadena(instr.exp,ts,salida)
    if isinstance(instr.exp, ExpresionDobleComilla) or isinstance(instr.exp, ExpresionCadenaNumerico) or isinstance(instr.exp, ExpresionArray) or isinstance(instr.exp, LlamadaArray) or isinstance(instr.exp, LlamadaArrayBi) or isinstance(instr.exp, LlamadaArrayMulti):
        for i in cadena:
            procesar_asignacion(Asignacion(instr.expDeclarativa.val,ExpresionDobleComilla(i),0,0),local,salida)
            res =  procesar_instrucciones(instr.instrucciones, local, salida)
            if isinstance(res, Break):
                break
            elif isinstance(res, Continue):
                continue
            elif res:
                pilaCiclos.pop()
                return res
    ts.simbolos = local.simbolos
    pilaCiclos.pop()    

def procesar_funcion(instr, ts, salida) :
    simbolo = Simbolo(instr.id, "funcion", instr) 
    if ts.buscar(simbolo.id) == "0":   
        ts.agregar(simbolo)
    else:
        print("Error semantico, el nombre de la funcion ya ha sido utilizado")
        salida.agregar('>'+ "Error semantico, el nombre de la funcion ya ha sido utilizado"+'~')

def procesar_llamada_funcion(instr, ts, salida) :
    #sdfsdf
    if ts.buscar(instr.id) != "0":   
        simboloFuncion = ts.buscar(instr.id)
    else:
        print("Error semantico, no se encontro la funcion escrita, en la linea: "+str(instr.linea)+", en la columna: "+str(instr.columna))
        salida.agregar('>'+ "Error semantico, no se encontro la funcion escrita, en la linea: "+str(instr.linea)+", en la columna: "+str(instr.columna)+'~')
        return 
    pilaFuncion.append(instr.id)
    local = TablaDeSimbolos(ts, ts.simbolos) 
    retorno = "Error" 
    c=0 
    lista_cantidades = []
    for exp in instr.parametros:
        lista_cantidades.append(resolver_cadena(exp,ts,salida))
    for param in simboloFuncion.valor.parametros:
        procesar_asignacion(Asignacion(param.id,ExpresionNumero(lista_cantidades[c]),0,0),local,salida)
        c = c+1
    res = procesar_instrucciones(simboloFuncion.valor.instrucciones,local,salida)
    if res: 
        exp = resolver_cadena(res, local, salida)
        retorno = exp
        c2 = 0
        for param in simboloFuncion.valor.parametros:
            #cuando lista_cantidades sea una lista entonces que actualice
            if type(lista_cantidades[c2]) is list:
                simbolo = Simbolo(instr.parametros[c2].exp.id, TIPO_DATO.ARRAY,ts.obtener(param.id).valor)
                ts.actualizar(simbolo)
                while ts.anterior !="":
                    ts = ts.anterior
                    ts.actualizar(simbolo)
            c2 = c2 +1

    else: 
        retorno = "nothing"
        c2 = 0
        for param in simboloFuncion.valor.parametros:
            #cuando lista_cantidades sea una lista entonces que actualice
            if type(lista_cantidades[c2]) is list:
                simbolo = Simbolo(instr.parametros[c2].exp.id, TIPO_DATO.ARRAY,ts.obtener(param.id).valor)
                ts.actualizar(simbolo)
                while ts.anterior !="":
                    ts = ts.anterior
                    ts.actualizar(simbolo)
            c2 =c2 +1
    pilaFuncion.pop() 
    return retorno

def procesar_if(instr, ts, salida) :
    val = resolver_expresion_logica(instr.expLogica, ts, salida)
    if val :
        local = TablaDeSimbolos(ts,ts.simbolos)
        return procesar_instrucciones(instr.instrucciones, local, salida)

def procesar_if_else(instr, ts, salida) :
    val = resolver_expresion_logica(instr.expLogica, ts, salida)
    if val :
        local = TablaDeSimbolos(ts,ts.simbolos)
        return procesar_instrucciones(instr.instrIfVerdadero, local, salida)
    else :
        local = TablaDeSimbolos(ts,ts.simbolos) 
        return procesar_instrucciones(instr.instrIfFalso, local, salida)

def procesar_lista_elif(instr, ts, salida) :
    for sentencia in instr.lista_elif:
        if isinstance(sentencia,IfElse):
            val = resolver_expresion_logica(sentencia.expLogica, ts, salida)
            if val :
                local = TablaDeSimbolos(ts,ts.simbolos)
                return procesar_instrucciones(sentencia.instrIfVerdadero, local, salida)
            else :
                local = TablaDeSimbolos(ts, ts.simbolos) 
                return procesar_instrucciones(sentencia.instrIfFalso, local, salida)
        elif isinstance(sentencia,If):
            val = resolver_expresion_logica(sentencia.expLogica, ts, salida)
            if val :
                local = TablaDeSimbolos(ts, ts.simbolos)
                return procesar_instrucciones(sentencia.instrucciones, local, salida)

#RESOLVEMOS LA CADENA VALIDAMOS 
def resolver_cadena(expCad, ts, salida) :
    #RESOLVEMOS
    
    if isinstance(expCad, ExpresionConcatenar) :
        exp1 = resolver_cadena(expCad.exp1, ts, salida)
        exp2 = resolver_cadena(expCad.exp2, ts, salida)
        return exp1 + exp2
    #VALIDAMOS QUE TIPO DE EXPRESION ES
    elif isinstance(expCad, ExpresionDobleComilla) :
        return expCad.val
    elif isinstance(expCad, ExpresionBinaria) :
        return resolver_expresion_aritmetica(expCad,ts, salida)
    elif isinstance(expCad, ExpresionIdentificador) :
        return resolver_expresion_aritmetica(expCad,ts, salida)
    elif isinstance(expCad, LlamadaArrayBi) :
        return resolver_expresion_aritmetica(expCad,ts, salida)
    elif isinstance(expCad, LlamadaArray) :
        return resolver_expresion_aritmetica(expCad,ts, salida)
    elif isinstance(expCad, LlamadaArrayMulti) :
        return resolver_expresion_aritmetica(expCad,ts, salida)
    elif isinstance(expCad, ExpresionArray):
        lista_cantidades = []
        for exp in expCad.exp:
            lista_cantidades.append(resolver_cadena(exp,ts,salida))
        return lista_cantidades
    elif isinstance(expCad, ExpresionArrayBi):
        lista_cantidades = [[]]
        c=0
        for exp in expCad.exp:
            for exp2 in exp:
                lista_cantidades[c].append(resolver_cadena(exp2,ts,salida))
            c = c + 1
        return lista_cantidades
    elif isinstance(expCad, ExpresionArrayMulti):
        lista_cantidades = [[[]]]
        c=0
        c2 = 0
        for exp in expCad.exp:
            for exp2 in exp:
                for exp3 in exp2:
                    lista_cantidades[c][c2].append(resolver_cadena(exp3,ts,salida))
                c2 = c2 + 1
            c = c + 1
            c2 = 0
        return lista_cantidades
    elif isinstance(expCad, ExpresionDobleComillaPotencia) :
        return expCad.val1 * expCad.val2
    #VALIDAMOS QUE TIPO DE EXPRESION ES
    elif isinstance(expCad, ExpresionComillasSimples) :
        return expCad.val  
    #VALIDAMOS QUE TIPO DE EXPRESION ES
    elif isinstance(expCad, ExpresionBooleano) : 
        return bool(expCad.val)
    elif isinstance(expCad, ExpresionNegativo) :   
        exp = resolver_expresion_aritmetica(expCad.exp, ts, salida)
        return exp * -1
    #VALIDAMOS QUE TIPO DE EXPRESION ES
    elif isinstance(expCad, ExpresionCadenaBooleano) :
        return resolver_expresion_logica(expCad.exp, ts, salida)
    elif isinstance(expCad, ExpresionNumero) :
        return resolver_expresion_aritmetica(expCad, ts, salida)
    #MANDAMOS A RESOLVER LA EXPRESION
    elif isinstance(expCad, ExpresionCadenaNumerico) :
        return resolver_expresion_aritmetica(expCad.exp, ts, salida)
    #PASAMOS A MAYUSCULAS LAS LETRAS DE UNA CADENA
    elif isinstance(expCad, ExpresionUpperCase) :
        if isinstance(expCad.exp, ExpresionDobleComilla) :
            return str.upper(expCad.exp.val)
        elif isinstance(expCad.exp, ExpresionCadenaNumerico):
            return str.upper(resolver_expresion_aritmetica(expCad.exp.exp, ts, salida))
        else:
            return str.upper(resolver_cadena(expCad.exp,ts,salida))
    elif isinstance(expCad, ExpresionLowerCase) :
        if isinstance(expCad.exp, ExpresionDobleComilla) :
            return str.lower(expCad.exp.val)
        elif isinstance(expCad.exp, ExpresionCadenaNumerico):
            return str.lower(resolver_expresion_aritmetica(expCad.exp.exp, ts, salida))
        else:
            return str.lower(resolver_cadena(expCad.exp,ts,salida))
    elif isinstance(expCad, ExpresionLength) :
        if isinstance(expCad.exp, ExpresionDobleComilla) :
            return len(expCad.exp.val)
        elif isinstance(expCad.exp, ExpresionCadenaNumerico):
            return len(resolver_expresion_aritmetica(expCad.exp.exp, ts, salida))
        else:
            return len(resolver_cadena(expCad.exp,ts,salida))
            
    elif isinstance(expCad, ExpresionParse):
        if isinstance(expCad.exp, ExpresionDobleComilla) :
            if expCad.tipo == TIPO_DATO.INT:
                return int(expCad.exp.val)
            elif expCad.tipo == TIPO_DATO.FLOAT:
                return float(expCad.exp.val)
            else:
                print("Error semantico, no se acepta este tipo de dato en el parse, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna))
                salida.agregar('>'+ "Error semantico, no se acepta este tipo de dato en el parse, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna)+'~')
                return
        elif isinstance(expCad.exp, ExpresionCadenaNumerico):
            if expCad.tipo == TIPO_DATO.INT:
                return int(resolver_expresion_aritmetica(expCad.exp.exp, ts, salida))
            elif expCad.tipo == TIPO_DATO.FLOAT:
                return float(resolver_expresion_aritmetica(expCad.exp.exp, ts, salida))
            else:
                print("Error semantico, no se acepta este tipo de dato en el parse, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna))
                salida.agregar('>'+ "Error semantico, no se acepta este tipo de dato en el parse, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna)+'~')
                return
        else: 
            if expCad.tipo == TIPO_DATO.INT:
                return int(resolver_cadena(expCad.exp,ts,salida))
            elif expCad.tipo == TIPO_DATO.FLOAT:
                return float(resolver_cadena(expCad.exp,ts,salida))
            else:
                print("Error semantico, no se acepta este tipo de dato en el parse, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna))
                salida.agregar('>'+ "Error semantico, no se acepta este tipo de dato en el parse, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna)+'~')
                return    
    elif isinstance(expCad, ExpresionTrunc) :
        if isinstance(expCad.exp, ExpresionCadenaNumerico):
            if isinstance(expCad.exp.exp, ExpresionNumero):
                if type(expCad.exp.exp.val) is float:
                    return int(resolver_expresion_aritmetica(expCad.exp.exp, ts, salida))
                else:
                    print("Error semantico, no se acepta este tipo de dato en el trunc, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna))
                    salida.agregar('>'+ "Error semantico, no se acepta este tipo de dato en el trunc, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna)+'~')
                    return
            else:
                if type(resolver_expresion_aritmetica(expCad.exp.exp,ts,salida)) is float:
                    return int(resolver_expresion_aritmetica(expCad.exp.exp,ts,salida))
                else:
                    print("Error semantico, no se acepta este tipo de dato en el trunc, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna))
                    salida.agregar('>'+ "Error semantico, no se acepta este tipo de dato en el trunc, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna)+'~')
                    return
        else:
            print("Error semantico, no se acepta este tipo de dato en el trunc, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna))
            salida.agregar('>'+ "Error semantico, no se acepta este tipo de dato en el trunc, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna)+'~')
            return
    elif isinstance(expCad, ExpresionFloat) :
        if isinstance(expCad.exp, ExpresionCadenaNumerico):
            if isinstance(expCad.exp.exp, ExpresionNumero):
                if type(expCad.exp.exp.val) is int:
                    return float(resolver_expresion_aritmetica(expCad.exp.exp, ts, salida))
                else:
                    print("Error semantico, no se acepta este tipo de dato en el float, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna))
                    salida.agregar('>'+ "Error semantico, no se acepta este tipo de dato en el float, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna)+'~')
                    return
            else:
                if type(resolver_expresion_aritmetica(expCad.exp.exp,ts,salida)) is int:
                    return float(resolver_expresion_aritmetica(expCad.exp.exp,ts,salida))
                else:
                    print("Error semantico, no se acepta este tipo de dato en el float, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna))
                    salida.agregar('>'+ "Error semantico, no se acepta este tipo de dato en el float, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna)+'~')
                    return
        else:
            print("Error semantico, no se acepta este tipo de dato en el trunc, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna))
            salida.agregar('>'+ "Error semantico, no se acepta este tipo de dato en el float, en la linea: "+str(expCad.linea)+", en la columna: "+str(expCad.columna)+'~')
            return
    elif isinstance(expCad, ExpresionString) :
        if isinstance(expCad.exp, ExpresionDobleComilla) :
            return str(expCad.exp.val)
        elif isinstance(expCad.exp, ExpresionCadenaNumerico) :
            return str(resolver_cadena(expCad.exp,ts,salida))
        elif isinstance(expCad.exp, ExpresionConcatenar) :
            return str(resolver_cadena(expCad.exp,ts,salida))
        else:
            return str(resolver_expresion_aritmetica(expCad.exp,ts,salida))
    elif isinstance(expCad, ExpresionType) :
        if isinstance(expCad.exp, ExpresionDobleComilla) :
            if type(expCad.exp.val) is str:
                return "string"
            elif type(expCad.exp.val) is int:
                return "int"
            elif type(expCad.exp.val) is float:
                return "float"
            elif type(expCad.exp.val) is bool:
                return "bool"
            elif type(expCad.exp.val) is str and len(expCad.exp.val)==1:
                return "char"
            elif type(expCad.exp.val) is list:
                return "array" 
        elif isinstance(expCad.exp, ExpresionComillasSimples) :
            if type(expCad.exp.val) is str and len(expCad.exp.val)==1:
                return "char"
        elif isinstance(expCad.exp, ExpresionCadenaNumerico) :
            if type(resolver_cadena(expCad.exp,ts,salida)) is str:
                return "string"
            elif type(resolver_cadena(expCad.exp,ts,salida)) is int:
                return "int"
            elif type(resolver_cadena(expCad.exp,ts,salida)) is float:
                return "float"
            elif type(resolver_cadena(expCad.exp,ts,salida)) is bool:
                return "bool"
            elif type(resolver_cadena(expCad.exp,ts,salida)) is str and len(resolver_cadena(expCad.exp,ts,salida))==1:
                return "char"
            elif type(resolver_cadena(expCad.exp,ts,salida)) is list:
                return "array"   
        elif isinstance(expCad.exp, ExpresionConcatenar) :
            if type(resolver_cadena(expCad.exp,ts,salida)) is str:
                return "string"
            elif type(resolver_cadena(expCad.exp,ts,salida)) is int:
                return "int"
            elif type(resolver_cadena(expCad.exp,ts,salida)) is float:
                return "float"
            elif type(resolver_cadena(expCad.exp,ts,salida)) is bool:
                return "bool"
            elif type(resolver_cadena(expCad.exp,ts,salida)) is str and len(resolver_cadena(expCad.exp,ts,salida))==1:
                return "char"
            elif type(resolver_cadena(expCad.exp,ts,salida)) is list:
                return "array"    
        else:
            if type(resolver_expresion_aritmetica(expCad.exp,ts,salida)) is str:
                return "string"
            elif type(resolver_expresion_aritmetica(expCad.exp,ts,salida)) is int:
                return "int"
            elif type(resolver_expresion_aritmetica(expCad.exp,ts,salida)) is float:
                return "float"
            elif type(resolver_expresion_aritmetica(expCad.exp,ts,salida)) is bool:
                return "bool"
            elif type(resolver_expresion_aritmetica(expCad.exp,ts,salida)) is str and len(resolver_expresion_aritmetica(expCad.exp,ts,salida))==1:
                return "char"
            elif type(resolver_expresion_aritmetica(expCad.exp,ts,salida)) is list:
                return "array"    

    elif isinstance(expCad, LlamadaFuncion) :
        return procesar_llamada_funcion(expCad, ts, salida)
    elif type(expCad) is list: 
        res = ""
        for exp in expCad:
            res += str(resolver_cadena(exp,ts,salida))
        return res
    else :
        print('Error: Expresión cadena no válida')


def resolver_expresion_logica(expLog, ts, salida) :
    if isinstance(expLog, ExpresionLogica) :
        if isinstance(expLog.exp1, ExpresionCadenaNumerico) :
            expLog.exp1 = expLog.exp1.exp
        if isinstance(expLog.exp2, ExpresionCadenaNumerico) :
            expLog.exp2 = expLog.exp2.exp

        if isinstance(expLog.exp1, ExpresionBooleano) :
            exp1 = resolver_cadena(expLog.exp1, ts,salida)#10>6
        elif isinstance(expLog.exp1, ExpresionDobleComilla) :
            exp1 = expLog.exp1.val    
        else:
            exp1 = resolver_expresion_aritmetica(expLog.exp1, ts,salida)

        if isinstance(expLog.exp2, ExpresionBooleano) :
            exp2 = resolver_cadena(expLog.exp2, ts,salida)#10>6
        elif isinstance(expLog.exp2, ExpresionDobleComilla) :
            exp2 = expLog.exp2.val
        else: 
            exp2 = resolver_expresion_aritmetica(expLog.exp2, ts,salida)

        if expLog.operador == OPERACION_LOGICA.MAYOR_QUE : return exp1 > exp2
        if expLog.operador == OPERACION_LOGICA.MENOR_QUE : return exp1 < exp2
        if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
        if expLog.operador == OPERACION_LOGICA.DIFERENTE : return exp1 != exp2
        if expLog.operador == OPERACION_LOGICA.MAYORIG_QUE : return exp1 >= exp2
        if expLog.operador == OPERACION_LOGICA.MENORIG_QUE : return exp1 <= exp2

    elif isinstance(expLog, ExpresionRelacional) :
        exp1 = resolver_expresion_logica(expLog.exp1, ts, salida)#10>6
        exp2 = resolver_expresion_logica(expLog.exp2, ts, salida)
        if expLog.operador == OPERACION_LOGICA.AND : return True if(exp1 and exp2) else False
        if expLog.operador == OPERACION_LOGICA.OR : return True if(exp1 or exp2) else False
        if expLog.operador == OPERACION_LOGICA.NOT : return True if(not(exp1)) else False 
    elif isinstance(expLog, ExpresionRelacionalUnario) :
        exp1 = resolver_expresion_logica(expLog.exp1, ts, salida)#10>6
        if expLog.operador == OPERACION_LOGICA.NOT : return True if(not(exp1)) else False   
    #VALIDAMOS QUE TIPO DE EXPRESION ES
    elif isinstance(expLog, ExpresionBooleano) :
        return expLog.val


def resolver_expresion_aritmetica(expNum, ts,salida) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts,salida)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts,salida)
        if type(exp1) is not str and type(exp2) is not str:
            if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
            if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
            if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
            if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
            if expNum.operador == OPERACION_ARITMETICA.MOD : return exp1 % exp2
            if expNum.operador == OPERACION_ARITMETICA.POTENCIAL : return exp1**exp2
            if expNum.operador == OPERACION_ARITMETICA.LOG : return math.log(exp2,exp1)
        
        else:
            if type(exp1) is str and exp2 is None:
                if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 + " "
            elif exp1 is None and type(exp2) is str:
                if expNum.operador == OPERACION_ARITMETICA.POR : 
                    return " " + exp2  
                
            else:
                
                if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 + exp2
                else: 
                    print("Error semantico, esta operacion no es permitida")
                    salida.agregar('>'+ "Error semantico, esta operacion no es permitida"+'~')
 
        
    elif isinstance(expNum, ExpresionUnaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts, salida)
        if expNum.operador == OPERACION_ARITMETICA.SEN : return math.sin(exp1)
        if expNum.operador == OPERACION_ARITMETICA.COS : return math.cos(exp1) 
        if expNum.operador == OPERACION_ARITMETICA.TAN : return math.tan(exp1)
        if expNum.operador == OPERACION_ARITMETICA.SQRT : return math.sqrt(exp1)
        if expNum.operador == OPERACION_ARITMETICA.LOG10 : return math.log10(exp1)
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts, salida)
        return exp * -1
    elif isinstance(expNum, ExpresionDobleComilla) :
        return expNum.val
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionLength) :
        return len(resolver_cadena(expNum.exp,ts,salida))
    elif isinstance(expNum, ExpresionIdentificador) :
        identificador = ts.obtener(expNum.id)
        if identificador != "0":
            return identificador.valor
    elif isinstance(expNum, LlamadaArray) :
        identificador = ts.obtener(expNum.id)
        if identificador != "0":
            indice = resolver_cadena(expNum.indice,ts,salida)
            if indice  <= len(identificador.valor):
                return identificador.valor[indice - 1]
            else:
                print("Error semantico, el indice esta afuera del rango del array")
                salida.agregar('>'+ "Error semantico, el indice esta afuera del rango del array"+'~')
                return
    elif isinstance(expNum, LlamadaArrayBi) :
        identificador = ts.obtener(expNum.id)
        if identificador != "0":
            indice = resolver_cadena(expNum.indice,ts,salida)
            indice2 = resolver_cadena(expNum.indice2,ts,salida)
            if indice  <= len(identificador.valor) and indice2 <= len(identificador.valor[0]) and indice  > 0 and indice2 > 0:
                return identificador.valor[indice - 1][indice2 -1]
            else:
                print("Error semantico, el indice esta afuera del rango del array")
                salida.agregar('>'+ "Error semantico, el indice esta afuera del rango del array"+'~')
                return
    elif isinstance(expNum, LlamadaArrayMulti) :
        identificador = ts.obtener(expNum.id)
        if identificador != "0":
            indice = resolver_cadena(expNum.indice,ts,salida)
            indice2 = resolver_cadena(expNum.indice2,ts,salida)
            indice3 = resolver_cadena(expNum.indice3,ts,salida)
            if indice  <= len(identificador.valor) and indice2 <= len(identificador.valor[0]) and indice3 <= len(identificador.valor[0][0]) and indice  > 0 and indice2 > 0 and indice3 >0:
                return identificador.valor[indice - 1][indice2 -1][indice3 -1 ]
            else:
                print("Error semantico, el indice esta afuera del rango del array")
                salida.agregar('>'+ "Error semantico, el indice esta afuera del rango del array"+'~')
                return
    elif isinstance(expNum, LlamadaFuncion) :
        return procesar_llamada_funcion(expNum, ts, salida)
    elif isinstance(expNum, ExpresionConcatenar) : 
        
        exp1 = resolver_cadena(expNum.exp1, ts, salida)
        exp2 = resolver_cadena(expNum.exp2, ts, salida)
        return exp1 + exp2
    elif isinstance(expNum, ExpresionBooleano) :
        print(expNum.val)
        return expNum.val

#RECORREMOS EL ARCHIVO DE ENTRADA CON LA FINALIDAD DE IR LELLENDO LOS OBJETOS E INSTRUCCIOENS

def procesar_instrucciones(instrucciones, ts, salida) :
    ## lista de instrucciones recolectadas
    #Validamos a donde va entrar
    retorno = None
    for instr in instrucciones :
        #VALIDAMOS A QUE TIPO DE INSTRUCCION 
        # TENEMOS QUE PASAR LA TABLA DE SIMBOLOS CON LA INSTRUCCION QUE CORRESPINDE 
        if isinstance(instr, Imprimir) :  procesar_imprimir(instr, ts, salida)
        elif isinstance(instr, Imprimirln) : procesar_imprimirln(instr, ts, salida)
        elif isinstance(instr, Definicion) : retorno = procesar_definicion(instr, ts, salida)
        elif isinstance(instr, Asignacion) : retorno = procesar_asignacion(instr, ts, salida)
        elif isinstance(instr, AsignacionTipo) : retorno = procesar_asignacion(instr, ts, salida)
        elif isinstance(instr, AsignacionArray) : retorno = procesar_asignacion(instr, ts, salida)
        elif isinstance(instr, AsignacionArrayBi) : retorno = procesar_asignacion(instr, ts, salida)
        elif isinstance(instr, AsignacionArrayMulti) : retorno = procesar_asignacion(instr, ts, salida)
        elif isinstance(instr, Mientras) : retorno = procesar_mientras(instr, ts, salida)
        elif isinstance(instr, ForExp) : retorno = procesar_for_expresion(instr, ts, salida)
        elif isinstance(instr, ForRango) : retorno = procesar_for_rango(instr, ts, salida)
        elif isinstance(instr, ForExp) : retorno = procesar_for_expresion(instr, ts, salida)
        elif isinstance(instr, If) : retorno = procesar_if(instr, ts, salida)
        elif isinstance(instr, IfElse) : retorno = procesar_if_else(instr, ts, salida)
        elif isinstance(instr, Lista_elif) :  retorno = procesar_lista_elif(instr, ts, salida)
        elif isinstance(instr, Funcion) : retorno = procesar_funcion(instr, ts, salida)
        elif isinstance(instr, Global) : retorno = procesar_global(instr, ts, salida)
        elif isinstance(instr, LlamadaFuncion) : 
            procesar_llamada_funcion(instr, ts, salida)
            retorno = None
        elif isinstance(instr, Retorno) : 
            if len(pilaFuncion)>0:
                retorno = instr.exp
            else:
               print("Error semantico, intruccion return fuera de una funcion, en la linea: "+str(instr.linea)+", en la columna: "+str(instr.columna))
               salida.agregar('>'+ "Error semantico, intruccion return fuera de una funcion, en la linea: "+str(instr.linea)+", en la columna: "+str(instr.columna)+'~') 
        elif isinstance(instr, Break) :
            if len(pilaCiclos)>0:
                return instr
            else:
                print("Error semantico, intruccion break fuera de un ciclo, en la linea: "+ str(instr.linea) +", en la columna: "+str(instr.columna))
                salida.agregar('>'+ "Error semantico, intruccion break fuera de un ciclo, en la linea: "+ str(instr.linea) +", en la columna: "+str(instr.columna)+'~') 
        elif isinstance(instr, Continue) :
            if len(pilaCiclos)>0:
                return instr
            else:
                print("Error semantico, intruccion continue fuera de un ciclo, en la linea: "+str(instr.linea)+", en la columna: "+str(instr.columna))
                salida.agregar('>'+ "Error semantico, intruccion continue fuera de un ciclo, en la linea: "+str(instr.linea)+", en la columna: "+str(instr.columna)+'~') 
        else : print('Error: instrucción no válida')
        if retorno:
            return retorno



