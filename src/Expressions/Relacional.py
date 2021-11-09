from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Generator import Generator
from enum import Enum

class OPERACION_RELACIONALES(Enum) :
    MAYOR_QUE = 0
    MENOR_QUE = 1
    MAYORIG_QUE = 2
    MENORIG_QUE = 3
    IGUAL = 4
    DIFERENTE = 5
    
class Relacionales(Expresion):
    
    def __init__(self, left, right, type, line, column):
        Expresion.__init__(self, line, column)
        self.left = left
        self.right = right
        self.type = type

    def compile(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.addComment("INICIO EXPRESION RELACIONAL")

        left = self.left.compile(environment)
        right = None

        result = Return(None, Type.BOOLEAN, False)

        if left.type != Type.BOOLEAN:
            right = self.right.compile(environment)
            if (left.type == Type.INT or left.type == Type.FLOAT) and (right.type == Type.INT or right.type == Type.FLOAT):
                self.checkLabels()
                generator.addIf(left.value, right.value, self.getOp(), self.trueLbl)
                generator.addGoto(self.falseLbl)
            elif left.type == Type.STRING and right.type == Type.STRING:
                print("Comparacion de cadenas")     # Únicamente se puede con igualdad o desigualdad
        else:
            gotoRight = generator.newLabel()
            leftTemp = generator.addTemp()

            generator.putLabel(left.trueLbl)
            generator.addExp(leftTemp, '1', '', '')
            generator.addGoto(gotoRight)

            generator.putLabel(left.falseLbl)
            generator.addExp(leftTemp, '0', '', '')

            generator.putLabel(gotoRight)

            right = self.right.compile(environment)
            if right.type != Type.BOOLEAN:
                print("Error, no se pueden comparar")
                return
            gotoEnd = generator.newLabel()
            rightTemp = generator.addTemp()

            generator.putLabel(right.trueLbl)
            
            generator.addExp(rightTemp, '1', '', '')
            generator.addGoto(gotoEnd)

            generator.putLabel(right.falseLbl)
            generator.addExp(rightTemp, '0', '', '')

            generator.putLabel(gotoEnd)

            self.checkLabels()
            generator.addIf(leftTemp, rightTemp, self.getOp(), self.trueLbl)
            generator.addGoto(self.falseLbl)

        generator.addComment("FIN DE EXPRESION RELACIONAL")
        generator.addSpace()
        result.trueLbl = self.trueLbl
        result.falseLbl = self.falseLbl

        return result     
    
    def checkLabels(self):
        genAux = Generator()
        generator = genAux.getInstance()
        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()

    def getOp(self):
        if self.type == OPERACION_RELACIONALES.MAYOR_QUE:
            return '>'
        elif self.type == OPERACION_RELACIONALES.MENOR_QUE:
            return '<'
        elif self.type == OPERACION_RELACIONALES.MAYORIG_QUE:
            return '>='
        elif self.type == OPERACION_RELACIONALES.MENORIG_QUE:
            return '<='
        elif self.type == OPERACION_RELACIONALES.IGUAL:
            return '=='
        elif self.type == OPERACION_RELACIONALES.DIFERENTE:
            return '!='