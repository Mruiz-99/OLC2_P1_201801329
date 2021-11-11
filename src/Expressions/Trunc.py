from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Generator import Generator
from enum import Enum
import uuid


class Trunc(Expresion):
    
    def __init__(self, value, line, column):
        Expresion.__init__(self, line, column)
        self.value = value
    
    def compile(self, env):
        genAux = Generator()
        generator = genAux.getInstance()
        if self.value != None:
            leftValue = self.value.compile(env)
        generator.fTrunc()
        t1 = generator.addTemp()
        t2 = generator.addTemp()
        t3 = generator.addTemp()
        
        generator.addExp(t1, 'P', env.size, '+')
        generator.setStack(t1, leftValue.value)

        generator.newEnv(env.size)
        generator.callFun('Trunc')

        generator.getStack(t1, 'P')
        generator.retEnv(env.size)
        return Return(t1, Type.INT, True)

        