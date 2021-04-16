class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __str__(self):
        return str(self.dado)

# ##############################
# Lista Simplesmente Encadeada
# [NODO] => [NODO] => None
class LSE:
    def __init__(self):
        self.head = None # cabeca | inicio
        self.tail = None # cauda  | fim
        self.tam = 0     # quantidade de elementos

    def is_empty(self): # retorna se a lista esta vazia
            if self.head is None and self.tail is None:
                return True
            return False
        
    def inserirFim(self, novo): # similar ao append da List
        self.tam += 1        
        if self.is_empty():
            # lista vazia
            self.head = novo
            self.tail = novo            
        else:
            self.tail.proximo = novo
            self.tail = novo

    def inserirInicio(self, novo): # similar ao insert(0,item) da List
        self.tam += 1
        if self.is_empty():
            self.head = novo
            self.tail = novo
        else:
            atual = self.head
            novo.proximo = atual
            self.head = novo


        
    def removerInicio(self):
        if self.is_empty():
            print('Lista Vazia!')
            return

        self.tam -= 1 # diminui o contador de itens
        removido = self.head

        ## quando temos apenas 1 item
        if (self.head == self.tail):
            self.head = None
            self.tail = None

        # lista possui + de 1 item               
        else:            
            self.head = self.head.proximo
            removido.proximo = None
            
        return removido
    
    def removerFim(self):
        if self.is_empty():
            print('Lista Vazia!')
            
        ## precisamos descobrir quem eh o penultimo da lista!!
        removido = None
        item = self.head
        while (item != None):
            # quando tem apenas 1 item
            if (item == self.tail and item == self.head):
                self.head = None
                self.tail = None
                self.tam -= 1
                return item

            # quando tem mais de 1
            if (item.proximo != None and item.proximo == self.tail):
                removido = self.tail
                self.tail = item
                item.proximo = None
                self.tam -= 1
                return removido
            
            item = item.proximo
            
    def buscar(self, valor):
        if self.is_empty():
            print('Lista Vazia')
            return

        item = self.head

        while(item != None):
            if str(valor) == str(item):
                return True

            item = item.proximo

    
    def imprimir(self):
        if (self.head is None and self.tail is None):
            print('Lista Vazia')
            return
            
        item = self.head
        while (item != None):
            print(item)
            item = item.proximo

    def imprimirLadoALado(self):
        saida = ''
        item = self.head
        while (item != None):
            if item == self.head:
                saida += '[' + str(item) + ']'
            else:
                saida += ' => ' + '[' + str(item) + ']'
            item = item.proximo
        print(saida)

    def __len__(self):
        return self.tam

## TESTES ##

lista = LSE()
lista.inserirFim( Nodo("ABC") )
lista.inserirFim( Nodo("DEF") )

achou = lista.buscar(Nodo("ABC"))
print(achou)

achou = lista.buscar(Nodo("DEC"))
print(achou)

lista.imprimir()
print(len(lista))

removido = lista.removerInicio()
print("removido elemento", removido)
lista.imprimir()



'''
lista.inserirInicio( Nodo("123") )
lista.removerFim()
lista.imprimirLadoALado()
'''