def numero_perfeito(num):
    num_perfeito = True
    valida_num   = True
    div = 0
    soma = 0
    while valida_num == True:
        div = div+1
        divisor = num%div
        if divisor ==0:
            soma= soma + div
            if soma == num:
                #print(soma_valor,' é um número perfeito.')
                num_perfeito = True
                valida_num   = False
            elif soma > num:
                #print(num,' não é número perfeito.')
                num_perfeito = False
                valida_num   = False
        
    return num_perfeito
