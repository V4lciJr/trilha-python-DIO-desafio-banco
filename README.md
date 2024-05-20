
# Desafio: Criando um sistema banc�rio

## Objetivo Geral
Criar um sistema banc�rio com as opera��es: sacar, depositar e visualizar extrato.

## Sistema
De in�cio essa era ideia, criar um sistema banc�rio simples, que tivesse apenas como opera��es: saque, dep�sito e imprimir extrato, mas, as ideias foram surgindo e o sistema cresceu um pouco. Contando com dois m�dulos de aplica��es, temos o m�dulo cliente e o m�dulo gerente, o segundo possui mais opera��es de manipula��es de conta.<br>
No total, o sistema conta com 11 opera��es que, apenas o perfil gerente, tem acesso a todas elas, s�o elas:
- Criar Conta
- Sacar
- Depositar
- Transferir
- Conceder ou Realizar empr�stimo
- imprimir extrato
- Aumentar limite de Contas
- Listar contas
- Listar Clientes
- Pesquisar conta por n�mero
- Pesquisar cliente por n�mero

## Menus
O primeiro menu exibido � o tipo de usu�rio, se ele � um cliente normal ou se � um gerente, caso ele seja um gerente, � solicitado uma senha, que � super dif�cil, criptografia da NASA, caso ele responda "1234" o menu gerente � apresentado, caso a senha n�o seja essa sequ�ncia de n�meros, uma mensagem indicando que a senha � inv�lida � impressa. No caso do cliente, ele n�o precisa de nenhuma senha de acesso, apenas escolhendo a op��o 2, j� possui acesso ao menu e as opera��es permitidas para o cliente. Abaixo segue um overview dos menus:

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
             ** O que voc� deseja fazer?           ************
             **                                    ************
             ** 1  - Criar conta                   ************
             ** 2  - Sacar                         ************
             ** 3  - Depositar                     ************
             ** 4  - Transferir                    ************
             ** 5  - Conceder empr�stimo           ************
             ** 6  - Imprimir Extrato              ************          
             ** 7  - Aumentar limite de Conta      ************
             ** 8  - Listar Contas                 ************
             ** 9  - Listar Clientes               ************
             ** 10 - Pesquisar Conta por N�mero    ************
             ** 11 - Pesquisar Cliente por N�mero  ************       
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
         ** O que voc� deseja fazer?         *************
         **                                  *************
         ** 1 - Criar conta                  *************
         ** 2 - Sacar                        *************
         ** 3 - Depositar                    *************
         ** 4 - Transferir                   *************
         ** 5 - Realizar empr�stimo          *************
         ** 6 - Imprimir Extrato             *************           
         ** 0 - Sair do Sistema              *************
         *************************************************
         *************************************************
~~~

## Opera��es
### Criar Conta
Essa op��o solicitar� os dados do cliente, como nome, cpf e etc, bem como os dados do seu endere�o, em seguida ela cria a conta do cliente no sistema. Essa � fun��o que praticamente n�o tem valida��o, portanto, nome, cpf, email e ..., como s�o strings, o sistema vai aceitar qualquer coisa que seja uma string, na data de nascimento, caso n�o esteja no padr�o (dd/mm/aaaa) o programa dar� um erro e parar� a execu��o, esse tratamento ser� feito com exce��es futuramente. Ao criar a conta ele exibe no painel conta criada com sucesso, contendo os dados principais da conta.

### Sacar
Com a conta cadastrada, podemos fazer qualquer opera��o e uma delas � o saque, como a conta � criada j� com um limite de cheque especial de R$ 500,00(� um banco "camarada"), caso o usu�rio esteja no aperto pode sacar at� esse valor, acima disso, a opera��o n�o permite. A fun��o de saque ela valida se possui saldo e se o valor � maior que zero para poder efetuar a opera�ao. Mas, o sistema s� permite 3 saques di�rios, essa foi uma medida imposta no projeto(pegando a l�gica dos caixas 24hs, quem sabe futuramente os 3 saques s�o gr�tis e a partir do quarto, o banco cobre uma taxinha amiga).

### Depositar
A opera��o de dep�sito primeiro valida se o valor � maior que zero e tamb�m assim como as outras, valida se a conta existe para poder efetuar a opera��o, em seguida pega o valor digitado e soma com o saldo da conta.

### Transferir
A opera��o faz todas as valida��es de saque e dep�sito, como tamb�m se as contas de origem e destino existem, por baixo dos panos e para simplificar, a fun��o de transferir ela efetua um "saque" na conta de origem e faz um dep�sito na conta destino.

### Conceder ou Realizar empr�stimo
Essa foi a fun��o que mais gostei de fazer, ela como todas as outras verifica primeiro se o cliente possui conta, caso sim, � solicitado o sal�rio do cliente e o valor da parcela, por que como eu mencionei mais acima, esse banco � um banco "camarada" e n�o concede empr�stimos com parcelas que comprometam mais de 20% do sal�rio informado, caso esteja dentro dos padr�es, ele faz um c�lculo do limite de empr�stimo � ser pago em at� 48 parcelas do valor informado pelo cliente, com isso ele escolhe se pega o valor do limite de empr�stimo que � mostrado em tela ou se ele escolhe um valo menor, mas ele n�o pode pegar um valor maior que o limite mostrado em tela ou pegar dois empr�stimos, esse banco s� permite um empr�stimo por conta, � um banco "seguro" hahahahah.

### Imprimir Extrato
Essa opera��o deve listar todos os dep�sitos, saques e transfer�ncias realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, deve exibir a mensagem: **N�o foram realizadas movimenta��es**
Os valores devem ser exibidos utilizando R$ xxx.xx.

### Aumentar Limite de Conta
O aumentar limite de conta, � uma das opera��es que quem tem a permiss�o para us�-la � o perfil de gerente, s� ele pode aumentar o limite do cheque especial do cliente, que � o que acontece � uma ag�ncia banc�ria no dia � dia; sua funcionalidade � simples, ela acessa a property setter do atributo limite e seta o novo valo de limite.

### Listar Contas
Opera��o b�sica e auxiliar, verifica se possui contas cadastradas, caso a resposta seja sim, ela varre a lista de contas e exibe o relat�rio na tela.

### Listar Clientes
Esta opera��o segue mesma l�gica da fun��o listar contas, a diferen�a � que ela percorre uma lista de clientes, que caso existam cadastrados, ele imprime o relat�rio na tela.

### Pesquisar cliente Conta e Pesquisar cliente por n�mero
Esas opera��es tamb�m possuem l�gicas semelhantes. Primeiro elas validam se possuem contas ou clientes cadastrados, caso sim, validam se possuem contas ou clientes com n�mero que foi solicitado, caso sim imprime-se os dados na tela, caso n�o, uma mensagem informado que n�o foram encontradas contas ou clientes com aquele n�mero, � exibida.


> Este projeto foi desenvolvido no Bootcamp **Pot�ncia Tech Powered by iFood | Ci�ncia de Dados** e aprimorado por Valci J�nior que � o usu�rio deste gitHub, este projeto ainda necessita de v�rias valida��ees anti usus�rio bem como um melhor tratamento de erros e exce��es, que tendem � ser implementados com o tempo(mas n�o temos prazos).<br>
> Espero que este projeto ou essas implementa��es venham � ajuda e auxiliar estudantes da �rea, com desafios semelhantes.
> 
> Qualquer d�vida ou sugest�o, voc� pode criar uma issue ou entrar em contato pelo linkedIn: <https://www.linkedin.com/in/valci-j%C3%BAnior-023818122/> 
