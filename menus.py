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
         ** 5 - Imprimir Extrato             *************          
         ** 0 - Sair do Sistema              *************
         *************************************************
    ''')

    op = int(input("         => "))
    return op


def menu_gerente():
    print('''
             *************************************************
             ********************** ATM **********************
             ******************* DIO BANK ********************
             *************************************************
             ** O que você deseja fazer?          ************
             **                                   ************
             ** 1 - Criar conta                   ************
             ** 2 - Criar Cliente                 ************
             ** 3 - Sacar                         ************
             ** 4 - Depositar                     ************
             ** 5 - Transferir                    ************
             ** 6 - Aumentar limite de Conta      ************
             ** 7 - Listar Contas                 ************
             ** 8 - Listar Clientes               ************
             ** 9 - Pesquisar Conta por Número    ************
             ** 10 - Pesquisar Cliente por Número ************
             ** 11 - Imprimir Extrato             ************          
             ** 0 - Sair do Sistema               ************
             *************************************************
        ''')

    op = int(input("         => "))
    return op


def menu_apresentacao():
    menu = '''
     ######## MENU #######
     ## 1 - Gerente     ##
     ## 2 - Cliente     ##
     ## 0 - SAIR        ##
     #####################
     '''
    return menu
