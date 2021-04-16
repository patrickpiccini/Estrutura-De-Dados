class Fila:    
    def __init__(self):
        self._vet = []
    
    def enqueue(self, item): # enfileirar
        self._vet.append(item)
    
    def dequeue(self): # desenfileirar
        if not self.is_empty():
            return self._vet.pop(0)

    def front(self): # mostrar o 1o da fila, sem remover!
        return self._vet[0]
                
    def is_empty(self): # retorna se a fila esta vazia
        if len(self._vet) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self): # representacao da fila como string
        return str(self._vet)

#-------------------------------------------- MAIN ------------------------------------------------#
import os
if __name__ == "__main__":
    # Criando uma Fila
    f = Fila()
 
    cont = 0
    novalista = []

    while True:
        
        print("\n 1 | Obter nova senha")
        print(" 2 | Proxima Senha") 
        print(" 3 | Mostrar todas as senhas") 
        print(" 0 | Sair! ") 
        opcao = int(input(" Escolha umas nas opções: "))

        if opcao == 1:
            len(f) == cont
            cont += 1
            f.enqueue(cont)
            print(f"\nNova senha numero {cont} gerada!")
            continue
                         
        elif opcao == 2:
            #f.front()
            print("\nChamar proxima senha numero:",f.front())
            novalista += str(f.dequeue())
            continue

        elif opcao == 3:
            print("\nSenhas já chamadas: ", novalista)
            continue

        elif opcao == 0 :
            break

        else:
            print("\nOpção invalida!")
            continue

        

     