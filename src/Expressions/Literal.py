from Abstract.Expresion import *
from Abstract.Return import *
from Instruction.Print import Print
from Symbol.Generator import Generator
import uuid
class Literal(Expresion):

    def __init__(self, value, type, line, column):
        Expresion.__init__(self, line, column)
        self.value = value
        self.type = type
    
    def compile(self, env):
        genAux = Generator()
        generator = genAux.getInstance()
        if(self.type == Type.INT or self.type == Type.FLOAT):
            return Return(str(self.value), self.type, False)
        elif self.type == Type.BOOLEAN:
            if self.trueLbl == '':
                self.trueLbl = generator.newLabel()
            if self.falseLbl == '':
                self.falseLbl = generator.newLabel()
            
            if(self.value):
                generator.addGoto(self.trueLbl)
                generator.addComment("GOTO PARA EVITAR ERROR DE GO")
                generator.addGoto(self.falseLbl)
            else:
                generator.addGoto(self.falseLbl)
                generator.addComment("GOTO PARA EVITAR ERROR DE GO")
                generator.addGoto(self.trueLbl)
            
            ret = Return(self.value, self.type, False)
            ret.trueLbl = self.trueLbl
            ret.falseLbl = self.falseLbl

            return ret
        elif self.type == Type.STRING or self.type == Type.CHAR:
            retTemp = generator.addTemp()
            generator.addExp(retTemp, 'H', '', '')

            for char in str(self.value):
                generator.setHeap('H', ord(char))   # heap[H] = NUM;
                generator.nextHeap()                # H = H + 1;

            generator.setHeap('H', '-1')            # FIN DE CADENA
            generator.nextHeap()

            return Return(retTemp, self.type, True)
        elif self.type == Type.ARRAY:
            retTemp = generator.addTemp()
            t1 = generator.addTemp()
            generator.addExp(retTemp, 'H', '', '')
            generator.addExp(t1,retTemp,'1','+')
            generator.setHeap('H', len(self.value))
            print(len(self.value))
            size_vector = len(self.value) + 1
            generator.addExp('H','H',str(size_vector),'+')
            print(self.value)
            for valor in self.value:
                generator.setHeap(t1, valor.value) 
                generator.addExp(t1,t1,'1','+')             

            return Return(retTemp, self.type, True)
        else:
            print('Por hacer')