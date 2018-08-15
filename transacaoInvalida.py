class TransacaoInvalida(Exception):
    def __init__(self, salado_atual,quantidade):
        super().__init__('Sua conta não tem ${}'.format(quantidade))
        self.quantidade = quantidade
        self.salado_atual = salado_atual

    def excesso(self):
        return self.quantidade - self.salado_atual

try:
    raise TransacaoInvalida(10,20)
except TransacaoInvalida as e:
    print('Voce não tem salado suficiente, falta R${}.'.format(e.excesso()))
