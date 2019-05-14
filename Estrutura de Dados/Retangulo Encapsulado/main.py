class Retangulo:
  def __init__(self,lado,altura):
    self.__altura = altura
    self.__lado = lado
  
  def getAltura(self):
    return self.__altura
  
  def getLado(self):
    return self.__lado
  
  def area(self):
    return self.__lado*self.__altura
  
  def perimetro(self):
    return 2*self.__lado+2*self.__altura
  
  def __str__(self):
    return "Lado: {}, Altura: {}, Area: {}, Perimetro: {}".format(
      self.__lado, self.__altura, self.area(),
      self.perimetro())

#Criando o objeto    
ret = Retangulo(2,4)
print("Lado: {}, Altura: {}\n".format(
    ret.getLado(), ret.getAltura()))

print(ret)