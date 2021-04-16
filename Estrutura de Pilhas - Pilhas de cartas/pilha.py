# Implementacao Pilha baseada na List do Python
class Pilha:
    def __init__(self):
        self._vet = [] # lista interna

    def peek(self): # retorna qual item esta no topo
        return self._vet[-1]
       
    def push(self, item): # metodo de inserir item
        self._vet.append(item)
        
    def pop(self): # remover o topo e retornar item para usuario
        # tratar caso de underflow
        if not self.is_empty():
            return self._vet.pop()
            
    def is_empty(self): # teste se é vazia
        return True if len(self._vet) < 0 else False
        
    def __len__(self): # retorna o total de itens
        return len(self._vet)

    def __str__(self): # representacao da pilha como string
        return str(self._vet)

## Desafio ##
##TESTE USANDO OS METODOS ACIMA##
if __name__ == "__main__":

    p1 = Pilha()
    p1.push("♥A")
    print("Primeira carta da pilha 1: ", p1.peek())

    p2 = Pilha()
    p2.push("♦A")
    print("Primeira carta da pilha 2: ", p2.peek())

    p3 = Pilha()
    p3.push("♣A")
    print("Primeira carta da pilha 3: ", p3.peek())

    p4 = Pilha()
    p4.push("♠A")
    print("Primeira carta da pilha 4: ", p4.peek())

    p5 = Pilha()
    p5.push("♥2")
    print("Primeira carta da pilha 5: ", p5.peek())

    p6 = Pilha()
    p6.push("♦2")
    print("Primeira carta da pilha 6: ", p6.peek())

    p7 = Pilha()
    p7.push("♣2")
    print("Primeira carta da pilha 7: ", p7.peek())

    p8 = Pilha()
    p8.push("♠2")
    print("Primeira carta da pilha 8: ", p8.peek())

