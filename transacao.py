#INTERFACE
from abc import ABC, abstractmethod, abstractproperty
class Transacao(ABC):
    
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass
    

class Deposito(Transacao):

    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

class Saque(Transacao):

    def __init__(self, valor):
        self.valor = valor


    @property
    def valor(self):
        return self._valor

    def registrar():
        pass

