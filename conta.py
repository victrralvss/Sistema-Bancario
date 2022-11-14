from transacao import Transacao

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



    def sacar(self, valor):
        saldo = self._saldo

        if valor > saldo:
            print("Saldo insuficiente!")

        elif valor > 0:
            self._saldo -= valor
            return True

        else:
            pass
 
    def depositar(self, valor):
        pass

    def __str__(self):
        return f"CLASSE: {self.__class__.__name__} | {' | '.join([f'{k} : {v}' for k, v in self.__dict__.items()])}"

class Historico:
    
    def adicionar_transacao(self, transacao):
        pass

class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite =  limite
        self._limite = limite_saques


    def __str__ (self):
        return f"CONTA:\t\tCC\nNUMERO:\t\t{self._numero}\nAGENCIA:\t{self._agencia}\n"


