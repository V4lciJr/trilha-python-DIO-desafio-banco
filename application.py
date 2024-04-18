from menus import menu_apresentacao
from banco import banco

while True:

    print(menu_apresentacao())
    usuario = int(input('Qual o sue nível de usuário?\nDigite 1 para GERENTE e 2 para CLIENTE ou 0 para sair do '
                        'sistema: '))

    if usuario == 0:
        print('Muito obrigado pela preferência. É um prazer tê-lo conosco\nVolte Sempre!!')
        break
    elif usuario == 1:
        senha = input('Digite sua senha de acessso: ')
        if senha == '2123':
            banco(1)
        else:
            print('ERRO!! Senha inválida!!')
    elif usuario == 2:
        banco(2)
    else:
        print('ERRO!!! Opção Inválida.\nPor favor, digite uma opção válida.')

"""
    if opcao == 1:
        deposito = float(input('Digite o valor do depósito:R$ '))
        if deposito <= 0:
            print(f'Você tentou depositar R${deposito:.2f}, não é permitido valores menores ou igual a zero.\nDigite um valor válido.')
        else:
            saldo += deposito
            extrato += f'=> Depósito R${deposito:.2f}\n'

    elif opcao == 2:

        valor_saque = float(input('Digite o valor que deseja sacar:R$ '))

        if valor_saque > saldo:
            print(f'Você não possui saldo suficiente para sacar.\nSaldo R${saldo:.2f}')
        elif valor_saque > limite:
            print(f'Operação Inválida. Valor de saque maior do que o limite.\nLimite R${limite:.2f}')
        elif numero_saques >= LIMITE_SAQUES:
            print(f'Você ultrapassou o limite de saques diários.\nLimite de saques {LIMITE_SAQUES}')

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f'=> Saque: R$-{valor_saque:.2f}\n'
            numero_saques += 1

    elif opcao == 3:
        print('###### Extrato ######')
        print('Não foram realizadas movimentações!!' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('#####################')

    elif opcao == 0:
        print('Muito obrigado pela preferência. É um prazer tê-lo conosco\nVolte Sempre!!')
        break

    else:
        print('Erro!! Operação inválida. Digite uma operação válida.') """