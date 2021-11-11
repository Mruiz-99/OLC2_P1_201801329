from Abstract.Instruccion import *
from Abstract.Return import *
from Symbol.Generator import Generator
import uuid

class Print(Instruccion):

    def __init__(self, value, line, column, newLine = False):
        Instruccion.__init__(self, line, column)
        self.value = value
        self.newLine = newLine
    
    def compile(self, env):
        val = self.value.compile(env)
        
        genAux = Generator()
        generator = genAux.getInstance()

        if(val.type == Type.INT):
            generator.addPrint("d", val.value)
        elif val.type == Type.FLOAT or val.type == Type.ARRAY:
            generator.addPrint("f", val.value)
        elif val.type == Type.BOOLEAN:
            tempLbl = generator.newLabel()
            
            generator.putLabel(val.trueLbl)
            generator.printTrue()
            
            generator.addGoto(tempLbl)
            
            generator.putLabel(val.falseLbl)
            generator.printFalse()

            generator.putLabel(tempLbl)
        elif val.type == Type.STRING or val.type == Type.CHAR:
            generator.fPrintString()

            paramTemp = generator.addTemp()
            
            generator.addExp(paramTemp, 'P', env.size, '+')
            generator.addExp(paramTemp, paramTemp, '1', '+')
            generator.setStack(paramTemp, val.value)
            
            generator.newEnv(env.size)
            generator.callFun('printString')

            temp = generator.addTemp()
            generator.getStack(temp, 'P')
            generator.retEnv(env.size)
        if self.newLine:
            generator.addPrint("c", 10)