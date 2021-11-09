from Abstract.Instruccion import *
from Abstract.Return import Type
from Symbol.Generator import *

class If(Instruccion):

    def __init__(self, condition, instructions, line, column, elseSt = None):
        Instruccion.__init__(self, line, column)
        self.condition = condition
        self.instructions = instructions
        self.elseSt = elseSt
        
    
    def compile(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.addComment("Compilacion de If")
        condition = self.condition.compile(environment)

        if condition.type != Type.BOOLEAN:
            print('Error, condicion no booleana')
            return
        
        generator.putLabel(condition.trueLbl)
        
        for instrucciones in self.instructions:
            instrucciones.compile(environment)
        
        if self.elseSt != None:
            exitIf = generator.newLabel()
            generator.addGoto(exitIf)
        
        generator.putLabel(condition.falseLbl)
        if self.elseSt != None:
            if ( isinstance(self.elseSt, If)):
                self.elseSt.compile(environment)
            else:
                for instrucciones in self.elseSt:  
                    instrucciones.compile(environment)
            generator.putLabel(exitIf)