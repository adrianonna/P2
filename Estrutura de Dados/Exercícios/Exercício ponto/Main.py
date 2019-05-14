from Ponto import Ponto

#Criando um objeto da classe Ponto
x = float(input('Informe o valor da coordenada X, para o ponto P1:'))
y = float(input('Informe o valor da coordenada Y, para o ponto P1:'))
p1 = Ponto(x,y)

#Criando outro objeto da classe Ponto
x = float(input('Informe o valor da coordenada X, para o ponto P2:'))
y = float(input('Informe o valor da coordenada Y, para o ponto P2:'))
p2 = Ponto(x,y)

#Imprimindo os valores dos atributos do objeto p1
print ("P1({0},{1})\n".format(p1.x,p1.y))

#Imprimindo os valores dos atributos do objeto p2
print ("P2({0},{1})\n".format(p2.x,p2.y))

#Exibindo a distancia entre P1 e P2
print ("Distancia entre P1 e P2 é = {0}\n".format(p1.distanciaEntre(p2)))

#Movendo P1 para uma nova coordenada
#Criando um objeto da classe Ponto
x = float(input('Informe o novo valor da coordenada X, para o ponto P1:'))
y = float(input('Informe o novo valor da coordenada Y, para o ponto P1:'))
p1.moverPara(x,y)

#Exibindo a nova coordenada de P1
print ("Nova coordenada P1({0},{1})\n".format(p1.x,p1.y))

#Criando 10 pontos

#Lista que armazenará os pontos:
pontos = list()

#Criando 10 pontos
for i in range(10):
    x = float(input('Informe o novo valor da coordenada X, para P{0}:'.format(i+1)))
    y = float(input('Informe o novo valor da coordenada Y, para P{0}:'.format(i+1)))
    #Criando o ponto e adicionando a lista pontos
    pontos.append(Ponto(x,y))

#Listando os pontos

print('Listagem dos Pontos:\n\n')
for i in range(len(pontos)):
    print ("P{0}({1},{2})\n".format(i+1,pontos[i].x,pontos[i].y))
