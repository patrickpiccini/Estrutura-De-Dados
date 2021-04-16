Objetivo: Converter Decimal para Binário
Requisitos:
- Usar implementação própria de Pilha
- Baseada na List do Python – Vetor Dinâmico

Criar uma função chamada dec2bin que receba como parâmetro um valor inteiro e retorne um string com sua representação binária (0 e 1).

Exemplo de execução:
>> print(dec2bin(25))
>> 11001

DICAS

- Uso da Pilha: https://repl.it/@FahadKalil1/desafiodecbin

- O python possui um método que realiza a divisão de 2 número e devolve uma tupla com o resultado e o resto da divisão.
Exemplo

(resultado, resto) = divmod(25, 2)
print(resultado) # retorna 12
print(resto) # retorna 1