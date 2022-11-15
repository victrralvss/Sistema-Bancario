from transacao import Transacao
from datetime import datetime

class Conta:

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente =  cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
        
    @property
    def cliente(self):
        return self._cliente.nome

    @property
    def historico(self):
        return self._historico


    def sacar(self, valor):
        saldo = self._saldo

        if valor > saldo:
            print("Saldo insuficiente!")
            return False

        elif valor > 0:
            self._saldo -= valor
            return True

        else:
            print("Erro ao tentar realizar o saque, por favor insira um valor válido!")
            return False
 
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Por favor insira apenas valores a cima de R$ 5.00")
            return False
        
        return True
        

    def __str__(self):
        return f"CLASSE: {self.__class__.__name__} | {' | '.join([f'{k} : {v}' for k, v in self.__dict__.items()])}"

    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "operação": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )

class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite = limite_saques

    def sacar(self, valor):
        
        if valor > self._limite:
            print(f"Saque não realizado! O seu limite de saquie é R$ {self._limite},00")
            return False
        


    def __str__ (self):
        return f"TITULAR:\t{self._cliente.nome}\nC/C:\t\t{self._numero}\nAGENCIA:\t{self._agencia}\n"


class Historico:
    def __init__(self):
        self._transacoes = []
    
    def adicionar_transacao(self, transacao):
        pass