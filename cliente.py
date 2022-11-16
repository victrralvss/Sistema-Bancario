from transacao import *
from conta import *
from datetime import date



class Cliente:

    def __init__(self):
        self.endereco = None
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)
       

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, idade):
        self._cpf = cpf
        self._nome = nome
        self._idade = idade
        self.contas = []

    @classmethod
    def fromDataNascimento(cls, cpf, nome, ano_nascimento):
        return cls(cpf, nome, date.today().year - ano_nascimento)

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade
    
    def adicionar_conta(self, conta):
        return super().adicionar_conta(conta)
        

    def __str__(self):
        return f"CLASSE : {self.__class__.__name__} | {' | '.join([f'{k} : {v}' for k, v in self.__dict__.items()])}"


class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado):
        self.rua= rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"CLASSE : {self.__class__.__name__} | {' | '.join([f'{k} : {v}' for k, v in self.__dict__.items()])}"

p1 = PessoaFisica(12, 'sdasdasd', 22)
print(p1)