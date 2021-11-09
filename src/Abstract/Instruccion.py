from abc import ABC, abstractmethod
from Symbol.Environment import *

class Instruccion(ABC):
    
    def __init__(self, line, column):
        self.line = line
        self.column = column
    
    @abstractmethod
    def compile(self, environment):
        pass
    