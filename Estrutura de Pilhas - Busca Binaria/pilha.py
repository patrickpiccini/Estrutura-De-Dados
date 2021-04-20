resto = []

def binario(numero):
    while numero > 0:
        binario = numero % 2
        resto.append(binario)
        numero = numero  // 2
        
    divisao = ""
    while len(resto) > 0:
        divisao += str(resto.pop())
        
    return divisao


numero = int(input("Digite um valor: "))
print(binario(numero))


