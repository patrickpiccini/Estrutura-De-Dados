from time import sleep
import os.path
#cria um arquivo
def criarArquivoTxt():
    print()
    titulo = input("Digite o nome da noticia: ")
    titulo = titulo +".txt"
    if os.path.isfile("docs/"+titulo):
        print("Já existe uma notícia com esse título.")
        sleep(1)
    else:
        abrirArquivo = open("docs/"+titulo,"a")
        insercao = input("Digite a noticia: ")
        print()
        abrirArquivo.write(insercao)
        print("Criando arquivo...")
        sleep(2)
        print("Arquivo", titulo,"criado!")
        abrirArquivo.close()
        sleep(2)