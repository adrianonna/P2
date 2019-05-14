Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def busca_bin(lista, valor):
  inicio = 0
  final = len(lista)-1
  while inicio <= final:
    meio = (inicio+final)//2
    if lista[meio] == valor:
      return meio
    elif lista[meio] < valor:
      inicio = meio+1
    else:
      final = meio-1
  return -1

valor = int(input('Digite o valor procurado: '))
lista = [1,2,4,5,7,8,9]
print(busca_bin(lista, valor))
