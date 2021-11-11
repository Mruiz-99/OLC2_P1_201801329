from Abstract.Expresion import *
from Abstract.Return import *
from Expressions.CallFunc import CallFunc
from Symbol.Generator import Generator
from enum import Enum
import uuid

class OPERACION_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MOD = 5
    POTENCIAL = 6
    UMENOS = 7

class Aritmeticas(Expresion):
    
    def __init__(self, left, right, type, line, column):
        Expresion.__init__(self, line, column)
        self.left = left
        self.right = right
        self.type = type
    
    def compile(self, env):
        genAux = Generator()
        generator = genAux.getInstance()
        if self.left != None:
            leftValue = self.left.compile(env)
        if isinstance(self.right, CallFunc):
            self.right.GuardarTemp(generator,env,[leftValue.value])
            rightValue = self.right.compile(env)
            if isinstance(rightValue, Exception):
                return rightValue
            self.right.RecuperacionTemp(generator,env,[leftValue.value])
        else:
            rightValue = self.right.compile(env)
            if isinstance(rightValue, Exception):
                return rightValue
        temp = generator.addTemp()
        op = ''
        if(self.type == OPERACION_ARITMETICA.MAS):
            op = '+'
        elif(self.type == OPERACION_ARITMETICA.MENOS):
            op = '-'
        elif(self.type == OPERACION_ARITMETICA.POR):
            op = '*'
        elif(self.type == OPERACION_ARITMETICA.DIVIDIDO):
            op = '/'  
        elif(self.type == OPERACION_ARITMETICA.MOD):  
            op='%'
            tipo = ''
            if(leftValue.type == Type.INT and rightValue.type == Type.INT):
                tipo = Type. INT
            elif(leftValue.type == Type.INT and rightValue.type == Type.FLOAT):
                tipo = Type. FLOAT
            elif(leftValue.type == Type.FLOAT and rightValue.type == Type.INT):
                tipo = Type. FLOAT
            elif(leftValue.type == Type.FLOAT and rightValue.type == Type.FLOAT):
                tipo = Type. FLOAT
            else:
                return Exception("Semantico", "Operacion 'MOD' no permitida en: ", self.fila, self.column)
            temp = generator.addTemp()
            generator.setImport("math")

            L1 = generator.newLabel()
            L2 = generator.newLabel()

            generator.addIf(rightValue.value,'0','!=',L1)
            generator.addPrint("c", 77) #M
            generator.addPrint("c", 97) #a
            generator.addPrint("c", 116) #t
            generator.addPrint("c", 104) #h
            generator.addPrint("c", 69) #E
            generator.addPrint("c", 114) #r
            generator.addPrint("c", 114) #r
            generator.addPrint("c", 111) #o
            generator.addPrint("c", 114) #r
            generator.addPrint("c", 10)
            generator.addExp(temp,'0','','')
            generator.addGoto(L2)
            generator.putLabel(L1)
            generator.addModulo(temp, leftValue.value, rightValue.value)
            generator.putLabel(L2)
            return Return(temp, tipo, True)
                
        elif (self.type == OPERACION_ARITMETICA.UMENOS):  # 0-5
            op = '-'
            temp = generator.addTemp()
            
            if rightValue.type == Type.INT:
                generator.addExp(temp, '0', rightValue.value, op)
                return Return(temp, Type.INT, True)
            
            if rightValue.type == Type.FLOAT:
                generator.addExp(temp, '0', rightValue.value, op)
                return Return(temp, Type.FLOAT, True)

            return Exception("Semantico", "Operacion 'Resta' no permitida en: ", self.fila, self.column)
        if (self.type == OPERACION_ARITMETICA.POTENCIAL):
            
            generator.fPotencia()
            paramTemp = generator.addTemp()

            generator.addExp(paramTemp, 'P', env.size, '+')
            generator.addExp(paramTemp, paramTemp, '1', '+')
            generator.setStack(paramTemp, leftValue.value)
            
            generator.addExp(paramTemp, paramTemp, '1', '+')
            generator.setStack(paramTemp, rightValue.value)
            
            generator.newEnv(env.size)
            generator.callFun('potencia')

            temp = generator.addTemp()
            generator.getStack(temp, 'P')
            generator.retEnv(env.size)

            return Return(temp, Type.INT, True)

            
        else:
            if(op=='*' and leftValue.type == Type.STRING and rightValue.type == Type.STRING):
                generator.fconcatString()
                paramTemp = generator.addTemp()

                generator.addExp(paramTemp, 'P', env.size, '+')
                generator.addExp(paramTemp, paramTemp, '1', '+')
                generator.setStack(paramTemp, leftValue.value)
                
                generator.addExp(paramTemp, paramTemp, '1', '+')
                generator.setStack(paramTemp, rightValue.value)
                
                generator.newEnv(env.size)
                generator.callFun('concatenacion')

                temp = generator.addTemp()
                generator.getStack(temp, 'P')
                generator.retEnv(env.size)

                '''
                
                '''
                return Return(temp, Type.STRING, True)
            else:
                if(op=='/'):
                    L1 = generator.newLabel()
                    L2 = generator.newLabel()

                    generator.addIf(rightValue.value,'0','!=',L1)
                    generator.addPrint("c", 77) #M
                    generator.addPrint("c", 97) #a
                    generator.addPrint("c", 116) #t
                    generator.addPrint("c", 104) #h
                    generator.addPrint("c", 69) #E
                    generator.addPrint("c", 114) #r
                    generator.addPrint("c", 114) #r
                    generator.addPrint("c", 111) #o
                    generator.addPrint("c", 114) #r
                    generator.addPrint("c", 10)
                    generator.addExp(temp,'0','','')
                    generator.addGoto(L2)
                    generator.putLabel(L1)
                    generator.addExp(temp, leftValue.value, rightValue.value, op)
                    generator.putLabel(L2)
                    return Return(temp, Type.FLOAT, True)
                else:
                    generator.addExp(temp, leftValue.value, rightValue.value, op)
                    return Return(temp, Type.INT, True)
               
            