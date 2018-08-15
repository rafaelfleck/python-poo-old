class A:

	def fazer_algo(self):
		pass

	def outro_metodo(self):
		pass

	def algum_metodo(self, nome):
		print(nome)


class B:

	def __init__(self):
		self.a = A()

	def fazer_algo(self):
		# delega para self.a
		return self.a.fazer_algo()

	def outro_metodo(self):
		# delega para self.a
		return self.a.outro_metodo()

	def __getattr__(self, nome):
		return getattr(self.a, nome)


b = B()
b.fazer_algo() # chama B.fazer_algo() (existe em B)
b.algum_metodo('python') # chama B.__getattr__('algum_metodo') e delega para A.algum_metodo
