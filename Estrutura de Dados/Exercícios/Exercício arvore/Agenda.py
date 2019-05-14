class No:
    def __init__(self, nome, telefone=None, email=None, esq=None, dire=None, fb=None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.esq = esq
        self.dire = dire
        self.fb = fb


def Insere(arvore, no):
    if arvore is None:
        return no
    elif arvore.nome > no.nome:
        arvore.esq = Insere(arvore.esq, no)
    elif arvore.nome < no.nome:
        arvore.dire = Insere(arvore.dire, no)
    Atribui_fb(arvore)
    return arvore


def Busca(arvore, dado):
    if arvore is None or arvore.nome == dado:
        return arvore
    elif dado < arvore.nome:
        return Busca(arvore.esq, dado)
    elif dado > arvore.nome:
        return Busca(arvore.dire, dado)


def Sucessor(arvore):
    if arvore is None:
        return None
    suce = arvore.dire
    while suce.esq != None:
        suce = suce.esq
    return suce

def Predecessor(arvore):
    if arvore is None:
        return None
    pred = arvore.esq
    while pred.dire != None:
        pred = pred.dire
    return pred

# def Sucessor(arvore):
#   if arvore is None:
#     return None
#   elif arvore.dire != None:
#     ladir = arvore.dire
#   return InOrderEsp(ladir)

# def InOrderEsp(arvore):
#   if arvore.esq is None:
#     return arvore
#   else:
#     aux = InOrderEsp(arvore.esq)
#   return aux

def PreOrder(arvore):
    if arvore is not None:
        print("{}".format(arvore.nome))
        PreOrder(arvore.esq)
        PreOrder(arvore.dire)

def InOrder(arvore):
    if arvore is not None:
        InOrder(arvore.esq)
        print("{}".format(arvore.nome))
        InOrder(arvore.dire)

def PosOrder(arvore):
    if arvore is not None:
        PosOrder(arvore.esq)
        PosOrder(arvore.dire)
        print("{}".format(arvore.nome))

def Remove(arvore, dado):
    if arvore is None:
        return None
    elif arvore.nome == dado:
        if arvore.esq and arvore.dire is None:
            return None
        elif arvore.esq is None:
            return arvore.dire
        elif arvore.dire is None:
            return arvore.esq
        else:
            suce = Sucessor(arvore)
            nome = arvore.nome
            telefone = arvore.telefone
            email = arvore.email
            aux = None
            aux = Insere(aux, No(nome, telefone,email))
            arvore.nome = suce.nome
            arvore.telefone = suce.telefone
            arvore.email = suce.email
            suce.nome = aux.nome
            suce.telefone = aux.telefone
            suce.email = aux.email
            arvore.dire = Remove(arvore.dire, suce.nome)
    elif arvore.nome > dado:
        arvore.esq = Remove(arvore.esq, dado)
    elif arvore.nome < dado:
        arvore.dire = Remove(arvore.dire, dado)
    Atribui_fb(arvore)
    return arvore

def Profundidade(arvore):
    prof_esq = 0
    if arvore.esq != None:
        prof_esq = Profundidade(arvore.esq)
    prof_dire = 0
    if arvore.dire != None:
        prof_dire = Profundidade(arvore.dire)
    return 1 + max(prof_esq, prof_dire)

def Calcula_fb(arvore):
    if arvore.esq != None:
        prof_esq = Profundidade(arvore.esq)
    else:
        prof_esq = 0
    if arvore.dire != None:
        prof_dire = Profundidade(arvore.dire)
    else:
        prof_dire = 0
    return prof_esq - prof_dire

def Atribui_fb(arvore):
    if arvore is not None:
        Atribui_fb(arvore.esq)
        Atribui_fb(arvore.dire)
        arvore.fb = Calcula_fb(arvore)

def BuscaDesbalanceados(arvore, aux=[]):
    if arvore is not None:
        BuscaDesbalanceados(arvore.esq)
        BuscaDesbalanceados(arvore.dire)
        if abs(arvore.fb) > 1:
            print(arvore.nome)
            aux.append(arvore.nome)
    return aux

def BuscaDesbalanceado(arvore):
    aux = BuscaDesbalanceados(arvore)
    if aux != None:
        desbalanceado = aux[0]
    return desbalanceado


# def BuscaDesbalanceado(arvore):
#   if arvore.esq is not None:
#     BuscaDesbalanceado(arvore.esq)
#     if abs(Calcula_fb(arvore.esq)) > 1:
#       return arvore.esq
#     else:
#       arvore.fb = Calcula_fb(arvore)
#       if abs(Calcula_fb(arvore)) > 1:
#         return arvore
#
#       if arvore.dire is not None:
#         BuscaDesbalanceado(arvore.dire)
#   else:
#       arvore.fb = Calcula_fb(arvore)
#       if abs(Calcula_fb(arvore)) > 1:
#         return
#       if arvore.dire is not None:
#         BuscaDesbalanceado(arvore.dire)
#   return True


