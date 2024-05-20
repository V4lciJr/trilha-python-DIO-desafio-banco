def menu_cliente():
    print('''
         *************************************************
         ********************** ATM **********************
         ******************* DIO BANK ********************
         *************************************************
         ** O que você deseja fazer?         *************
         **                                  *************
         ** 1 - Criar conta                  *************
         ** 2 - Sacar                        *************
         ** 3 - Depositar                    *************
         ** 4 - Transferir                   *************
         ** 5 - Realizar empréstimo          *************
         ** 6 - Imprimir Extrato             *************           
         ** 0 - Sair do Sistema              *************
         *************************************************
         *************************************************
    ''')

    op = int(input("         => "))
    return op


def menu_gerente():
    print('''
             **************************************************
             ********************** ATM ***********************
             ******************* DIO BANK *********************
             **************************************************
             ** O que você deseja fazer?           ************
             **                                    ************
             ** 1  - Criar conta                   ************
             ** 2  - Sacar                         ************
             ** 3  - Depositar                     ************
             ** 4  - Transferir                    ************
             ** 5  - Conceder empréstimo           ************
             ** 6  - Imprimir Extrato              ************          
             ** 7  - Aumentar limite de Conta      ************
             ** 8  - Listar Contas                 ************
             ** 9  - Listar Clientes               ************
             ** 10 - Pesquisar Conta por Número    ************
             ** 11 - Pesquisar Cliente por Número  ************       
             ** 0  - Sair do Sistema               ************
             **************************************************
             **************************************************
        ''')

    op = int(input("         => "))
    return op


def menu_apresentacao():
    print('''
             ********************
             ******* MENU *******
             ** 1 - Gerente    **
             ** 2 - Cliente    **
             ** 0 - SAIR       **
             ********************
             ********************
     ''')

    op = int(input('Qual o sue nível de usuário?\nDigite 1 para GERENTE e 2 para CLIENTE ou 0 para sair do '
                            'sistema: '))
    return op


def menu_emprestimo(limite_emprestimo, total_a_pagar):
    print(f'Você pode pegar até R$ {limite_emprestimo:.2f} emprestados.')
    print(f'Esse valor pode ser dividido em até 48x de R$ {total_a_pagar / 48:.2f}')
    resp = int(input('O que deseja fazer?\n1 - Para realizar o empréstimo no valor integral\n2 - Para Outro Valor\nOU '
                 'QUALQUER TECLA PARA CANCELAR A OPERAÇÃO. '))
    return resp
