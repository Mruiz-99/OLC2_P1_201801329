from Abstract.Instruccion import *
from Abstract.Return import *
from Symbol.Generator import *

class For(Instruccion):

    def __init__(self, expresion, instr, line, column):
        Instruccion.__init__(self, line, column)
        self.expresion = expresion
        self.instr = instr
    
    def compile(self, environment):
        
        genAux = Generator()
        generator = genAux.getInstance()

        t1 = generator.addTemp()
        t2 = generator.addTemp()
        t3 = generator.addTemp()

        L0 = generator.newLabel()
        L1 = generator.newLabel()
        L2 = generator.newLabel()

        expresion = self.expresion.compile(environment)
        generator.getHeap(t1,expresion.value)
        generator.addExp(t2,'0','','')
        generator.addExp(t3,'P','0','+')
        generator.setStack(t3,t2)
        generator.putLabel(L0)
        generator.addIf(t2,t1,'==',L2)
        
        newEnv = Environment(environment)
        for instruccion in self.instr:
            instruccion.compile(newEnv)
        #self.instr.compile(newEnv)
        generator.putLabel(L1)
        generator.addExp(t2,t2,'1','+')
        generator.setStack(t3,t2)
        generator.addGoto(L0)
        generator.putLabel(L2)
