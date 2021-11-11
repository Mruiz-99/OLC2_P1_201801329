from Abstract.Expresion import Expresion
from Symbol.Generator import *
from Abstract.Expresion import *
from Abstract.Return import *

class AccessVector(Expresion):

    def __init__(self, id, pos, line, column):
        Expresion.__init__(self, line, column)
        self.id = id
        self.pos = pos

    def compile(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.addComment("Compilacion de Acceso")
        
        var = environment.getVar(self.id)
        if(var == None):
            print("Error, no existe la variable")
            return

        # Temporal para guardar variable
        temp = generator.addTemp()

        # Obtencion de posicion de la variable
        tempPos = var.pos
        if(not var.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', var.pos, "+")
        generator.getStack(temp, tempPos)

        if var.type == Type.ARRAY:
            generator.addComment("Fin compilacion acceso")
            generator.addSpace()

            t3 = generator.addTemp()
            t4 = generator.addTemp()

            generator.addExp(t3,temp,str(self.pos),'+')
            generator.addExp(t3,t3,'1','+')
            generator.getHeap(t4,t3)
            return Return(t4, var.type, True)
        return 