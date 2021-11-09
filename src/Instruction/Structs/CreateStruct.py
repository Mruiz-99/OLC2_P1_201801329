from Abstract.Instruccion import *

class CreateStruct(Instruccion):

    def __init__(self, id, attr, line, column):
        Instruccion.__init__(self, line, column)
        self.id = id
        self.attr = attr
    
    def compile(self, environment):
        environment.saveStruct(self.id, self.attr)