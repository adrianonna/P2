from Cliente3 import Cliente
from ContaCorrente3 import ContaCorrente

clientes = list()
nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF(apenas números): ')
while len(cpf) <= 10 or len(cpf) >= 12:
    cpf = input('CPF inválido! Digite novamente: ')
qtde = 0
cpf2 = []
for i in cpf:
    cpf2.append(i)
    qtde += 1
    if qtde == 3:
        cpf2.insert(3, '.')
    if qtde == 6:
        cpf2.insert(7, '.')
    if qtde == 9:
        cpf2.insert(11, '-')
novoCPF = ''.join(cpf2)
ag = int(input('Digite sua agência: '))
cc = int(input('Digite sua conta-corrente: '))
saldo = float(input('Digite seu saldo: '))
print('\n')
cliente = Cliente(nome, novoCPF)
clientes.append(ContaCorrente(cliente, cc, ag, saldo))
for i in range(1):
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')
    while len(cpf) <= 10 or len(cpf) >= 12:
        cpf = input('CPF inválido! Digite novamente: ')
    qtde = 0
    cpf2 = []
    for c in cpf:
        cpf2.append(c)
        qtde += 1
        if qtde == 3:
            cpf2.insert(3, '.')
        if qtde == 6:
            cpf2.insert(7, '.')
        if qtde == 9:
            cpf2.insert(11, '-')
    novoCPF = ''.join(cpf2)
    for j in range(len(clientes)):
        while clientes[j].getCliente().getCPF() == novoCPF:
            cpf = input('CPF já existente. Digite outro CPF: ')
            while len(cpf) <= 10 or len(cpf) >= 12:
                cpf = input('CPF inválido! Digite novamente: ')
            qtde = 0
            cpf2 = []
            for c in cpf:
                cpf2.append(c)
                qtde += 1
                if qtde == 3:
                    cpf2.insert(3, '.')
                if qtde == 6:
                    cpf2.insert(7, '.')
                if qtde == 9:
                    cpf2.insert(11, '-')
            novoCPF = ''.join(cpf2)
    ag = int(input('Digite sua agência: '))
    cc = int(input('Digite sua conta-corrente: '))
    for j in range(len(clientes)):
        if clientes[j].getAg() == ag:
            while clientes[j].getCc() == cc:
                cc = int(input('Conta-corrente já existente nessa agência, digite outra conta: '))
    saldo = float(input('Digite seu saldo: '))
    cliente = Cliente(nome, novoCPF)
    clientes.append(ContaCorrente(cliente, cc, ag, saldo))

aux = 1
print('\n')
while (aux > 0 and aux < 4):
    print('Escolha a opção 1 para saque.')
    print('Escolha a opção 2 para deposito.')
    print('Escolha a opção 3 para saldo.')
    print('Escolha a opção 4 para transferência.')
    print('Escolha a opção 0 para sair.')
    aux = int(input('Opção: '))
    while aux < 0 or aux > 4:
        print('Opção inválida')
        aux = int(input('Digite entre 0 a 3 para sua opção: '))
    if aux == 1:
        conta = int(input('Digite a conta que deseja sacar: '))
        saque = float(input('Digite o valor do saque: '))
        for i in range(len(clientes)):
            if clientes[i].getCc() == conta:
                total = clientes[i].getSaldo() - saque
                while total < 0:
                    print(clientes[i])
                    saque = float(input('Saldo insuficiente, digite um valor menor: '))
                    total = clientes[i].getSaldo() - saque
                clientes[i].Sacar(saque)
        print('\n')
    if aux == 2:
        conta = int(input('Digite a conta que deseja depositar: '))
        deposito = float(input('Digite o valor do deposito: '))
        for i in range(len(clientes)):
            if clientes[i].getCc() == conta:
                clientes[i].Depositar(deposito)
    if aux == 3:
        conta = int(input('Digite a conta para verificar seu saldo: '))
        for i in range(len(clientes)):
            if clientes[i].getCc() == conta:
                print(clientes[i].saldo)
    if aux == 4:
        conta = int(input('Digite a conta do transferente: '))
        conta2 = int(input('Digite a conta do transferido: '))
        transferencia = float(input('Digite o valor a ser transferido: '))
        for i in range(len(clientes)):
            if conta == clientes[i].getCc():
                total = clientes[i].getSaldo() - transferencia
                while total < 0:
                    print(clientes[i])
                    transferencia = float(input('Saldo insuficiente, digite um valor menor: '))
                    total = clientes[i].getSaldo() - transferencia
                clientes[i].Sacar(transferencia)
                for j in range(len(clientes)):
                    if conta2 == clientes[j].getCc():
                        clientes[j].Transferir(transferencia)
    if aux == 0:
        print('\n')
        break
    print('\n')
for i in range(len(clientes)):
    print(clientes[i])
    print('\n')
