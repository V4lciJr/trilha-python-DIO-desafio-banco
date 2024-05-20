from banco import *
from menus import menu_cliente


def aplicacao_cliente():

    while True:
        op = menu_cliente()

        if op == 0:
            print('\t\t Agradecemos à preferência. É um prazer tê-lo conosco!!!')
            print('\t\t Volte Sempre!!!')
            sleep(2)
            break

        elif op == 1:
            criar_conta()

        elif op == 2:
            efetuar_saque()
        elif op == 3:
            efetuar_deposito()
        elif op == 4:
            efetuar_transferencia()
        elif op == 5:
            realizar_emprestimo()
        elif op == 6:
            imprimir_extrato()
        else:
            opcao_invalida()