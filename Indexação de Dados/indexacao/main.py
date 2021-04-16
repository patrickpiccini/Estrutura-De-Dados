import glob, os, codecs, sys
from escolha1 import criarArquivoTxt
from escolha234 import indexaTexto, consultar, invertido
from time import sleep



def menu():
    escolha = 0
    while escolha != 5:
        print()
        print("[ 1 ] - Criar novo documento")
        print("[ 2 ] - Indexar documentos '.txt' presentes na pasta docs")
        print("[ 3 ] - Realizar consultas")
        print("[ 4 ] - Mostrar indice invertido")
        print("[ 5 ] - Sair")  
        print()
        escolha = int(input("Digite a opção desejada: "))
        print()
        if escolha == 1:
            criarArquivoTxt()       
        elif escolha == 2:
            indexaTexto()
            sleep(2)
        elif escolha == 3:
            consultar()
        elif escolha == 4:
            invertido()
        elif escolha == 5:
            print("Volte sempre camarada =)")
            break
        else:      
            print("Escolha inválida")
            sleep(1.5)

menu()