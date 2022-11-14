from cliente import *
from conta import *
from transacao import *
from operacoes import Operacao as op

SUCESSINIT = '\033[32m'
SUCESSEND = '\033[0;0m'
ERRORINIT = '\033[0;31m'
ERROREND = '\033[m'

# Programa principal
msg_menu = f"""
{" BANCO DIGITAL ".center(30, "=")}
[1]\tDepositar
[2]\tSacar
[3]\tConsultar extrato
[4]\tNova conta
[5]\tListar contas
[6]\tNovo usuário
[X]\tEncerrar programa
"""

def cadastro():
    msg_cadastro = f"""
    
{" BANCO DIGITAL ".center(30, "=")}   

Já é cliente do nosso banco?
[S] - SIM\t[N] - NÃO]
"""


def listar_clientes(cpf):
    pass


def programa():
    contas_criadas = []
    clientes_registrados = []

    while True:

        print(msg_menu)
        escolha =  input("> ").strip().lower()
    
        match escolha:
            case "1":
                op.deposito()
            case "2":
                op.sacar()
            case "3":
                op.consultar_extrato()
            case "4":
                op.criar_conta()
            case "5":
                op.listar_contas()
            case "6":
                op.novo_usuario()

            case "x":
                print("Encerrando o programa...")
                break
            case other:
                print(f"{ERRORINIT}COMANDO NÃO RECONHECIDO{ERROREND}")

programa()  