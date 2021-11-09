from Abstract.Instruccion import *

class DeclareStruct(Instruccion):

    def __init__(self, id, type, line, column):
        Instruccion.__init__(self, line, column)
        self.id = id
        self.type = type
    