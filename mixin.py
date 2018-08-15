'''
Quando utilizar?

1) Se você desejar reutilizar uma determinada feature em várias classes diferentes.
2) Para melhorar a modularidade.

Mixins é uma forma controlada de adicionar funcionalidades as classes.

Propriedades:
1) não deve ser extendida
2) não deve ser instanciada

Em Python, o conceito de mixins é implementado utilizando herança múltipla.
'''

class Livro(object):
	def __init__(self, nome, conteudo):
		self.nome = nome
		self.conteudo = conteudo

class LivroHTMLMixin(object):
	def renderizar(self):
		return ('<html><title>%s</title><body>%s</body></html>') % (self.nome, self.conteudo)

class LivroHTML(Livro, LivroHTMLMixin):
	pass


livro_html = LivroHTML('Algum Livro', 'blablabla')
print(livro_html.renderizar())
