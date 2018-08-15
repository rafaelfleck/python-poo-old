import heapq

class FilaDePrioridade: 

    def __init__(self):
        self.fila = []
        self.indice = 0

    def inserir(self,item,prioridade):
        heapq.heappush(self.fila,(-prioridade,self.indice,item))
        self.indice +=1
        
    def remove(self):
        return heapq.heappop(self.fila)[-1]
        
class Item:
    def __init__(self,nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

    
fila = FilaDePrioridade()
fila.inserir(Item('Rafael'),42)
fila.inserir(Item('Aline'),38)
fila.inserir(Item('Felix'),60)

print(fila.remove())
print(fila.remove())
print(fila.remove())
