from cliente import *
from conta import *
from transacao import *
from operacoes import Operacao as op



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

def programa():
    
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
                print("COMANDO NÃO RECONHECIDO")

programa()  