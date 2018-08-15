import doctest

class fib:

	def calculo_fib(self, n):
		"""
		Método para cálcular o fibonaci

		>>> fib().calculo_fib(10)
		55
		>>> fib().calculo_fib(1)
		1
		>>> fib().calculo_fib(-1)
        Traceback (most recent call last):
        ...
        ValueError: N tem que ser maior que zero!!!

		"""

		if n < 0:
			raise ValueError("N tem que ser maior que zero!!!")

		a, b = 0, 1
		for i in range(n):
			a, b = b, a + b

		return a

if __name__ == '__main__':
	doctest.testmod(extraglobs={'f':fib()})
