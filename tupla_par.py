def tupla_par(tupla):
    nova_tupla = []
    num = 0
    for y in tupla:
        if num%2 == 0:
            nova_tupla.append(y)
        num = num +1
    return nova_tupla
