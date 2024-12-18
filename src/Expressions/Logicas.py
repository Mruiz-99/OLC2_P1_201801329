from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Generator import Generator
from enum import Enum

class OPERACION_LOGICAS(Enum) :
    AND = 0
    OR = 1
    NOT = 2

class Logicas(Expresion): 

    def __init__(self, left, right, type, line, column):
        Expresion.__init__(self, line, column)
        self.left = left
        self.right = right
        self.type = type
    
    def compile(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.addComment("INICIO EXPRESION LOGICA")

        self.checkLabels()
        lblAndOr = ''

        if self.type == OPERACION_LOGICAS.AND:
            lblAndOr = self.left.trueLbl = generator.newLabel()
            self.right.trueLbl = self.trueLbl
            self.left.falseLbl = self.right.falseLbl = self.falseLbl
        elif self.type == OPERACION_LOGICAS.OR:
            self.left.trueLbl = self.right.trueLbl = self.trueLbl
            lblAndOr = self.left.falseLbl = generator.newLabel()
            self.right.falseLbl = self.falseLbl
        elif self.type == OPERACION_LOGICAS.NOT:
            self.left.falseLbl = self.trueLbl
            

            self.left.trueLbl = self.falseLbl 
            
            #TREE, table
            lblNot = self.left.compile(environment)
            if lblNot.type != Type.BOOLEAN:
                return Exception ("Semantico", "No se puede utilizar la expresion booleana en: ", self.fila, self.column)

            lbltrue = lblNot.trueLbl
            lblfalse = lblNot.falseLbl
            lblNot.trueLbl = lblfalse
            lblNot.falseLbl = lbltrue
            self.type = Type.BOOLEAN
            return lblNot


        left = self.left.compile(environment)
        if left.type != Type.BOOLEAN:
            print("No se puede utilizar en expresion booleana")
            return
        generator.putLabel(lblAndOr)
        right = self.right.compile(environment)
        if right.type != Type.BOOLEAN:
            print("No se puede utilizar en expresion booleana")
            return
        generator.addComment("FINALIZO EXPRESION LOGICA")
        generator.addSpace()
        ret = Return(None, Type.BOOLEAN, False)
        ret.trueLbl = self.trueLbl
        ret.falseLbl = self.falseLbl
        return ret
    
    def checkLabels(self):
        genAux = Generator()
        generator = genAux.getInstance()
        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()