from motor import Motor
from dimensao import Dimensao
from carro import Carro

#Criando um motor 1.6L a gasolina
motor = Motor('1.6','gasolina')

#Criando um objeto dimensão
dimensao = Dimensao(1.67,1.81,4.37)

#Criando um Carro, relacionando-o com os objetos motor e dimensao
carro = Carro('preto','XXX1234',motor,dimensao)
#Imprimindo o carro
print(carro)

#Alterando o motor do carro
carro.get_motor().set_motorizacao('2.0')

#Alterando a altura do carro
carro.get_dimensao().set_altura(1.65)

#Imprimindo novamento o carro
print(carro)


