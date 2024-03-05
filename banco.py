menu = '''
 ######## MENU #######
 ## 1 - Depositar   ##
 ## 2 - Sacar       ##
 ## 3 - Extrato     ##
 ## 0 - SAIR        ##
 #####################
 =>  '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        pass

    elif opcao == 2:
        pass
    elif opcao == 3:
        pass

    elif opcao == 0:
        print('Muito obrigado pela preferência. É um prazer tê-lo conosco\nVolte Sempre!!')
        break

    else:
        print('Erro!! Operação inválida. Digite uma operação válida.')