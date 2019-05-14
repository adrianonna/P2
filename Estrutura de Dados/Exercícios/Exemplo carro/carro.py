class Carro:
  #Construtor
  def __init__(self, cor, placa, motor, dimensao):
    self._cor = cor #string
    self._placa = placa #string
    self._motor = motor #instancia de Motor
    self._dimensao = dimensao #instancia de Dimensao
  
  #Metodos acessadores
  
  def get_cor(self):
    return self._cor
  def get_placa(self):
    return self._placa
  def get_motor(self):
    return self._motor
  def get_dimensao(self):
    return self._dimensao
  
  #Método alterador
  def set_placa(self, nova_placa):
    self._placa =nova_placa
  
  #Método mágico que retorna o objeto representado numa string
  def __str__(self):
    return 'Cor:{}, Placa: {}, \nMotorização: {}, \nDimensão: {}'.format(
      self._cor,self._placa, self._motor, self._dimensao)
      