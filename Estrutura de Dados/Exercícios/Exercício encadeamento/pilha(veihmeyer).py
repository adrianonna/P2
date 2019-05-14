class No_Pilhas:
  
  def __init__ (self, dados = None, NoAnterior = None):
    self.dados = dados
    self.anterior = NoAnterior
    
  def GetDados(self):
    return self.dados
  def SetDados(self, NovoDado):
    self.dados = NovoDado
  
  def Get_No_Anterior(self):
    return self.anterior
  def Set_No_Anterior(self, NovoAnterior):
    self.anterior = NovoAnterior
    
  def __repr__(self):
    return '%s -> %s' % (self.anterior, self.dados)
        
class Pilha:
  def __init__ (self):
    self.topo = None
  
  def GetTopo(self):
    return self.topo
  def SetTopo(self, NewTopo):
    self.topo = NewTopo
    
  def inserir(self, NewDate):
    NovoNo = No_Pilhas(NewDate)
    NovoNo.anterior = self.topo
    self.topo = NovoNo
    
  def remover(self):
    if(self.topo == None):
      print('Impossível remover elementos de uma pilha vazia')
    self.topo = self.topo.anterior
  
  def __str__(self):
   return "[" + str(self.topo) + "]" 
   
  def RemoverAnyElements(self):
    while self.topo != None:
      p.remover()
      
    print('Pilha completamente vazia')
    
   

# p = Pilha()
# print('A pilha de elementos está vazia ', p)
  
# p.inserir(10)
# p.inserir(20)
# p.inserir(30)
# p.inserir('veihmeyer')
# p.inserir('Adriano')
# p.inserir('Jovys')
# print(p)
# p.remover()
# print(p)
# p.RemoverAnyElements()

p = Pilha()
print('A pilha de elementos está vazia ', p)
opcao = 1
while opcao != 4:
    print('\n')
    print('1 para adicionar\n2 para remover\n3 para remover tudo da pilha\n4 para sair do loop')
    opcao = int(input('Digite sua opção: '))
    while opcao < 1 and opcao > 4:
        opcao = int(input('Opção inválida, digite entre 1 e 4.'))
    if opcao == 1:
        valor = input('Digite o que deseja adicionar na pilha: ')
        p.inserir(valor)
    elif opcao == 2:
        p.remover()
    elif opcao == 3:
        p.RemoverAnyElements()
    print('Pilha: ', p)