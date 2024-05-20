import sys
from endereco import Endereco
from time import sleep
from cliente import Cliente
from conta import Conta
from os import system
from menus import menu_emprestimo


LIMITE_SAQUES = 3
numero_saques = 0
tem_emprestimo = False
contas = []
clientes = []

def criar_conta():
    print('Informe os dados do Cliente: ')
    nome = input('Nome: ')
    cpf = input('CPF: ')
    data_nascimento = input('Data de Nascimento [dd/mm/aaaa]: ')
    email = input('Email: ')
    rua = input('Rua: ')
    numero_casa = input('Número da Casa: ')
    bairro = input('Bairro: ')
    cidade = input('cidade: ')
    estado = input('Estado: ')

    endereco = Endereco(rua, numero_casa, bairro, cidade, estado)
    cliente = Cliente(nome, cpf, data_nascimento, email, endereco)
    conta = Conta(cliente)

    contas.append(conta)
    clientes.append(cliente)

    print('\t\t Conta cadastrada com sucesso!!')
    print('\t\t Dados da Conta: ')
    print('\t\t ' + '*' * 40)
    print(conta)
    sleep(2)


def efetuar_saque():
    global numero_saques
    if possui_contas():
        tipo_operacao = 'sacar'
        numero_conta = int(input('Digite o número da sua conta: '))
        conta = buscar_conta_por_numero(numero_conta)

        if valida_conta(conta, numero_conta, efetuar_saque):
            valor = ler_valor(tipo_operacao)
            eh_menor, valor = saldo_insuficiente(valor, conta.saldo_total, tipo_operacao)
            if eh_menor:
                if numero_saques <=  LIMITE_SAQUES:
                    conta.sacar(valor, 'Saque de R$')
                    numero_saques += 1
                else:
                    print('Você ultrapassou o seu limite de saques diários!!')


def efetuar_deposito():
    if possui_contas():
        tipo_operacao = 'depositar'
        numero_conta = int(input('Digite o número da sua conta: '))
        conta = buscar_conta_por_numero(numero_conta)

        if valida_conta(conta, numero_conta, efetuar_deposito):
            valor = ler_valor(tipo_operacao)
            valida_valor, valor = valor_maior_q_zero(valor, tipo_operacao)
            if valida_valor:
                conta.depositar(valor, 'Depósito de R$')


def efetuar_transferencia():
    tipo_operacao = 'transferir'
    if possui_contas():
        conta_orig, numero_conta_orig = ler_conta('Digite o número da sua conta: ')

        if valida_conta(conta_orig, numero_conta_orig, efetuar_transferencia):
            conta_dest, numero_conta_dest = ler_conta('Digite a conta para a qual deseja transferir: ')
            if valida_conta(conta_dest, numero_conta_dest, ler_conta):
                valor = ler_valor(tipo_operacao)
                eh_menor, valor = saldo_insuficiente(valor, conta_orig.saldo_total, tipo_operacao)
                if eh_menor:
                    conta_orig.transferir(conta_dest, valor)


def realizar_emprestimo(tipo_acesso=0):
    taxa=0.4
    global tem_emprestimo
    if possui_contas():
        numero_conta = int(input('Digite o número da sua conta: '))
        conta = buscar_conta_por_numero(numero_conta)

        if tem_emprestimo:
            print('EMPRÉSTIMO NEGADO!!!\nInfelizmente, só permitimos um empréstimo por conta e você já possui um')

        elif tipo_acesso == 1:
            resp = input('Deseja mudar a taxa de empréstimo do cliente? S ou N').upper()
            if resp in 'SIM':
                taxa = float(input('Informe a taxa negociada: EX: 10% 20%: '))
                taxa /= 100
        elif valida_conta(conta, numero_conta, realizar_emprestimo):
            salario = float(input('Digite o valor do seu salário: R$ '))
            parcela = float(input('Informa o valor da parcela que seja pagar por mês: R$ '))
            emprestimo(salario, parcela, conta, realizar_emprestimo,taxa)

def emprestimo(salario, valor_parcela, conta, funcao, taxa=0.4):
    global tem_emprestimo
    limite_parcela = salario * 0.2

    if valor_parcela > limite_parcela:
        print('EMPRÉSTIMO NEGADO!!!\nO valor da parcela não pode compromenter mais do que 20% do seu salário.')
        print(f'Valor Máximo da parcela: R$ {limite_parcela:.2f}')
        funcao()
    else:
        total_a_pagar = valor_parcela * 48
        limite_emprestimo = total_a_pagar - (total_a_pagar * taxa)
        resp = menu_emprestimo(limite_emprestimo, total_a_pagar)
        if resp == 1:
            conta.depositar(limite_emprestimo, 'Empréstimo do Banco DIO Bank')
            tem_emprestimo = True
        elif resp == 2:
            valor = float(input('Digite o valor do Empréstimo desejado: '))
            if valor <= limite_emprestimo:
                conta.depositar(valor, 'Empréstimo do Banco DIO Bank')
                tem_emprestimo = True
            else:
                print(f'Valor não Permitido!! R${valor:.2f} ultrapassa o seu Limite de Empréstimos.')
        else:
            exit()


