
# Desafio: Criando um sistema bancário

## Objetivo Geral
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

## Sistema
De início essa era ideia, criar um sistema bancário simples, que tivesse apenas como operações: saque, depósito e imprimir extrato, mas, as ideias foram surgindo e o sistema cresceu um pouco. Contando com dois módulos de aplicações, temos o módulo cliente e o módulo gerente, o segundo possui mais operações de manipulações de conta.<br>
No total, o sistema conta com 11 operações que, apenas o perfil gerente, tem acesso a todas elas, são elas:
- Criar Conta
- Sacar
- Depositar
- Transferir
- Conceder ou Realizar empréstimo
- imprimir extrato
- Aumentar limite de Contas
- Listar contas
- Listar Clientes
- Pesquisar conta por número
- Pesquisar cliente por número

## Menus
O primeiro menu exibido é o tipo de usuário, se ele é um cliente normal ou se é um gerente, caso ele seja um gerente, é solicitado uma senha, que é super difícil, criptografia da NASA, caso ele responda "1234" o menu gerente é apresentado, caso a senha não seja essa sequência de números, uma mensagem indicando que a senha é inválida é impressa. No caso do cliente, ele não precisa de nenhuma senha de acesso, apenas escolhendo a opção 2, já possui acesso ao menu e as operações permitidas para o cliente. Abaixo segue um overview dos menus:

### Menu de Inicial
~~~
             ********************
             ******* MENU *******
             ** 1 - Gerente    **
             ** 2 - Cliente    **
             ** 0 - SAIR       **
             ********************
             ********************
     
~~~
### Menu Gerente
~~~
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
~~~

### Menu do Cliente
~~~
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
~~~

## Operações
### Criar Conta
Essa opção solicitará os dados do cliente, como nome, cpf e etc, bem como os dados do seu endereço, em seguida ela cria a conta do cliente no sistema. Essa é função que praticamente não tem validação, portanto, nome, cpf, email e ..., como são strings, o sistema vai aceitar qualquer coisa que seja uma string, na data de nascimento, caso não esteja no padrão (dd/mm/aaaa) o programa dará um erro e parará a execução, esse tratamento será feito com exceções futuramente. Ao criar a conta ele exibe no painel conta criada com sucesso, contendo os dados principais da conta.

### Sacar
Com a conta cadastrada, podemos fazer qualquer operação e uma delas é o saque, como a conta é criada já com um limite de cheque especial de R$ 500,00(é um banco "camarada"), caso o usuário esteja no aperto pode sacar até esse valor, acima disso, a operação não permite. A função de saque ela valida se possui saldo e se o valor é maior que zero para poder efetuar a operaçao. Mas, o sistema só permite 3 saques diários, essa foi uma medida imposta no projeto(pegando a lógica dos caixas 24hs, quem sabe futuramente os 3 saques são grátis e a partir do quarto, o banco cobre uma taxinha amiga).

### Depositar
A operação de depósito primeiro valida se o valor é maior que zero e também assim como as outras, valida se a conta existe para poder efetuar a operação, em seguida pega o valor digitado e soma com o saldo da conta.

### Transferir
A operação faz todas as validações de saque e depósito, como também se as contas de origem e destino existem, por baixo dos panos e para simplificar, a função de transferir ela efetua um "saque" na conta de origem e faz um depósito na conta destino.

### Conceder ou Realizar empréstimo
Essa foi a função que mais gostei de fazer, ela como todas as outras verifica primeiro se o cliente possui conta, caso sim, é solicitado o salário do cliente e o valor da parcela, por que como eu mencionei mais acima, esse banco é um banco "camarada" e não concede empréstimos com parcelas que comprometam mais de 20% do salário informado, caso esteja dentro dos padrões, ele faz um cálculo do limite de empréstimo à ser pago em atá 48 parcelas do valor informado pelo cliente, com isso ele escolhe se pega o valor do limite de empréstimo que é mostrado em tela ou se ele escolhe um valo menor, mas ele não pode pegar um valor maior que o limite mostrado em tela ou pegar dois empréstimos, esse banco só permite um empréstimo por conta, é um banco "seguro" hahahahah.

### Imprimir Extrato
Essa operação deve listar todos os depósitos, saques e transferências realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, deve exibir a mensagem: **Não foram realizadas movimentações**
Os valores devem ser exibidos utilizando R$ xxx.xx.

### Aumentar Limite de Conta
O aumentar limite de conta, é uma das operações que quem tem a permissão para usá-la é o perfil de gerente, só ele pode aumentar o limite do cheque especial do cliente, que é o que acontece é uma agência bancária no dia à dia; sua funcionalidade é simples, ela acessa a property setter do atributo limite e seta o novo valo de limite.

### Listar Contas
Operação básica e auxiliar, verifica se possui contas cadastradas, caso a resposta seja sim, ela varre a lista de contas e exibe o relatório na tela.

### Listar Clientes
Esta operação segue mesma lógica da função listar contas, a diferença é que ela percorre uma lista de clientes, que caso existam cadastrados, ele imprime o relatório na tela.

### Pesquisar cliente Conta e Pesquisar cliente por número
Esas operações também possuem lógicas semelhantes. Primeiro elas validam se possuem contas ou clientes cadastrados, caso sim, validam se possuem contas ou clientes com número que foi solicitado, caso sim imprime-se os dados na tela, caso não, uma mensagem informado que não foram encontradas contas ou clientes com aquele número, é exibida.


> Este projeto foi desenvolvido no Bootcamp **Potência Tech Powered by iFood | Ciência de Dados** e aprimorado por Valci Júnior que é o usuário deste gitHub, este projeto ainda necessita de várias validaçõees anti ususário bem como um melhor tratamento de erros e exceções, que tendem à ser implementados com o tempo(mas não temos prazos).<br>
> Espero que este projeto ou essas implementações venham à ajuda e auxiliar estudantes da área, com desafios semelhantes.
> 
> Qualquer dúvida ou sugestão, você pode criar uma issue ou entrar em contato pelo linkedIn: <https://www.linkedin.com/in/valci-j%C3%BAnior-023818122/> 
