from Abstract.Instruccion import *

class StructAttr(Instruccion):

    def __init__(self, id, type, line, column):
        Instruccion.__init__(self, line, column)
        self.id = id
        self.type = type
    
    def compile(self, environment):
        return self