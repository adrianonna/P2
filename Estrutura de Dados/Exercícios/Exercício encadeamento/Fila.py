class Fila:
  def __init__(self, itens = []):
    self._itens = itens
  
  def isEmpty(self):
    return self._itens == []
  
  def add_inicio(self, item):
    self._itens.insert(0, item)
  def add_fim(self, item):
    self._itens.append(item)
  
  def remove_fim(self):
    return self._itens.pop()
  def remove_inicio(self):
    return self._itens.pop(0)
    
  def inicio(self):
    return print(self._itens[0])

  def final(self):
    tam = len(self._itens)
    return print(self._itens[tam - 1])
#   def topo(self):
#     return print(self._itens[len(self._itens)-1])
  
  def size(self):
    return len(self._itens)
  
  def __str__(self):
    return '{}'.format(self._itens)
#   def __str__(self):
#     return str(self._itens)

p = Fila()
p.add_fim(3)
print(p)
p.add_inicio(4)
print(p)
p.add_fim(5)
print(p)
p.remove_fim()
print(p)
p.remove_inicio()
print(p)
