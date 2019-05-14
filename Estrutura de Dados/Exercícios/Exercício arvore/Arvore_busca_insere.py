class No:
  def __init__(self, chave, esq=None, dire=None, fb=None):
    self.chave = chave
    self.esq = esq
    self.dire = dire
    self.fb = fb

  def __str__(self):
    return '{}'.format(self.chave)

def Insere(arvore, no):
  if arvore is None:
    return no
  elif arvore.chave > no.chave:
    arvore.esq = Insere(arvore.esq, no)
  elif arvore.chave < no.chave:
    arvore.dire = Insere(arvore.dire, no)
  return arvore

def Busca(arvore, dado):
  if arvore is None or arvore.chave == dado:
    return print("{}".format(arvore))
  elif dado < arvore.chave:
    return Busca(arvore.esq, dado)
  elif dado > arvore.chave:
    return Busca(arvore.dire, dado)

def Sucessor(arvore): #menor No da subarvore direita
  if arvore is None:
    return None

def Remove(arvore, dado):
  if arvore is None:
    return None
  elif arvore.dado == dado:
    if arvore.esq and arvore.dire is None: #função EhFolha()
      return None
    elif arvore.esq is None:
      return arvore.dire
    elif arvore.dire is None:
      return arvore.esq
    #else:
      #achar No sucessor da raiz
      #trocar as chaves
      #atualizar o lado da arvore arvore.dire=excluir(arvore.dire, chave do sucessor)
  elif arvore.dado > dado:
    arvore.esq = Remove(arvore.esq, dado)
  elif arvore.dado < dado:
    arvore.dire = Remove(arvore.dire, dado)
  return arvore

def InOrder(arvore):
  if arvore is not None:
    InOrder(arvore.esq)
    print("{}".format(arvore.chave))
    InOrder(arvore.dire)

arvore=None
for i in range(5):
  dado=int(input('Digite a informação: '))
  arvore=Insere(arvore, No(dado))

InOrder(arvore)
print(Busca(arvore, 2))