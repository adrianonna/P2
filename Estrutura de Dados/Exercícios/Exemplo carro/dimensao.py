class Dimensao:
  #Construtor
  def __init__(self,altura,largura,comprimento):
    self._altura =altura
    self._largura = largura
    self._comprimento = comprimento
  
  #Métodos Acessadores
  def get_altura(self):
    return self._altura
  def get_largura(self):
    return self._largura
  def get_comprimento(self):
    return self._comprimento
  
  #Métodos Alteradores
  def set_altura(self, nova_altura):
    self._altura =nova_altura
  def set_largura(self,nova_largura):
    self._largura =nova_largura
  def set_comprimento(self, novo_comprimento):
    self._comprimento = novo_comprimento
    
  #Método mágico que retorna o objeto representado numa string
  def __str__(self):
    return "Altura: {}, Largura: {}, Comprimento:{}".format(
      self._altura, self._largura, self._comprimento)
