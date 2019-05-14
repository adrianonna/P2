class NoTree:
  def __init__(self, chave, esq = None, dire = None):
    self.chave = chave
    self.esq = esq
    self.dire = dire

def insere(arvore, no):
  if (arvore is None):
    return no
  elif(arvore.chave>no.chave):
    arvore.esq = insere(arvore.esq,no)
  elif(arvore.chave<no.chave):
    arvore.dire = insere(arvore.dire,no)
  return arvore

def inOrdem(arvore):
  if(arvore is not None):
    inOrdem(arvore.esq)
    print("{}".format(arvore.chave))
    inOrdem(arvore.dire)

raiz = None
for i in range(5):
  chave = int (input('Valor:'))
  raiz = insere(raiz, NoTree(chave))

inOrdem(raiz)
