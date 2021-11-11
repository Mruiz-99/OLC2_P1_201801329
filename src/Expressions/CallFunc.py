from Abstract.Expresion import *
from Abstract.Return import *
from Instruction.Functions.ReturnST import ReturnST
from Symbol.Environment import *
from Symbol.Generator import *

class CallFunc(Expresion):

    def __init__(self, id, params, line, column):
        Expresion.__init__(self, line, column)
        self.id = id
        self.params = params
    
    def GuardarTemp(self, generador, ent, paramsTemp):
        generador.addComment("Guardado de temporales")
        tmp = generador.addTemp()

        for param in paramsTemp:
            generador.addExp(tmp,'P',ent.size,'+')
            generador.setStack(tmp,param)
            ent.size = ent.size + 1
        generador.addComment("Finalizado de guardado de temporales") 

    def RecuperacionTemp(self, generador, ent, paramsTemp):
        generador.addComment("Recuperacion de temporales")
        tmp = generador.addTemp()

        for param in paramsTemp:
            ent.size = ent.size - 1
            generador.addExp(tmp,'P',ent.size,'+')
            generador.getStack(param,tmp)
            
        generador.addComment("Finalizado de recuperacion de temporales") 


    def compile(self, environment):
        try:
            func = environment.getFunc(self.id)
            paramValues = []

            genAux = Generator()
            generator = genAux.getInstance()
            size = environment.size
            paramsTemp = []
            for param in self.params:
                if isinstance(param,CallFunc):
                    self.GuardarTemp(generator,environment,paramsTemp)
                    aux = param.compile(environment)
                    paramValues.append(aux)
                    self.RecuperacionTemp(generator,environment,paramsTemp)
                else:
                    aux = param.compile(environment)
                    if isinstance(aux,Exception):
                        return aux
                    paramValues.append(aux)
                    paramsTemp.append(aux.value)
                        
            temp = generator.addTemp()

            generator.addExp(temp, 'P', size+1, '+')
            aux = 0
            for param in paramValues:
                aux = aux +1
                generator.setStack(temp, param.value)
                if aux != len(paramValues):
                    generator.addExp(temp, temp, '1', '+')
                
            generator.newEnv(size)
            generator.callFun(self.id)
            generator.getStack(temp, 'P')
            generator.retEnv(size)
                
            # TODO: Verificar tipo de la funcion. Boolean es distinto
            return Return(temp, Type.INT, True)
        except:
            print("Error en llamada a funcion")
        '''else:
                # STRUCT
                struct = environment.getStruct(self.id)
                if struct != None:
                    self.structType = self.id

                    genAux = Generator()
                    generator = genAux.getInstance()

                    returnTemp = generator.addTemp()
                    generator.addExp(returnTemp, 'H', '', '')

                    aux = generator.addTemp()
                    generator.addExp(aux, returnTemp, '', '')

                    generator.addExp('H', 'H', len(struct), '+')

                    for att in self.params:
                        value = att.compile(environment)

                        if value.type != Type.BOOLEAN:
                            generator.setHeap(aux, value.value)
                        else:
                            retLbl = generator.newLabel()
                            
                            generator.putLabel(value.trueLbl)
                            generator.setHeap(aux, '1')
                            generator.addGoto(retLbl)

                            generator.putLabel(value.falseLbl)
                            generator.setHeap(aux, '0')

                            generator.putLabel(retLbl)
                        generator.addExp(aux, aux, '1', '+')
                    
                    return Return(returnTemp, Type.STRUCT, True)'''
        