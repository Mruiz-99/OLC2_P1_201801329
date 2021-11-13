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
            t5 = generator.addTemp()

            L0 = generator.newLabel()
            L1 = generator.newLabel()
            L2 = generator.newLabel()

            generator.addIf(str(self.pos-1),'0','<',L0)
            generator.getHeap(t5,temp)
            generator.addIf(str(self.pos),t5,'>',L0)
            generator.addGoto(L1)
            generator.putLabel(L0)
            generator.addPrint("c",66)
            generator.addPrint("c",111)
            generator.addPrint("c",117)
            generator.addPrint("c",110)
            generator.addPrint("c",100)
            generator.addPrint("c",115)
            generator.addPrint("c",32)
            generator.addPrint("c",69)
            generator.addPrint("c",114)
            generator.addPrint("c",114)
            generator.addPrint("c",111)
            generator.addPrint("c",114)
            generator.addPrint("c",32)
            generator.addPrint("c",10)
            generator.addGoto(L2)
            generator.putLabel(L1)

            generator.addExp(t3,temp,str(self.pos-1),'+')
            generator.addExp(t3,t3,'1','+')
            generator.getHeap(t4,t3)
            generator.addGoto(L2)
            generator.putLabel(L2)

            return Return(t4, var.type, True)
        return 
        '''
        t3=t2+-1;
        t3=t3+1;
        t4=heap[int(t3)];
        fmt.Printf("%f", float64(t4));
        fmt.Printf("%c", int(10));
        goto L2;
        L2:
        '''