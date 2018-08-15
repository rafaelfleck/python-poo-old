class Quadrado:

	def __init__(self, lado):
		self.lado = lado

	def perimetro(self):
		return 4 * self.lado

	def area(self):
		return self.lado * self.lado


class Retangulo:

	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	def area(self):
		return self.base * self.altura