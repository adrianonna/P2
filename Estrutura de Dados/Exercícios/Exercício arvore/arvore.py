class No:
    def __ini__(self, dado, filhoEsq=None, filhoDir=None, pai=None):
        self._dado = dado
        self._filhoEsq = filhoEsq
        self._filhoDir = filhoDir
        self._pai = pai
    
    def getDado(self):
        return self._dado
    def setDado(self, dado):
        self._dado = dado

    def getfilhoEsq(self):
        return self._filhoEsq
    def setfilhoEsq(self, filhoEsq):
        self._filhoEsq = filhoEsq

    def getfilhoDir(self):
        return self._filhoDir
    def setfilhoDir(self, filhoDir):
        self._filhoDir = filhoDir

    def getpai(self):
        return self._pai
    def setpai(self, pai):
        self._pai = pai

class Arvore:
    def __ini__(self, raiz=None):
        self._raiz = raiz

    def addArvore(self, dado):
        no = No(dado)
        raiz = self._raiz
        if self._raiz == None:
            self._raiz = no
        elif raiz.getDado > dado: #adiciona no lado esquerdo
            if raiz.getfilhoEsq == None: #verifica se o primeiro filho esquerdo é None
                raiz.setfilhoEsq(no) #adicionar o No no primeiro filho esquerdo
            else:
                while raiz.getfilhoEsq != None: #enquanto o filho esquerdo for diferente de None
                    raiz = raiz.getfilhoEsq #atribui a raiz o proximo filho esquerdo
                raiz.setfilhoEsq(no) #quando encontrar o último filho esquerdo com None, atribui No a ele
        elif raiz.getDado < dado:
            if raiz.getfilhoDir == None: #verifica se o primeiro filho esquerdo é None
                raiz.setfilhoDir(no) #adicionar o No no primeiro filho esquerdo
            else:
                while raiz.getfilhoDir != None: #enquanto o filho esquerdo for diferente de None
                    raiz = raiz.getfilhoDir #atribui a raiz o proximo filho esquerdo
                raiz.setfilhoDir(no) #quando encontrar o último filho esquerdo com None, atribui No a ele

arvore=Arvore()
raiz = input('Digite o valor raiz: ')
arvore.addArvore(raiz)
valor = input('Digite o valor a ser inserido na árvore: ')
arvore.addArvore(valor)
valor = input('Digite o valor a ser inserido na árvore: ')
arvore.addArvore(valor)
valor = input('Digite o valor a ser inserido na árvore: ')
arvore.addArvore(valor)
# opcao = int(input('Digite 1 para esquerdo ou 2 para direito: '))
# while opcao < 1 or opcao > 2:
#     opcao = int(input('Opção inválida! Digite 1 para esquerdo ou 2 para direito: '))
# if opcao == 1:
#     valor = input('Digite o valor a ser inserido no lado esquerdo: ')
#     arvore.addArvore(valor)
# else:
#     valor = input('Digite o valor a ser inserido no lado direito: ')
#     arvore.addArvore(valor)