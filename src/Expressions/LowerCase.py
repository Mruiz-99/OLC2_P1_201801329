from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Generator import Generator
from enum import Enum
import uuid


class LowerCase(Expresion):
    
    def __init__(self, value, type, line, column):
        Expresion.__init__(self, line, column)
        self.value = value
        self.type = type
    
    def compile(self, env):
        genAux = Generator()
        generator = genAux.getInstance()
        if self.value != None:
            leftValue = self.value.compile(env)

        generator.ftoLower()
        t4 = generator.addTemp()
        t5 = generator.addTemp()

        generator.addExp(t4, 'P', env.size, '+')
        generator.addExp(t4, t4, '1', '+')
        generator.setStack(t4, leftValue.value)
                
        generator.newEnv(env.size)
        generator.callFun('toLower')

        generator.getStack(t5, 'P')
        generator.retEnv(env.size)
        return Return(t5, Type.STRING, True)
        '''

            t4 = P+0;
            t4 = t4+1;
            stack[int(t4)] = t0;
            P = P + 0;
            toLower();
            t5 = stack[int(P)];
            P = P - 0;
        '''

        