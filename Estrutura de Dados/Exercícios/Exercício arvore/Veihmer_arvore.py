import arvore

print('\033[33m' + '\tÁrvore Binária' + '\033[0;0m')

raiz = None

while True:
    arvore.imprimeMenu()
    select = int(input('\033[31m' + 'Opção:' + '\033[0;0m'))

    if select == 1:
        '''
        print('\nInsira as informações do contato!')
        raiz = insere(raiz, No(input('\033[33m'+'Nome:'+'\033[0;0m'), input('\033[33m'+'Telefone: ''\033[0;0m'), input('\033[33m'+'e-mail: '+'\033[0;0m')))
        '''
        # DEFAULT
        raiz = arvore.insere(raiz, arvore.No('levy', 83, 'levy@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('bia', 83, 'bia@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('alberto', 83, 'alberto@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('levy', 83, 'levyfagundes@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('carlos', 83, 'carlos@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('maria', 83, 'maria@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('vanessa', 83, 'vanessa@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('A', 83, 'levy@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('B', 83, 'bia@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('C', 83, 'alberto@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('D', 83, 'levyfagundes@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('E', 83, 'carlos@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('F', 83, 'maria@gmail.com'))
        raiz = arvore.insere(raiz, arvore.No('vanessa', 83, 'vanessa@gmail.com'))


    elif select == 2:
        print('\nQual o contato que deseja localizar?')
        key = input('\033[33m' + 'Nome:' + '\033[0;0m')
        print('-' * 30)
        print('\n{}\n'.format(arvore.busca_contato(raiz, key)))
        print('-' * 30)


    elif select == 3:
        print('\nContato que deseja excluir:')
        key = input('\033[33m' + 'Nome:' + '\033[0;0m')
        arvore.remove(raiz, key)


    elif select == 4:
        print('-' * 30)
        print('\033[33m' + '\tLista de contatos\n' + '\033[0;0m')
        print('\n{}\n'.format(arvore.emOrdem(raiz)))
        print('-' * 30)


    elif select == 5:
        print('\nAltura da Árvore: {}'.format(arvore.altura(raiz)))


    elif select == 6:
        print('\n\033[33m' + '\tPrograma Finalizado!' + '\033[0;0m\n')
        break


    elif select == 7:
        print('-' * 30)
        print('\033[33m' + '\tNós a esquerda\n' + '\033[0;0m')
        print('{}'.format(arvore.verEsquerda(raiz)))
        print('-' * 30)


    elif select == 8:
        print('-' * 30)
        print('\033[33m' + '\tNós a direita\n' + '\033[0;0m')
        print('{}'.format(arvore.verDireita(raiz)))
        print('-' * 30)

    elif select == 9:
        key = input()
        print(arvore.isFolha(raiz, key))

--------------------------------  #######-----------------------------------------------


class No:
    def _init_(self, dado):
        self._dado = None
        self._filhoesquerdo = None
        self._filhodireito = None
        self._pai = None

    def getDado(self):
        return self._dado

    def setDado(self, NovoDado):
        return self._dado = Novo

    def getFilhoesquerdo(self):
        return self._filhoesquerdo

    def setFilhoesquerdo(self, NovoFilho):
        return self._filhoesquerdo = NovoFilho

    def getFilhodireito(self):
        return self._filhodireito

    def setFilhodireito(self, NovoFilho):
        return self._filhodireito = NovoFilho

    def getPai(self):
        return self._pai

    def setPai(self, NovoPai):
        return self._pai = NovoPai

    def _str_(self):
        return str("No: " + str(self._dado()))


class Arvore_Binaria(No):

    def _init_(self):
        self._raiz = None

    def getRaiz(self):
        return self._raiz

    def setRaiz(self, NovaRaiz):
        return self._raiz = NovaRaiz

    def BuscaSimples(self, x, d):
        if (x == None or x.getDado() == d):
            return x
        elif (d < x.getDado()):
            return self.BuscaSimples(x.getFilhoesquerdo(), d)
        else:
            return self.BuscaSimples(x.getFilhodireito(), d)

    def BuscaBinaria(vetor, i, f, x):
        if (i < f):
            meio = (i + f) // 2

            if (x > vetor[meio]):
                return BuscaBinaria(vetor, (meio + 1), f, x)
            elif (x < vetor[meio]):
                return BuscaBinaria(vetor, i, (meio - 1), d)
        else:
            return q

    def Minimo(self, x):
        while x.getFilhoesquerdo() is not None:
            x = x.getFilhoesquerdo()
        return x

    def Maximo(self, x):
        while x.getFilhodireito() is not None:
            x = x.getFilhodireito
        return x

    def Sucessor(self, x):
        if x.getFilhodireito() != None:
            return self.Minimo(x.getFilhodireito())
        y = x.getPai()
        while y != None and x is y.getFilhodireito:
            x = y
            y = y.getPai()
        return y

        def Predecessor(self, x):
            if x.getFilhoesquerdo() != None:
                return self.Maximo(x.getFilhoesquerdo())
            y = x.getPai()
            while y != None and x is y.getFilhoesquerdo():
                x = y
                y = getPai()
            return y

        def inserir(self, z):
            y = None
            x = self.getRaiz()
            while x != None:
                y = x
                if z.getDado() < y.getDado():
                    x = x.getFilhoesquerdo()
                else:
                    x = x.getFilhodireito()
            z.setPai(y)
            if y == None:
                self.setRaiz(z)
            else:
                if z.getDado() < y.getDado():
                    y.setFilhoesquerdo(z)
            else:
            y.setFilhodireito(z)

    def remover(self, x):
        if x.getFilhoesquerdo() == None or x.getFilhodireito() == None:
            y = x
        else:
            y = self.Sucessor(x)
        if y.getFilhoesquerdo() != None:
            z = y.getFilhoesquerdo()
        else:
            z = getFilhodireito()
        if z != None:
            z.setPai(y.getPai())
        if y.getPai() == None:
            self.setRaiz(z)
        else:
            if y == y.getPai().getfilho():
                y.getPai().setFilhoesquerdo(z)
            else:
                y.getPai().setFilhodireito(z)
        if y != x:
            x.setDado(y.getDado)

else:
result = lefty(tree.rigth)
left

class No:
    def _init_(self, data):
        self.data = data
        self.setaFilhos(None, None)

    def setaFilhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def balanco(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def rotacaoEsquerda(self):
        self.data, self.direita.data = self.direita.data, self.data
        old_esquerda = self.esquerda
        self.setaFilhos(self.direita, self.direita.direita)
        self.esquerda.setaFilhos(old_esquerda, self.esquerda.esquerda)

    def rotacaoDireita(self):
        self.data, self.esquerda.data = self.esquerda.data, self.data
        old_direita = self.direita
        self.setaFilhos(self.esquerda.esquerda, self.esquerda)
        self.direita.setaFilhos(self.direita.direita, old_direita)

    def rotacaoEsquerdaDireita(self):
        self.esquerda.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self.direita.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.esquerda.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.direita.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def insere(self, data):
        if data <= self.data:
            if not self.esquerda:
                self.esquerda = No(data)
            else:
                self.esquerda.insere(data)
        else:
            if not self.direita:
                self.direita = No(data)
            else:
                self.direita.insere(data)
        self.executaBalanco()

    def imprimeArvore(self, indent=0):
        print
        " " * indent + str(self.data)
        if self.esquerda:
            self.esquerda.imprimeArvore(indent + 2)
        if self.direita:
            self.direita.imprimeArvore(indent + 2)