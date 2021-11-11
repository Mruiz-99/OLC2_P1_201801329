from Abstract.Instruccion import Instruccion
from .Environment import Environment

class Generator:
    generator = None
    def __init__(self):
        # Contadores
        self.countTemp = 0
        self.countLabel = 0
        # Code
        self.code = ''
        self.funcs = ''
        self.natives = ''
        self.inFunc = False
        self.inNatives = False
        # Lista de Temporales
        self.temps = []
        self.imports =[f'import(\n\t\"fmt\"\n);\n']
        self.imports2 = ["fmt","math"]
        # Lista de Nativas
        self.printString = False
        self.TruncInt = False
        self.concatString = False
        self.repeticionString = False
        self.upperString = False
        self.lowerString = False
        self.potencia = False
        
    def cleanAll(self):
        # Contadores
        self.countTemp = 0
        self.countLabel = 0
        # Code
        self.code = ''
        self.funcs = ''
        self.natives = ''
        self.inFunc = False
        self.inNatives = False
        # Lista de Temporales
        self.temps = []
        # Lista de Nativas
        self.printString = False
        self.potencia = False
        Generator.generator = Generator()
    #############
    # IMPORTS
    #############
    def setImport(self,lib):
        if lib in self.imports2:
            self.imports2.remove(lib)
        else:
            return
        ret = f'import(\n\t\"{lib}\"\n);\n'
        self.imports.append(ret)
    #############
    # CODE
    #############
    def getHeader(self):
        ret = '/*----HEADER----*/\npackage main;\n\n'
        if len(self.imports)>0:
            for temp in range(len(self.imports)):
                ret += self.imports[temp]
        if len(self.temps) > 0:
            ret += 'var '
            for temp in range(len(self.temps)):
                ret += self.temps[temp]
                if temp != (len(self.temps) - 1):
                    ret += ", "
            ret += " float64;\n"
        ret += "var P, H float64;\nvar stack [30101999]float64;\nvar heap [30101999]float64;\n\n"
        return ret

    def getCode(self):
        return f'{self.getHeader()}{self.natives}\n{self.funcs}\nfunc main(){{\n{self.code}\n}}'

    def codeIn(self, code, tab="\t"):
        if(self.inNatives):
            if(self.natives == ''):
                self.natives = self.natives + '/*-----NATIVES-----*/\n'
            self.natives = self.natives + tab + code
        elif(self.inFunc):
            if(self.funcs == ''):
                self.funcs = self.funcs + '/*-----FUNCS-----*/\n'
            self.funcs = self.funcs + tab +  code
        else:
            self.code = self.code + '\t' +  code

    def addComment(self, comment):
        self.codeIn(f'/* {comment} */\n')
    
    def getInstance(self):
        if Generator.generator == None:
            Generator.generator = Generator()
        return Generator.generator

    def addSpace(self):
        self.codeIn("\n")

    ########################
    # Manejo de Temporales
    ########################
    def addTemp(self):
        temp = f't{self.countTemp}'
        self.countTemp += 1
        self.temps.append(temp)
        return temp

    #####################
    # Manejo de Labels
    #####################
    def newLabel(self):
        label = f'L{self.countLabel}'
        self.countLabel += 1
        return label

    def putLabel(self, label):
        self.codeIn(f'{label}:\n')

    ###################
    # GOTO
    ###################
    def addGoto(self, label):
        self.codeIn(f'goto {label};\n')
    
    ###################
    # IF
    ###################
    def addIf(self, left, right, op, label):
        self.codeIn(f'if {left} {op} {right} {{goto {label};}}\n')

    ###################
    # EXPRESIONES
    ###################
    def addExp(self, result, left, right, op):
        self.codeIn(f'{result}={left}{op}{right};\n')

    def addModulo(self, result, left, right):
        self.codeIn(f'{result}=  math.Mod({left},{right});\n')

    def addAsig(self, result, left):
        self.codeIn(f'{result}= {left};\n')
    ###################
    # FUNCS
    ###################
    def addBeginFunc(self, id):
        if(not self.inNatives):
            self.inFunc = True
        self.codeIn(f'func {id}(){{\n', '')
    
    def addEndFunc(self):
        self.codeIn('return;\n}\n');
        if(not self.inNatives):
            self.inFunc = False

    ###############
    # STACK
    ###############
    def setStack(self, pos, value):
        self.codeIn(f'stack[int({pos})]={value};\n')
    
    def getStack(self, place, pos):
        self.codeIn(f'{place}=stack[int({pos})];\n')

    #############
    # ENVS
    #############
    def newEnv(self, size):
        self.codeIn(f'P=P+{size};\n')

    def callFun(self, id):
        self.codeIn(f'{id}();\n')

    def retEnv(self, size):
        self.codeIn(f'P=P-{size};\n')

    ###############
    # HEAP
    ###############
    def setHeap(self, pos, value):
        self.codeIn(f'heap[int({pos})]={value};\n')

    def getHeap(self, place, pos):
        self.codeIn(f'{place}=heap[int({pos})];\n')

    def nextHeap(self):
        self.codeIn('H=H+1;\n')

    # INSTRUCCIONES
    def addPrint(self, type, value):
        if(type=='f'):
            self.codeIn(f'fmt.Printf("%{type}", float64({value}));\n')
        else:    
            self.codeIn(f'fmt.Printf("%{type}", int({value}));\n')
    def printTrue(self):
        self.addPrint("c", 116)
        self.addPrint("c", 114)
        self.addPrint("c", 117)
        self.addPrint("c", 101)

    def printFalse(self):
        self.addPrint("c", 102)
        self.addPrint("c", 97)
        self.addPrint("c", 108)
        self.addPrint("c", 115)
        self.addPrint("c", 101)
    
    ##############
    # NATIVES
    ##############
    def fPrintString(self):
        if(self.printString):
            return
        self.printString = True
        self.inNatives = True

        self.addBeginFunc('printString')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()
        # Temporal puntero a Stack
        tempP = self.addTemp()
        # Temporal puntero a Heap
        tempH = self.addTemp()
        self.addExp(tempP, 'P', '1', '+')
        self.getStack(tempH, tempP)
        # Temporal para comparar
        tempC = self.addTemp()
        self.putLabel(compareLbl)
        self.getHeap(tempC, tempH)
        self.addIf(tempC, '-1', '==', returnLbl)
        self.addPrint('c', tempC)
        self.addExp(tempH, tempH, '1', '+')
        self.addGoto(compareLbl)
        self.putLabel(returnLbl)
        self.addEndFunc()
        self.inNatives = False
    
    def fPotencia(self):

        if(self.potencia):
            return
        self.potencia = True
        self.inNatives = True

        self.addBeginFunc('potencia')
        
        t0 = self.addTemp()
        self.addExp(t0, 'P', '1', '+')

        t1 = self.addTemp()
        self.getStack(t1, t0)

        self.addExp(t0, t0, '1', '+')

        t2 = self.addTemp()
        self.getStack(t2, t0)
        self.addExp(t0, t1, '', '')

        L0 = self.newLabel()
        L1 = self.newLabel()

        self.putLabel(L0)
        self.addIf(t2, '1', '<=', L1)
        self.addExp(t1, t1, t0, '*')
        self.addExp(t2, t2, '1', '-')
        self.addGoto(L0)
        self.putLabel(L1)
        self.setStack('P', t1)
        
        self.addEndFunc()
        self.inNatives = False

    def fconcatString(self):
        if(self.concatString):
            return
        self.concatString = True
        self.inNatives = True

        self.addBeginFunc('concatenacion')

        # Temporal puntero
        t3 = self.addTemp()
        t4 = self.addTemp()
        t5 = self.addTemp()
        t6 = self.addTemp()
        t7 = self.addTemp()

        L0 = self.newLabel()
        L1 = self.newLabel()
        L2 = self.newLabel()
        L3 = self.newLabel()

        self.addExp(t3, 'H','','')
        self.addExp(t4, 'P','1','+')
        self.getStack(t6,t4)
        self.addExp(t5,'P','2','+')
        self.putLabel(L1)
        self.getHeap(t7,t6)
        self.addIf(t7,'-1','==',L2)
        self.setHeap('H',t7)
        self.addExp('H','H','1','+')
        self.addExp(t6,t6,'1','+')
        self.addGoto(L1)
        self.putLabel(L2)
        self.getStack(t6,t5)
        self.putLabel(L3)
        self.getHeap(t7,t6)
        self.addIf(t7,'-1','==',L0)
        self.setHeap('H',t7)
        self.addExp('H','H','1','+')
        self.addExp(t6,t6 , '1','+')
        self.addGoto(L3)
        self.putLabel(L0)
        self.setHeap('H','-1')
        self.addExp('H','H','1','+')
        self.setStack('P',t3)
        self.addEndFunc()
        self.inNatives = False

    def ftoUpper(self):
        if(self.upperString):
            return
        self.upperString = True
        self.inNatives = True

        self.addBeginFunc('toUpper')

        # Temporal puntero
        t1 = self.addTemp()
        t2 = self.addTemp()
        t3 = self.addTemp()

        L0 = self.newLabel()
        L1 = self.newLabel()
        L2 = self.newLabel()

        self.addExp(t1,'H','','')
        self.addExp(t2,'P','1','+')
        self.getStack(t2,t2)
        self.putLabel(L0)
        self.getHeap(t3,t2)
        self.addIf(t3,'-1','==',L2)
        self.addIf(t3,'97','<',L1)
        self.addIf(t3,'122','>',L1)
        self.addExp(t3,t3,'32','-')
        self.putLabel(L1)
        self.setHeap('H',t3)
        self.addExp('H','H','1','+')
        self.addExp(t2,t2,'1','+')
        self.addGoto(L0)
        self.putLabel(L2)
        self.setHeap('H','-1')
        self.addExp('H','H','1','+')
        self.setStack('P',t1)
        self.addEndFunc()
        self.inNatives = False


    def fTrunc(self):
        if(self.TruncInt):
            return
        self.TruncInt = True
        self.inNatives = True

        self.addBeginFunc('Trunc')

        # Temporal puntero
        t2 = self.addTemp()
        t3 = self.addTemp()
        t4 = self.addTemp()
        t5 = self.addTemp()

        L0 = self.newLabel()
        L1 = self.newLabel()
        L2 = self.newLabel()

        self.addExp(t2,'P','0','+')
        self.getStack(t3,t2)
        self.setImport("math")
        self.addModulo(t4,t3,'1')
        self.addExp(t5,t3,t4,'-')
        self.setStack('P',t5)
        self.addGoto(L0)
        self.putLabel(L0)
        self.addEndFunc()
        self.inNatives = False



    def ftoLower(self):
        if(self.lowerString):
            return
        self.lowerString = True
        self.inNatives = True

        self.addBeginFunc('toLower')

        # Temporal puntero
        t1 = self.addTemp()
        t2 = self.addTemp()
        t3 = self.addTemp()

        L0 = self.newLabel()
        L1 = self.newLabel()
        L2 = self.newLabel()

        self.addExp(t1,'H','','')
        self.addExp(t2,'P','1','+')
        self.getStack(t2,t2)
        self.putLabel(L0)
        self.getHeap(t3,t2)
        self.addIf(t3,'-1','==',L2)
        self.addIf(t3,'65','<',L1)
        self.addIf(t3,'90','>',L1)
        self.addExp(t3,t3,'32','+')
        self.putLabel(L1)
        self.setHeap('H',t3)
        self.addExp('H','H','1','+')
        self.addExp(t2,t2,'1','+')
        self.addGoto(L0)
        self.putLabel(L2)
        self.setHeap('H','-1')
        self.addExp('H','H','1','+')
        self.setStack('P',t1)
        self.addEndFunc()
        self.inNatives = False


        
