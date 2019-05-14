class Motor:
   #Construtor
  def __init__(self, motorizacao, combustivel='flex'):
    self._motorizacao = motorizacao
    self._combustivel = combustivel
  
  #Métodos Acessarores
  
  def get_motorizacao(self):
    return self._motorizacao
  def get_combustivel(self):
    return self._combustivel
  
  #Métodos alteradores
  def set_motorizacao(self,nova_motorizacao):
    self._motorizacao = nova_motorizacao
  
  def set_combustivel(self, novo_combustivel):
    self._combustivel = novo_combustivel
  
  #Método que retorna uma representação do objeto, em string.
  def __str__(self):
    return "Motor:{}L, Combustivel:{}".format(self._motorizacao, self._combustivel)
    
    