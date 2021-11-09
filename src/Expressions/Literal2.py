from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Generator import Generator
import uuid
class Literal2(Expresion):

    def __init__(self, value, rep, type, line, column):
        Expresion.__init__(self, line, column)
        self.value = value
        self.rep = rep
        self.type = type
    
    def compile(self, env):
        genAux = Generator()
        generator = genAux.getInstance()
        retTemp = generator.addTemp()
        generator.addExp(retTemp, 'H', '', '')

        for a in range(int(self.rep)):
            for char in str(self.value):
                generator.setHeap('H', ord(char))   # heap[H] = NUM;
                generator.nextHeap()                # H = H + 1;

        generator.setHeap('H', '-1')            # FIN DE CADENA
        generator.nextHeap()

        return Return(retTemp, self.type, True)