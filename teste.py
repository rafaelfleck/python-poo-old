import requests
def cria_lista_links(content):
    links = []
    for line in content.split('</p>'):
        index = line.find('class="title ')
        if index != -1:
            href_start = line.find('href="', index) + 6
            href_end = line.find('"', href_start)
            links.append(line[href_start:href_end])
    return links
 
r = requests.get("http://www.reddit.com/r/programming")
print ( r.content)
