# Lista Duplamente Encadeada com uso de Sentinelas

class Dnodo:
    def __init__(self, dado = None):
        self.dado = dado
        self.anterior = None
        self.proximo = None

    def __str__(self):
        return str(self.dado)

class LDE:
    def __init__(self):
        self.header = Dnodo()   # <<< Sentinela Cabeça
        self.trailer = Dnodo()  # <<< Sentinela Cauda
        self.tam = 0            # qtde de itens na lista

    def is_empty(self):
        if self.header.proximo is None and self.trailer.anterior is None:
            return True
        return False

    def __inserir(self, novo):
        self.header.proximo = novo    # header -> novo
        novo.anterior = self.header   # header <- novo
        novo.proximo = self.trailer   # novo -> trailer
        self.trailer.anterior = novo  # novo <- trailer
      
    def inserirInicio(self, novo):
        self.tam += 1
        if self.is_empty():
            self.__inserir(novo)
        else:
           antigo_primeiro = self.header.proximo ## item que deixara de ser o primeiro

           novo.anterior = self.header     ##  HEADER <- NOVO
           novo.proximo = antigo_primeiro  ##  NOVO -> AntigoPrimeiro
           antigo_primeiro.anterior = novo ##  NOVO <- AntigoPrimeiro
           self.header.proximo = novo      ##  HEADER -> NOVO
           
    def inserirFim(self, novo):
        self.tam += 1
        if self.is_empty():
            self.__inserir(novo)
        else:
            antigo_ultimo = self.trailer.anterior
            novo.proximo = self.trailer
            novo.anterior = antigo_ultimo
            antigo_ultimo.proximo = novo
            self.trailer.anterior = novo
    
    def removerInicio(self): # esse metodo retorna o nodo para o usuario
        if self.is_empty():
            print('Lista Vazia!')
            return
        else:
            # lista possui + de 1 item            
            removido = self.header.proximo
            novo_head = removido.proximo
            self.header.proximo = novo_head
            novo_head.anterior = self.header
            removido.proximo = None
            removido.anterior = None
            
        self.tam -= 1            
        return removido
        
    def removerFim(self):
        if self.is_empty():
            print('Lista Vazia!')
            return
        
        else:
            # refazer os apontamentos
            pass

        self.tam -= 1
        return removido

    def imprimir(self, reverso=False):
        if self.is_empty():
            print('Lista Vazia')
            return

        if not reverso:
            item = self.header.proximo # devolve o 1o da lista
            while (item.proximo is not None):
                print(item)
                item = item.proximo
        else:
            item = self.trailer.anterior # devolve o ultimo da lista
            while (item.anterior is not None):
                print(item)
                item = item.anterior
    
    def buscar(self, alvo): # retorna a 1a ocorrencia
        if alvo.dado == self.header.proximo.dado:
            return self.header.proximo
        
        if alvo.dado == self.trailer.anterior.dado:
            return self.trailer.anterior

        # laço de busca do 2o elemento até o penultimo
        # faça seu codigo

    def get(self, indice):
        pass

    def removerAntes(self, alvo):
        # header <-> [] <-> [] <-> trailer
        
        nodo_atual = self.buscar(alvo)
        nodo_anterior = nodo_atual.anterior
        
        if (nodo_anterior != self.header):            
            aux = nodo_anterior.anterior
            aux.proximo = nodo_atual
            nodo_atual.anterior = aux
            
            nodo_anterior.anterior = None
            nodo_anterior.proximo = None
            
        self.tam -= 1
        
    def removerApos(self, alvo):
        pass    

    def substituir(self, alvo, valor):
        pass

    def buscarTodos(self, alvo): # retorna uma list com resultados
        lista_todos = []
        ##
        ## sua logica aqui
        ##
        return lista_todos

    def primeiro(self):
        if self.is_empty():
            print('Lista Vazia')
            return
        else:
            return self.header.proximo

    def ultimo(self):
        pass

    def __len__(self):
        return self.tam

## TESTES ##

lista = LDE()
lista.inserirInicio(Dnodo('abc'))
lista.inserirInicio(Dnodo(9999))
lista.inserirInicio(Dnodo('001'))
lista.inserirInicio(Dnodo('xyz'))
lista.inserirFim(Dnodo('www'))
lista.imprimir()
print('Removido o nodo:', lista.removerInicio() )

print()
#lista.removerInicio()
#lista.removerInicio()
#lista.removerInicio()
lista.imprimir()
print(len(lista))