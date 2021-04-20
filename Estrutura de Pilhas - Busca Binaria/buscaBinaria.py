def buscaBinaria(vetor, alvo):
    _min = 0
    _max = len(vetor)-1
    
    while _min <= _max:
        _mid = (_max + _min)//2

        if vetor[_mid] == alvo:
            return _mid

        if alvo < vetor[_mid]:
            _max = _mid - 1

        if alvo > vetor[_mid]:
            _min = _mid + 1
                
lista = [5, 89, 52, 11, 22]
print(buscaBinaria(lista, 52)) # resultado: 2 [indice]