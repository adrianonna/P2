class Pilha:
  def __init__(self, itens = []):
    self._itens = itens
  
  def isEmpty(self):
    return self._itens == []
  
  def push(self, item):
    self._itens.append(item)
  
  def pop(self):
    return self._itens.pop()
  
  def topo(self):
    return print(self._itens[len(self._itens)-1])
  
  def size(self):
    return len(self._itens)
  
  def __str__(self):
    return str(self._itens)

p = Pilha()
p.push(3)
print(p)
p.push(4)
print(p)
p.push(5)
print(p)
p.pop()
print(p)
p.pop()
print(p)