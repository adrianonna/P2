class No:
    def __init__(self, dado = None, proximo = None): #anterior = None):
        self._dado = dado
        self._proximo = proximo
        #self.anterior = anterior
    
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

class Encadeamento:
    def __init__(self, no):
        self._no = No
        self._lista = []

    def add_inicio(self, no):
        self._lista.append(No())
        print(No())
        # p = self._no._dado
        # No._proximo = p
        #self._no.set_proximo(No)

    def add_fim(self, No):
        i = 0
        while self._no.get_proximo() != None:
            p = self._lista[i].get_proximo()
            ++i
        p.set_proximo(No)

    def __str__(self):
        return '{}, {}'.format(self._no, self._lista)

cabeca = No(1)
lista = Encadeamento(cabeca)
lista.add_inicio(No(2))
lista.add_inicio(No(3))
lista.add_inicio(No(4))
print(lista)

    # def AddFim(self, No):
    #     if (self._cabeca != None):
    #         self._fim.get_proximo().set_proximo(No)#é preciso usar o get_proximo para pegar a área de memória "proximo" do fim?
    #     else:
    #         self._cabeca = No

    # def AddInicio(self, No):
    #     No.set_proximo(self._cabeca)

        # if len(self._lista) == 0:
        #     self._lista[0] = No
        # else:
        #     aux = self._lista[0]
        #     No.set_proximo(aux)
    
    # def AddMeio(self, No, posicaoAnterior, posicaoPosterior):
    #     p = self._lista[0]
    #     q = self._lista[0]
    #     for i in range(len(self._lista)):
    #         for j in range(len(self._lista)):
    #             if i == posicaoAnterior and j == posicaoPosterior:
    #                 No.set_proximo(j)


# cabeca = No(1)


# no1 = No(1)
# no1.set_proximo(No(2))
# print(no1)
# no1.get_proximo().set_proximo(No(4))
# print(no1.get_proximo())
# no1.get_proximo().get_proximo().set_proximo(No(5))
# print(no1.get_proximo())
# print(no1.get_proximo().get_proximo())
# n4 = no1.get_proximo().get_proximo()
# no1.get_proximo().set_proximo(No(3))
# no1.get_proximo().get_proximo().set_proximo(n4)
# print(no1)

# nos = No(0)
# for i in range(5):
#     nos.set_proximo(No(i+1))
#     nos = nos.get_proximo()
# print(nos)
