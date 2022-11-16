#Aqui ficarão organizados todas as operação implementadas pelo Banco
from cliente import *
from conta import *
from transacao import *


SUCESSINIT = '\033[32m'
SUCESSEND =' \033[0;0m'
ERRORINIT = '\033[0;31m'
ERROREND =' \033[m'

clientes_cadastrados = []
contas_cadastradas = []

c1 = PessoaFisica(122, "1212", 22)

def validar_quantia(msg):
    validacao = False
    valor_verificado = ""

    while True:
        valor_entrada = input(msg).strip()

        if "." in valor_entrada or "," in valor_entrada:
            valor_verificado = valor_entrada.replace(".", "").replace(",", "")

        if (valor_verificado.isdigit() or valor_entrada.isdigit()):
            validacao = True
        else:
            print(f"{ERRORINIT}ERRO! Houve um problema ao tentar realizar a operação! Digite uma quantia válida.!{ERROREND}")

        if validacao:
            return float(valor_entrada.replace(",", "."))

def id_generator():
    ids = len(clientes_cadastrados)
    return ids + 1

def numero_generator():
    numero = len(contas_cadastradas)
    return numero + 1

def cpf_existe(cpf_user):
    cpf_list = []
    for cliente in clientes_cadastrados:
        for cpf in cliente:
            cpf_list.append(cpf)

    if cpf_user in cpf_list:
        return True
        
    return 

def validando_reposta(msg):
    while True:
        resposta = input(msg).strip().lower()
        if resposta.startswith('s') or resposta.startswith('n'):
            break
        else:
            print(f"{ERRORINIT}Por favor, digite uma opção válida!{ERROREND}")
            
    return True if resposta.startswith('s') else False

def get_client(cpf_cliente):
    for cliente in clientes_cadastrados:
        for cpf, registro_cliente in cliente.items():
                if cpf == cpf_cliente:
                    return registro_cliente

def registrar_endereco(cpf_cliente):

    cliente = get_client(cpf_cliente)

    while True: #validando numero
        numero_casa = input("Digite o número da sua casa: ").strip()
        if numero_casa:
            break
        else:
            print(f"{ERRORINIT}Por favor, insira um número válido{ERROREND}")

    while True: #validando rua
        rua = input("Digite a rua onde mora: ").strip()
        if rua:
            break
        else:
            print(f"{ERRORINIT}Por favor, insira uma rua válida{ERROREND}")

    while True: #validando bairro
        bairro = input("Digite o seu bairro: ").strip()
        if bairro:
            break
        else:
            print(f"{ERRORINIT}Por favor, insira um bairro válido{ERROREND}")

    while True: #validando cidade
        cidade = input("Digite o seu cidade: ").strip()
        if cidade and cidade.replace(' ', '').isalpha():
            break
        else:
            print(f"{ERRORINIT}Por favor, insira uma cidade válida{ERROREND}")

    while True: #validando estado
        estado = input("Digite o seu estado: ").strip()
        if estado and estado.replace(' ', '').isalpha():
            break
        else:
            print(f"{ERRORINIT}Por favor, insira um estado válido{ERROREND}")

    cliente.endereco = Endereco(rua, numero_casa, bairro, cidade, estado)

def usuario():
    cpf_cliente =  input("Digite seu CPF: ")

    if cpf_existe(cpf_cliente):  
        return get_client(cpf_cliente)
    else:
        print(f"{ERRORINIT}Sem registro de CPF{ERROREND}")
        return False

def get_conta(cliente):

    contas_cliente = [conta.numero for conta in cliente.contas]
    conta_final  = cliente.contas[0]

    if len(cliente.contas) > 1:

        print(f"\n{' CONTAS '.center(30, '=')}\n")
        for conta in cliente.contas:
            print(conta)
        print(f"\n{'='*30}\n")
        conta_escolhida = int(input("Escolha o número da conta que deseja realizar a transação\nCONTA > "))

        if conta_escolhida not in contas_cliente:
            print(f"{ERRORINIT}Conta inexistente!{ERROREND}")
            return
        else:
            conta_final =  cliente.contas[contas_cliente.index(conta_escolhida)]

    return conta_final




