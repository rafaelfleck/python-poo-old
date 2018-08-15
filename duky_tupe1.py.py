

class Pato:

	def quack(self):
		print('Quack, quack')


class Pessoa:

	def quack(self):
		print('Eu faco quack igual a um pato')


'''
# isso NÃO é pythonico
def fazer_quack(obj):

	if isinstance(obj, Pato):
		obj.quack()
	else:
		print('Isso tem que ser um pato')
'''

'''
def fazer_quack(obj):
	# LBYL - NÃO pythonico
	if hasattr(obj, 'quack'):
		if callable(obj.quack):
			obj.quack()
'''

'''
EAFP - Easier to ask for forgiveness than permission
É pythonico
'''
def fazer_quack(obj):

	try:
		obj.quack()
	except AttributeError as e:
		print(e)


pato = Pato()
fazer_quack(pato)

pessoa = Pessoa()
fazer_quack(pessoa)
