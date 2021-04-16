from Main import LSE, Nodo

class PilhaEncadeada:
    def __init__(self):
        self. pilha = LSE()

    def peek(self): # retorna qual item esta no topo
        return self.pilha.tail
       
    def push(self, item): # metodo de inserir item
        self.pilha.inserirFim(Nodo(item))
        
    def pop(self): # remover o topo e retornar item para usuario --- # tratar caso de underflow
        if not self.is_empty():
            return self.pilha.removerFim()
        else:
            return "Pilha Vazia"
    def is_empty(self): # teste se é vazia
        if len(self.pilha) == None:
            return True
        return False
        
    def len(self): # retorna o total de itens
        return len(self.pilha.tam)

    def imprimir(self): # representacao da pilha como string
        return self.pilha.imprimirPilhaEncadeada()



pilha = PilhaEncadeada()

pilha.push("AAAAA")
pilha.push("BBBBB")
pilha.push("CCCCC")
pilha.push("DDDDD")
pilha.push("EEEEE")
pilha.push("FFFFF")


print(pilha.imprimir())