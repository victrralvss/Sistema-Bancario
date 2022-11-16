from datetime import datetime

SUCESSINIT = '\033[32m'
SUCESSEND =' \033[0;0m'
ERRORINIT = '\033[0;31m'
ERROREND =' \033[m'

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
        return f"R$ {float(self._saldo):.2f}"
    
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
            print(f"{ERRORINIT}Saldo insuficiente!{ERROREND}")
            return False

        elif valor > 0:
            self._saldo -= valor
            print(f"{SUCESSINIT}SAQUE REALIZADO COM SUCESSO!{SUCESSEND}")
            return True

        else:
            print(f"{ERRORINIT}Erro ao tentar realizar o saque, por favor insira um valor válido!{ERROREND}")
            return False
 
    def depositar(self, valor):

        if valor > 0:
            self._saldo += valor
            print(f"{SUCESSINIT}DEPOSITO REALIZADO COM SUCESSO!{SUCESSEND}")
            return True
        else:
            print(f"{ERRORINIT}Erro na tentativa de deposito!{ERROREND}")
            return False

        

    def __str__(self):
        return f"CLASSE: {self.__class__.__name__} | {' | '.join([f'{k} : {v}' for k, v in self.__dict__.items()])}"



class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saques

    def sacar(self, valor):

        movimeto = [mov for mov in self.historico.transacoes if mov.get("operação") == "Saque"]

        if valor > self._limite:
            print(f"{ERRORINIT}Saque não realizado! O seu limite de saque é R$ {self._limite},00{ERROREND}")
            return False

        elif len(movimeto) >= 3:
            print(f"{ERRORINIT}Você atingiu o seu limite de 3 saques diários!{ERROREND}")
            return False

        else:
            print(movimeto)
            return super().sacar(valor)
    

    def __str__ (self):
        return f"TITULAR:\t{self._cliente.nome}\nC/C:\t\t{self._numero}\nAGENCIA:\t{self._agencia}\n"



class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "operação": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
                
            }
        )

    def __str__(self):
        return f"{self.__class__.__name__} | {' | '.join([f'{k} : {v}' for k, v in self.__dict__.items()])}"
        
