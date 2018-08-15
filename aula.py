class Funcionario:
    def __init__(self, nome,salario,cpf):
        self.nome   = nome
        self.salario= salario
        self.cpf    = cpf
        
    def get_bonificacao(self):
        return self.salario * 0.20
    
class Gerente(Funcionario):
    def __init__(self,nome,salario,cpf,senha):
        super().__init__(nome,salario,cpf)
        self.senha = senha
    
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.00

g = Gerente('Rafael',3000.00,'123456789',2333)

print(g.nome)
print(g.get_bonificacao())
print(g.senha)

    
        
