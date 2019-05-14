class No:
    def __init__(self, dado = None, proximo = None):
        self._dado = dado
        self._proximo = proximo
    
    def get_dado(self):
        return self._dado
    def set_dado(self, novoDado):
        self._dado = novoDado
    
    def get_proximo(self):
        return self._proximo
    def set_proximo(self, outro):
        self._proximo = outro

    def __str__(self):
        return '{}'.format(self._dado)

class Lista:
    def __init__(self, inicio = None, fim = None):
        self._inicio = inicio
        self._fim = fim

    def __str__(self):
        if self._inicio == None:
            return 'A lista está vazia'
        valorCorrente = self._inicio
        lista = 'A lista é: '
        while valorCorrente != None: #percorre a lista enquanto o primeiro elemento(dado) for diferente de None
            lista += str(valorCorrente.get_dado()) + ' ' #soma todos os dados de cada objeto percorrido na lista e converte para str para concatenar
            valorCorrente = valorCorrente.get_proximo() #recebe o valor do próximo objeto para continuar percorrendo a lista e comprar com None
        return lista

    def Vazia(self):
        if self._inicio == None: #se o primeiro elemento for None, é pq está vazia
            return 'A lista está vazia'
        else:
            return 'Ainda contem elementos na lista'

    def Busca(self, dado):
        if self._inicio == None: #verifica se a lista está vazia
            return None
        valorCorrente = self._inicio #pego o primeiro valor da lista
        while valorCorrente != None: #percorre a lista enquanto o objeto for diferente de None
            if valorCorrente.get_dado() == dado: #verifica se o dado desse objeto corrente é igual ao dado passado
                return 'O valor está na lista' #retorna o objeto procurado
            valorCorrente = valorCorrente.get_proximo() #atualiza a variável que percorre a lista para o próximo objeto enquanto não achar o valor
        return None #returna None se o dado não estiver na lista

    def Inserir(self, dado, posicao): #inserir depois do valor informado, se houver dois iguais, depois do primeiro que seja igual
        no = No(dado) #transformo o que vou inserir em um No(objeto)
        valorCorrente = self._inicio #variável que vai percorrer a lista
        while valorCorrente != None:
            if valorCorrente.get_dado() == posicao: #se o dado do objeto for igual ao valor informado
                no.set_proximo(valorCorrente.get_proximo())  #o novo objeto(No) aponta para o próximo do objeto atual
                valorCorrente.set_proximo(no) #o objeto atual aponta para o novo objeto(No)
                break
            valorCorrente = valorCorrente.get_proximo() #variável pula para a próxima posiçao da lista
        return None

    def addInicio(self, dado):
        p = No(dado)
        if self._inicio == None: #se o primeiro elemento for None, não existe elemento na lista
            self._inicio = p #adiciona o objeto no inicio
            self._fim = p #adiciona o mesmo objeto no fim, pois a lista estava vazia
        else:
            p.set_proximo(self._inicio) #aponta para o primeiro item da lista
            self._inicio = p #o primeiro item se tonar o objeto(dado) e o que era o inicio, se torna o proximo desse objeto

    def addFim(self, dado):
        p = No(dado)
        if self._inicio == None:
            self._inicio = p
            self._fim = p
        else:
            self._fim.set_proximo(p) #faz o proximo do ultimo elemento apontar para novo item
            self._fim = p #o ultimo elemento se torna o objeto(dado) passado

    def removeInicio(self):
        if self._inicio == None: #verifica se está vazia e não faz nada se estiver
            print('A lista já está vazia')
        elif self._inicio == self._fim: #se só existir um objeto na lista, o exclui atribuindo None para inicio e fim
            self._inicio = None
            self._fim = None
        else:
            self._inicio = self._inicio.get_proximo() #aponta o primeiro para o próximo desse primeiro

    def removeFim(self):
        if self._inicio == None:
            print('A lista já está vazia')
        elif self._inicio == self._fim:
            self._inicio = None
            self._fim = None
        else:
            valorCorrente = self._inicio #variável que vai percorrer
            while valorCorrente.get_proximo() != self._fim: #vai percorrer até o objeto anterior(penúltimo) ao ultimo
                valorCorrente = valorCorrente.get_proximo() #variável vai assumindo o valor do próximo objeto
            valorCorrente.set_proximo(None) #penúltimo objeto vai apontar para None e não mais para o ultimo
            self._fim = valorCorrente

p = Lista()
print('A lista de elementos está vazia ', p)
opcao = 1
while opcao != 8:
    print('\n')
    print('1 para adicionar no início\n2 para adicionar no final\n3 para remover do início\n4 para remover do final')
    print('5 para buscar um valor\n6 para verificar se a lista está vazia\n7 para inserir um elemento no meio da lista\n8 para sair do loop')
    opcao = int(input('Digite sua opção: '))
    while opcao < 1 and opcao > 8:
        opcao = int(input('Opção inválida, digite entre 1 e 5.'))
    if opcao == 1:
        valor = input('Digite o que deseja adicionar no início da lista: ')
        p.addInicio(valor)
    elif opcao == 2:
        valor = input('Digite o que deseja adicionar no final da lista: ')
        p.addFim(valor)
    elif opcao == 3:
        p.removeInicio()
    elif opcao == 4:
        p.removeFim()
    elif opcao == 5:
        valor = input('Digite o valor que deseja procurar na lista: ')
        p.Busca(valor)
    elif opcao == 6:
        p.Vazia()
    elif opcao == 7:
        valorCorrente = input('Informe o valor da posição onde o elemento irá ser inserido posteriormente: ')
        valor = input('Informe o valor a ser inserido: ')
        p.Inserir(valor, valorCorrente)

    print(p)