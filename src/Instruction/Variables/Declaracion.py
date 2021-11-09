from Symbol.Generator import *
from Abstract.Instruccion import *
from Abstract.Return import *

class Declaracion(Instruccion):

    def __init__(self, id, value, tipo, line, column):
        Instruccion.__init__(self, line, column)
        self.id = id
        print(id)
        self.value = value
        self.tipo = tipo
    
    def compile(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.addComment("Compilacion de valor de variable")
        # Compilacion de valor que estamos asignando
        val = self.value.compile(environment)

        generator.addComment("Fin de valor de variable")
        
        if ( self.tipo != None) :
            if(self.tipo != val.type):
               return  Exception ("Semantico", "No se puede utilizar la expresion booleana en: ", self.line, self.column)


        # Guardado y obtencion de variable. Esta tiene la posicion, lo que nos sirve para asignarlo en el heap
        newVar = environment.getVar(self.id)
        if newVar == None:
            newVar = environment.saveVar(self.id, val.type, (val.type == Type.STRING or val.type == Type.STRUCT), self.value.structType)
        newVar.type = val.type

        # Obtencion de posicion de la variable
        tempPos = newVar.pos
        if(not newVar.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', newVar.pos, "+")
        
        if(val.type == Type.BOOLEAN):
            tempLbl = generator.newLabel()
            
            generator.putLabel(val.trueLbl)
            generator.setStack(tempPos, "1")
            
            generator.addGoto(tempLbl)

            generator.putLabel(val.falseLbl)
            generator.setStack(tempPos, "0")

            generator.putLabel(tempLbl)
        else:
            generator.setStack(tempPos, val.value)
        generator.addSpace()