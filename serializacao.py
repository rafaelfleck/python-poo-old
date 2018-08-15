import pickle
import json
'''
meus_dados = ['Rafael',3.12,[1,2,3]]

with open('teste.txt','wb') as file:
    pickle.dump(meus_dados,file)

with open('teste.txt','rb') as file:
    dados_carregados = pickle.load(file)

assert meus_dados == dados_carregados
print(dados_carregados)
'''

class Contato:
    def __init__(self,primeiro_nome,sobre_nome):
        self.primeiro_nome = primeiro_nome
        self.sobre_nome = sobre_nome

    @property
    def nome_completo(self):
        return ('{} {}'.format(self.primeiro_nome,self.sobre_nome))

c = Contato('Rafael','Fleck')
print(json.dumps(c.__dict__))

    
