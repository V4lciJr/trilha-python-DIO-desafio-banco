from banco import *
from menus import menu_gerente


def aplicacao_gerente():

    while True:
        op = menu_gerente()
        if op == 0:
            print('\t\t Agradecemos à preferência. É um prazer tê-lo conosco!!!')
            print('\t\t Volte Sempre!!!')
            sleep(2)
            break
        if op == 1:
            criar_conta()
        elif op == 2:
            efetuar_saque()
        elif op == 3:
            efetuar_deposito()
        elif op == 4:
            efetuar_transferencia()
        elif op == 5:
            realizar_emprestimo(1)
        elif op == 6:
            imprimir_extrato()
        elif op == 7:
            aumentar_limite_conta()
        elif op == 8:
            listar_contas()
        elif op == 9:
            listar_clientes()
        elif op == 10:
            pesquisar_conta_por_id()
        elif op == 11:
            pesquisar_cliente_por_id()
        else:
            opcao_invalida()