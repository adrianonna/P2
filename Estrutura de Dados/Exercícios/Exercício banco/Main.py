from Cliente import Cliente

clientes = list()
nome = input('Digite seu nome: ')
ag = int(input('Digite sua agencia: '))
cc = int(input('Digite sua conta-corrente: '))
saldo = float(input('Digite seu saldo: '))
print('\n')
clientes.append(Cliente(nome, ag, cc, saldo))
for i in range(1):
    nome = input('Digite seu nome: ')
    ag = int(input('Digite sua agencia: '))
    cc = int(input('Digite sua conta-corrente: '))
    #verifica se na mesma agência, já existe a conta-corrente digitada
    for j in range(len(clientes)):
        if clientes[j].ag == ag:
            while clientes[j].cc == cc:
                print('Conta-corrente já existente, digite outra!')#conta corrente iguais só não pode existir na condição se forem da mesma agência
                cc = int(input('Digite sua conta-corrente: '))
    saldo = float(input('Digite seu saldo: '))
    clientes.append(Cliente(nome, ag, cc, saldo))
print('\n')

aux = 10
print('Escolha a opção 1 para saque.')
print('Escolha a opção 2 para deposito.')
print('Escolha a opção 3 para transferencia.')
print('Escolha a opção 0 para sair.')
print('\n')
while (aux == 10):
    for i in range(len(clientes)):
        print('Cliente: {}'.format(clientes[i].nome))
        aux = int(input('Opção: '))
        while aux < 0 or aux > 3:
            print('Valor inválido')
            aux = int(input('Digite entre 1 a 3 para sua opção:  '))
        if aux == 1:
            saque = float(input('Digite o valor do saque: '))
            print('\n')
            total = clientes[i].saldo - saque
            while total < 0:
                print(clientes[i])
                saque = float(input('Saldo insuficiente! Digite um valor menor: '))
                total = clientes[i].saldo - saque
            clientes[i].Sacar(saque)
        if aux == 2:
            deposito = float(input('Digite o valor do deposito: '))
            clientes[i].Depositar(deposito)
        if aux == 3:
            conta = int(input('Digite a conta para transferir: '))
            qtde = 0
            while qtde == 0:
                for j in range(len(clientes)):
                    if clientes[j].cc == conta and clientes[i].cc != conta:
                        qtde += 1
                        transferencia = float(input('Digite o valor da transferencia: '))
                        total = clientes[i].saldo - transferencia
                        while total < 0:
                            transferencia = float(input('Saldo insuficiente! Digite um valor menor:'))
                            total = clientes[i].saldo - transferencia
                        clientes[i].Transferir(transferencia)
                        clientes[j].saldo += transferencia
                if qtde == 0 or clientes[i].cc == conta:
                    conta = int(input('Conta inválida, digite uma conta válida: '))
        if aux == 0:
            print('\n')
            break
        print('\n')
        aux = 10
        print('Escolha a opção 1 para saque.')
        print('Escolha a opção 2 para deposito.')
        print('Escolha a opção 3 para transferencia.')
        print('Escolha a opção 0 para sair.')
        print('\n')
for i in range(len(clientes)):
    print(clientes[i])