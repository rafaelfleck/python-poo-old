'''
Se um objeto anda como um pato e faz quack como um pato então ele é um pato.

Programe para interfaces e não para uma implementação.
'''

class Pato:
	def quack(self):
		print('quack, quack!')


class Pessoa:
	def quack(self):
		print('QUACK!')


def na_floresta(obj):
	obj.quack()


na_floresta(Pato())
na_floresta(Pessoa())


'''
class Livro():

	def __init__(self, titulo, lancamento, autor):
		self.titulo = titulo
		self.lancamento = lancamento
		self.autor = autor


class Filme():

	def __init__(self, titulo, lancamento, diretor):
		self.titulo = titulo
		self.lancamento = lancamento
		self.diretor = diretor


def imprimir(midia):
	print(midia.titulo, midia.lancamento)
'''