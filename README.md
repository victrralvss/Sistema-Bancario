# Sistema Bancário :bank:

### OBJETIVO 🎯

Desenvolvi o programa a fim de por a teste as minhas habilidades com os conceitos fundamentais da linguagem Python.
A implementação de um banco digital foi perfeito para isso, consegui explorar bem os conceitos de POO dentro da linguagem, bem como ter a oportunidade de escrever um código robusto e aplicar as boas práticas a ele (tenho muito a melhorar) mas foi o suficiente para aprender a pensar no código antes de realmente escrevé-lo!


### FUNCIONAMENTO ⚙️

Toda operação é precidada pela tela de menu, o usuário é livre para escolher qualquer uma das opções, porém um cadastro no banco é necessário para que ele poça ser identificado e o banco saiba de qual conta estamos nos referindo.

![image](https://user-images.githubusercontent.com/90868283/202946508-7006b290-8520-48a6-bf59-6bbbc4816b1d.png)

Portanto, o caminho ideal do programa será:

__[6] NOVO USUÁRIO__
  
  * Para se cadastrar no banco há 3 informações necessárias de serem informadas: CPF | NOME | IDADE
  * O endereço será opcional, mas pode ser registrado no cadastro do cliente dado:  NUMERO | RUA | BAIRRO | CIDADE | ESTADO
  * Validado todas as entradas seu usuário será registrado, o programa irá usar seu CPF como identificador para realizar as opções disponíveis
  
__[4] CIRAR CONTA__
  * Caso o CPF informado não esteja registrado a operação é cancelada
  * Com um registro no banco, agora é possível criar uma ou mais contas que serão associadas ao seu CPF para futuras consultas
  * Com uma conta criada, as operações de DEPÓSITO | SAQUE | EXTRATO | LISTAR CONTAS estáo disponíveis
  
__[5 LISTAR CONTA__
  * Caso o CPF informado não esteja registrado ou ainda não tenha uma conta associada e ele, a operação é cancelada
  * Caso mais de uma conta esteja associada ao CPF informado, uma lita com as suas contas será apresentada e o cliente poderá escolher o número da que deseja operar
  * Você pode consultar todas as contas associadas ao seu CPF aqui
  * Não há limite de contas
    
__[1] DEPÓSITO__ 
  * Caso o CPF informado não esteja registrado ou ainda não tenha uma conta associada e ele, a operação é cancelada
  * Caso mais de uma conta esteja associada ao CPF informado, uma lita com as suas contas será apresentada e o cliente poderá escolher o número da que deseja operar
  * Validada a conta, será necessário informar o valor do depósito

__[2] SAQUE__
  * Caso o CPF informado não esteja registrado ou ainda não tenha uma conta associada e ele, a operação é cancelada
  * Caso mais de uma conta esteja associada ao CPF informado, uma lita com as suas contas será apresentada e o cliente poderá escolher o número da que deseja operar
 
