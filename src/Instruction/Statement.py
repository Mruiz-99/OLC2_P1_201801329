from Abstract.Instruccion import *
from Abstract.Return import *
from Symbol.Environment import *

class Statement(Instruccion):

    def __init__(self, instructions, line, column):
        Instruccion.__init__(self, line, column)
        self.instructions = instructions
    
    def compile(self, environment):
        for ins in self.instructions:
            ret = ins.compile(environment)
            if ret != None:
                return ret