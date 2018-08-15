'''
def modificar(funcao):
    def somar_pares(a, b):
        if a % 2 == 0 or b % 2 == 0:
            return a + b
        return a - b
    return somar_pares


@modificar
def soma(a, b):
    return a + b

print(soma(2,3))
    
'''

    
