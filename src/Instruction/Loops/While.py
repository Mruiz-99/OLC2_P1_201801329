from Abstract.Instruccion import *
from Abstract.Return import *
from Symbol.Generator import *

class While(Instruccion):

    def __init__(self, condition, instr, line, column):
        Instruccion.__init__(self, line, column)
        self.cond = condition
        self.instr = instr
    
    def compile(self, environment):
        
        genAux = Generator()
        generator = genAux.getInstance()
    
        continueLbl = generator.newLabel()
        generator.putLabel(continueLbl)

        condition = self.cond.compile(environment)
        newEnv = Environment(environment)
        newEnv.breakLbl = condition.falseLbl
        newEnv.continueLbl = continueLbl

        generator.putLabel(condition.trueLbl)
        for instruccion in self.instr:
            instruccion.compile(newEnv)
        #self.instr.compile(newEnv)
        generator.addGoto(continueLbl)

        generator.putLabel(condition.falseLbl)