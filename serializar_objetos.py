import json
class Contato:
    def __init__(self,primeiro_nome,sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return ('{} {}'.format(self.primeiro_nome,self.sobrenome))

c = Contato('Rafael','Fleck')
print(json.dumps(c.__dict__))
