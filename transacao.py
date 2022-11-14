#INTERFACE
from abc import ABC, abstractmethod
class Transacao(ABC):
    
    
    def registrar(conta):
        conta
    

class Deposito(Transacao):

    def __init__(self, valor):
        self.valor = valor

class Saque(Transacao):

    def __init__(self, valor):
        self.valor = valor