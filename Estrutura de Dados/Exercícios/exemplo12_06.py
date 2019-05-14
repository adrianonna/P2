#busca com parada até o valor informado, independente do tamanho da lista
def busca_sequencial(lista, valor):
  for i in range(len(lista)):
    if lista[i] > valor:
      return -1
    elif lista[i] == valor:
        return i
  return -1

lista2 = [1,3,4,7,8,9,15,21,30,54]
valor = int(input('Digite o valor procurado: '))
print(busca_sequencial(lista2, valor))