def aumentar_limite_conta():
    if possui_contas():
        numero_conta = int(input('Digite o número da sua conta: '))
        conta = buscar_conta_por_numero(numero_conta)
        novo_limite = float(input('Informe o novo limite da conta: R$ '))
        conta.limite(novo_limite)


def listar_contas():
    if possui_contas():
        print('\t\t Lista de Contas')
        print('\t\t ' + '*' * 40)
        for conta in contas:
            print(conta)
            print('\t\t ' + '*' * 40)


def listar_clientes():
    if possui_clientes():
        print('\t\t Lista de Clientes')
        print('\t\t ' + '*' * 40)
        for cliente in clientes:
            print(cliente)
            print('\t\t ' + '*' * 40)


def pesquisar_conta_por_id():
    if possui_contas():
        numero_conta = int(input('Digite o número da conta que deseja pesquisar: '))
        conta = buscar_conta_por_numero(numero_conta)

        if conta:
            print(conta)
            sleep(2)
        else:
            print(f'Não foram encontradas contas com o número {numero_conta}. Verifique o número da conta!!')
            pesquisar_conta_por_id()


def pesquisar_cliente_por_id():

    if possui_clientes():
        numero_cliente = int(input('Digite o ID do cliente que deseja pesquisar: '))
        cliente = buscar_cliente_por_numero(numero_cliente)

        if cliente:
            print(cliente)
            sleep(2)
        else:
            print(f'Não encontramos cliente(s) com o número {numero_cliente}. Verifique o ID do cliente!!')
            pesquisar_cliente_por_id()


def imprimir_extrato():
    if possui_contas():
        numero_conta = int(input('Digite o número da conta que deseja verificar o extrato: '))
        conta = buscar_conta_por_numero(numero_conta)

        if conta:
            conta.exibir_extrato()
            sleep(2)
        else:
            print(f'Não foram encontradas contas com o número {numero_conta}. Verifique o número da conta!!')
            imprimir_extrato()


def buscar_conta_por_numero(numero_conta):
    for conta in contas:
        if numero_conta == conta.numero:
            return conta
    return None


def buscar_cliente_por_numero(id_cliente):
    for cliente in clientes:
        if id_cliente == cliente.id_cliente:
            return cliente
    return None


def valor_maior_q_zero(valor, tipo_operacao):
    if valor <= 0:
        print('\t\t Valor inválido!! Por favor digite um valor maior que 0, para efetuar sua operação!!')
        valor = ler_valor(tipo_operacao)
        return valor_maior_q_zero(valor, tipo_operacao)
    else:
        return True, valor


def saldo_insuficiente(valor, saldo_total, tipo_operacao):
    valida_valor, valor = valor_maior_q_zero(valor, tipo_operacao)

    if valida_valor:
        if valor > saldo_total:
            print(f'\t\t Você não possui saldo suficiente para saque!!\n\t\t Saldo Total: R$ {saldo_total: .2f}!!')
            valor = ler_valor(tipo_operacao)
            return saldo_insuficiente(valor, saldo_total, tipo_operacao)
        else:
            return True, valor


def valida_conta(conta, numero_conta, funcao_banco):
    if conta:
        return True
    else:
        print(f'Não foram encontradas contas com o número {numero_conta}. Verifique o número da conta!!')
        funcao_banco()


def ler_conta(msg='Digite a conta para a qual deseja transferir: '):
    numero_conta = int(input(msg))
    conta = buscar_conta_por_numero(numero_conta)

    return conta, numero_conta


def ler_valor(tipo_operacao):
    valor = float(input(f"Informe o valor que deseja {tipo_operacao}: R$ "))
    return valor


def possui_contas():
    return True if len(contas) > 0 else print('\t\t Ainda não possuem contas cadastradas!!')


def possui_clientes():
    return True if len(clientes) > 0 else print('\t\t Ainda não possuem clientes cadastrados!!')

def opcao_invalida():
    print('ERRO!!! Opção Inválida.\nPor favor, digite uma opção válida.')

