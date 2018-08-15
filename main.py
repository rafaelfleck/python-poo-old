#função para retirar os acentos e espaços do nome da cidade
def replace_char(texto,codif="utf-8"):
    if texto is None:
        return None
    dic={"Á":"A","À":"A","Ã":"A","É":"E","Ê":"E",\
         "Í":"I","Ó":"O","Õ":"O","Ô":"O","Ú":"",\
         "Ç":"C","á":"a","à":"a","ã":"a","é":"e",\
         "ê":"e","í":"i","ó":"o","õ":"o","ô":"o",\
         "ú":"","ç":"c"," ":"","-":""}
    replaced=""
    for c in texto:
        replaced+=dic.get(c,c)
    return replaced

import requests

sair = 's'

while sair == 's':
    print("\n\nPREVIÃO DO TEMPO")
    estado = input('Informe a siglas do Estado: ')
    cidade = input('Informe o nome da Cidade: ')

    #utilizando o site tempoagora para buscar a temperatura da cidade informada
    pagina = requests.get("http://www.tempoagora.com.br/previsao-do-tempo/"+estado.lower()+"/"+replace_char(cidade)+"/")
    if pagina.status_code == 200:

        #utilizando modulo BeautifulSoup para fazer o parser das informações do site
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(pagina.content, 'html.parser')
        div_dados = soup.find(id="page")

        lista_tags = div_dados.select(".block-1")
        lista_inf = div_dados.select(".item")


        for pt in lista_tags:
            print("Na Cidade "+pt.find(class_='pull-left').get_text())
            print(pt.find(class_='text-previ-right').get_text()+" "+pt.find_all('p')[0].get_text())
            
        for inf in lista_inf:
            print(inf.select("span")[0].get_text()+" "+inf.select("span")[1].get_text())
    else:
        print("Site fora do ar, pedimos desculpa. \n\n")
    sair = input("Realizar nova pesquisa (S ou N')?")

    
    if sair.lower() == 's':
        continue
    elif sair == 'n':
        break
    else:
        while sair != 's' and sair != 'n':
            sair = input("Informação incorreta. Realizar nova pesquisa (S ou N')?")
            continue
