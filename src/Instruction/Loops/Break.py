from Abstract.Instruccion import *
from Abstract.Return import *
from Symbol.Generator import *

class Break(Instruccion):

    def __init__(self, line, column):
        Instruccion.__init__(self, line, column)
    
    def compile(self, environment):
        if environment.breakLbl == '':
            print("Break fuera de ciclo")
            return
        genAux = Generator()
        generator = genAux.getInstance()

        generator.addGoto(environment.breakLbl)