class Operacao:
    pass

    def deposito():
        cliente = usuario()
        if cliente:
            if len(cliente.contas) >= 1:
                conta = get_conta(cliente)
                valor_deposito = validar_quantia("Digite a quantia que deseja depositar > R$ ")
                transacao = Deposito(valor_deposito)
                cliente.realizar_transacao(conta, transacao)
                    
            else:
                print(f"{ERRORINIT}O CPF informado ainda não registrou nenhuma conta no nosso banco!{ERROREND}")
                return

    def sacar():
        cliente = usuario()

        if cliente:
            if len(cliente.contas) >= 1:
                conta = get_conta(cliente)
                valor_saque = validar_quantia("Digite a quantia que deseja sacar > R$ ")
                transacao = Saque(valor_saque)
                if cliente.realizar_transacao(conta, transacao):
                    print(f"{SUCESSINIT}SAQUE REALIZADO COM SUCESSO!{SUCESSEND}")
            else:
                print(f"{ERRORINIT}O CPF informado ainda não registrou nenhuma conta no nosso banco!{ERROREND}")
                return

    def consultar_extrato():
        cliente = usuario()
        if cliente:
            if len(cliente.contas) >= 1:
                conta = get_conta(cliente)
                extrato = conta.historico.transacoes

                print(f"{' EXTRATO '.center(30, '=')}")
                for movimento in extrato:
                    print(f"\n{movimento.get('data')}")
                    print(f"\tOPERAÇÃO: {movimento.get('operação')}")
                    print(f"\tVALOR: R$ {movimento.get('valor')}")
                print(f"\nSALDO:\tR$ {SUCESSINIT}{conta.saldo}{SUCESSEND}")
        else: 
            print(f"{ERRORINIT}O CPF informado ainda não registrou nenhuma conta no nosso banco!{ERROREND}")
            return

    def criar_conta():

        if validando_reposta(f"\n{' LOGIN '.center(30, '=')}\nJá é cliente do nosso banco?\n[S] - SIM\t[N] - NÃO\n\n> "):
            
                cliente = usuario()
                if cliente:
                    numero_conta = numero_generator()
                    conta = ContaCorrente.nova_conta(cliente, numero_conta)
                    cliente.adicionar_conta(conta)
                    contas_cadastradas.append(conta)
                    print(f"{SUCESSINIT}CONTA CADASTRADA COM SUCESSO!{SUCESSEND}")
                    
    def listar_contas():

        cliente = usuario()
        if len(cliente.contas) >= 1: 
            print(f"\n{' CONTAS '.center(30, '=')}\n")
            for conta in cliente.contas:
                print(conta)
            print('='*30)
        else:
            print(f"{ERRORINIT}O CPF informado ainda não registrou nenhuma conta no nosso banco!{ERROREND}")
            return
    
    def novo_usuario():

        """Responsavel por validar todos os dados inerentes a um cliente e retornar uma insatancia de Cliente
        com os dados previamente validados
        """

        print(f"{' CADASTRO '.center(30, '=')}")
 
        cpf = ""
        nome = ""
        idade = ""

        while True: #VALIDAÇÃO CPF
            
            cpf_entrada = input("Digite seu CPF: ").strip()
            if not cpf_entrada.replace('.', "").replace('-', '').isnumeric():
                print(f"{ERRORINIT}Por favor insira CPF válido{ERROREND}")

            elif len(cpf_entrada.replace('.', "").replace('-', '')) != 3:
                print(f"{ERRORINIT}O CPF deve ser composto por três dígitos!{ERROREND}")

            elif cpf_existe(cpf_entrada):
                print("VERIFICANDO CPF ...")
                print(f"{ERRORINIT}CPF já cadastrado{ERROREND}")

            else:
                cpf = cpf_entrada
                break
    
        while True: #VALIDAÇÃO NOME

            nome_entrada = input("Digite seu nome: ").strip()     
            if nome_entrada.replace(' ', '').isalpha():
                nome = nome_entrada.title()
                break
            else:
                print(f"{ERRORINIT}Por favor, insira um nome válido{ERROREND}")

        while True: #VALIDAÇÃO IDADE

            idade_entrada = input("Digite sua idade (idade mínima 18 anos ): ").strip()
            if idade_entrada.isdigit() and 18 <= int(idade_entrada) <= 150:
                idade = idade_entrada
                break
            else:
                print(f"{ERRORINIT}Por favor, insira uma idade válida{ERROREND}")

        cliente = PessoaFisica(cpf, nome, idade)
        clientes_cadastrados.append({cliente.cpf : cliente})

        if validando_reposta("\nGostaria de cadastrar seu endereço?\n[S] - SIM\t[N] - NÃO\n\n> "):
            registrar_endereco(cpf)

        print(f"{SUCESSINIT}USUÁRIO CADASTRADO COM SUCESSO!{SUCESSEND}")

         

        