class Ponto:

	def __init__(self, x = 0, y = 0):
		self.x, self.y = x, y

	def resetar(self):
		self.x, self.y = 0, 0

	def mover(self, x, y):
		self.x, self.y = x, y


p = Ponto()
p.resetar()
#Ponto.resetar(p)
print(p.x, p.y)
p.mover(10, 20)
print(p.x, p.y)