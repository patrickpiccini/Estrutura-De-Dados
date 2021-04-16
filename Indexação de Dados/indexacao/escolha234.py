import codecs, glob, time, pickle
from escolha2Indexacao import indexar

# Normalização (remover pontuação e deixar tudo em minúsculas) --> Tokenizar 
# --> Remover StopWords --> Stemming 
# --> Inclusão dos termos e documento do índice invertido 

dic = dict()
listA = ["à","â","ã","á"]
listE = ["é","ê","è"]
listI = ["í","ì","î"]
listO = ["ò","ó","õ","ô"]
listU = ["ú","ù","ü"]


#junta todas funções para formatar o texto
def indexaTexto():
    qtnArq = 0
    for arq in glob.glob("docs/*.txt"):
        arquivoString = leEmString(arq)
        stringSemPontuacao = remove_pontuacao(arquivoString)
        listaTokenizada = tokenizacao(stringSemPontuacao)
        listaFinal = remove_repetidas_stopwords(listaTokenizada) 
        indexar(arq, listaFinal, dic)     
        qtnArq += 1
    print("Indexando arquivos...")
    time.sleep(1.5)
    print("Todos os", qtnArq, "arquivos presentes na pasta docs foram indexados")
    write_file(dic)
    time.sleep(1.5)
    print("A indexação foi gravada no arquivo dic.dat")
    return dic
##Normalização
#Abre o arquivo arq_lido e retorna o conteúdo na string arquivoEmString tudo em minúsculo
def leEmString(arq_lido):
    arqAberto = codecs.open(arq_lido,"r","UTF-8")
    arquivoEmString = ''

    for i in arqAberto:
        arquivoEmString += i.lower()
    
    return arquivoEmString


#Remove as pontuações,os números e os caracteres especiais e retorna uma string
def remove_pontuacao(token):
    pontuacoes = '!()[]{};:\'\"\,<>.?@#%^&*_~1234567890\ufeff'
    quebra = '\n\r'
    for char in token:
        if char in pontuacoes:
            token = token.replace(char, "")
        elif char in quebra:
            token = token.replace(char, " ")

    for char in token:
        if char in listA:
            token = token.replace(char, 'a')
        elif char in listE:
            token = token.replace(char, 'e')
        elif char in listI:
            token = token.replace(char, 'i')
        elif char in listO:
            token = token.replace(char, 'o')
        elif char in listU:
            token = token.replace(char, 'u')
    
    return token

#Tokezina (transforma a string doc_inicial em uma lista de palavras separadas e exclui os elementos vazios)
def tokenizacao(doc_inicial):
    doc_inicial = doc_inicial.split(' ')
    while "" in doc_inicial: doc_inicial.remove("")
    return doc_inicial


#Adicionando palavras à lista stopwords
stopwords = []
nome_arq = 'stopwords.txt'

arq = codecs.open(nome_arq, "r", "UTF-8")
linhas = arq.readlines()
for linha in linhas:    
    stopwords.append(linha.replace('\n', '').strip().lower())
arq.close()

#Transforma a lista em um conjunto para remover palavras repetidas e devolve já em lista de novo sem as stopwords
def remove_repetidas_stopwords(doc_repetidas):
    doc_sem_repetidas = list(set(doc_repetidas))

    nova_lista = []

    for token in doc_sem_repetidas:
        if token.lower() not in stopwords:
            nova_lista.append(token)

    return nova_lista


def consultar():
    print("[ 1 ] - Consulta Simples")
    print("[ 2 ] - Consulta com operador AND")
    print("[ 3 ] - Consulta com operador OR")
    print()
    escolha_consulta = int(input("Digite a opção desejada: "))
    print()
    
    if escolha_consulta == 1:   
        while True:
            consulta = input("Digite a palavra a ser pesquisa: ")
            consulta_teste = consulta.split()
            if len(consulta_teste) != 1:
                print()
                print("A pesquisa simples compreende somente UMA palavra!")
                print()
            elif consulta.isdigit():
                print()
                print("A versão básica não indexa por números")
                print()
            else:
                break
        print()  
        try:
            read_file()

            if consulta in dic.keys():
                print("A palavra", consulta.upper(),"foi encontrada nos seguintes documentos: ")
                time.sleep(0.5)
                for v in dic[consulta]:
                    time.sleep(0.5)
                    print(v)
                time.sleep(2)

            else:
                print("A palavra", consulta.upper(), "não foi encontrada nos documentos indexados!")

        except:
            print("Nenhum documento foi indexado!")
            time.sleep(1)
            indexar_agora = input("Deseja indexar os elementos agora? [S/N] ").upper()
            print()
            if indexar_agora == "S":
                indexaTexto()
                time.sleep(2)


    elif escolha_consulta == 2:
        while True:
            consulta = input("Digite as palavras a serem pesquisadas: ")
            consulta_and = consulta.split()
            if len(consulta_and) < 2:
                print()
                print("Você precisa informar 2 palavras")
                print()
            elif len(consulta_and) > 2:
                print()
                print("Você precisa informar SOMENTE 2 palavras")
                print()
            elif consulta_and[0].isdigit() or consulta_and[1].isdigit():
                print()
                print("A versão básica não indexa por números")
                print()
            else:
                break
        print() 
        primeiro = 1
        try:
            read_file()
            
            if consulta_and[0] and consulta_and[1] in dic.keys():
                
                for v in dic[consulta_and[0]]:                
                    for x in dic[consulta_and[1]]:    
                        if v == x:                            
                            if primeiro == 1:
                                print("As palavras",consulta_and[0],"&&", consulta_and[1],"foram encontradas no(s) seguinte(s) arquivo(s):")
                                time.sleep(1)
                                print(v)
                            time.sleep(1)
                            primeiro += 1
                time.sleep(2)

            else:
                print("Nenhum documento possui essas duas palavras")
                time.sleep(2)

        except:
            print("Nenhum documento foi indexado!")
            time.sleep(1)
            indexar_agora = input("Deseja indexar os elementos agora? [S/N] ").upper()
            
            if indexar_agora == "S":
                indexaTexto()
                time.sleep(2)

    elif escolha_consulta == 3:
        while True:
            consulta = input("Digite as palavras a serem pesquisadas: ")
            consulta_or = consulta.split()
            if len(consulta_or) < 2:
                print()
                print("Você precisa informar 2 palavras")
                print()
            elif len(consulta_or) > 2:
                print()
                print("Você precisa informar SOMENTE 2 palavras")
                print()
            elif consulta_or[0].isdigit() or consulta_or[1].isdigit():
                print()
                print("A versão básica não indexa por números")
                print()
            else:
                break

        print()
        segundo = 1
        terceiro = 1
        try:
            read_file()

            if consulta_or[0] and consulta_or[1] in dic.keys():
                print("As palavras",consulta_or[0],"||", consulta_or[1],"foram encontradas no(s) seguinte(s) arquivo(s):")
                print()
                time.sleep(2)
                for v in dic[consulta_or[0]]:                
                    for x in dic[consulta_or[1]]:    
                        if v == x: 
                            if segundo == 1:                           
                                print("Documentos que possuem as DUAS palavras: ")
                                time.sleep(1)
                            segundo += 1
                            print(v)
                            time.sleep(1)      

                for a in dic[consulta_or[0]]:                
                    if a not in dic[consulta_or[1]]:
                        if terceiro == 1:
                            time.sleep(1)
                            print()
                            print("Documentos que só possuem a palavra", consulta_or[0].upper())
                        time.sleep(1)
                        print(v)

                for b in dic[consulta_or[1]]:                
                    if b not in dic[consulta_or[0]]:
                        if terceiro == 1:
                            time.sleep(1)
                            print()
                            print("Documentos que só possuem a palavra", consulta_or[1].upper())
                        time.sleep(1)
                        print(v)  
                        time.sleep(1)     
                
            else:
                print("As palavras", consulta_or[0],"||",consulta_or[1],"não foram encontradas nos documentos indexados!")

        except:
            print("Nenhum documento foi indexado!")
            time.sleep(1)
            indexar_agora = input("Deseja indexar os elementos agora? [S/N] ").upper()
            print()
            if indexar_agora == "S":
                indexaTexto()
                time.sleep(2)
        
    else:
        print("Escolha inválida")
    
   
def invertido():
    read_file()
    print(dic)
    time.sleep(2)

def write_file(dic):         
    dicDB = open("dic.dat","wb")
    pickle.dump( dic, dicDB)
    dicDB.close()


def read_file():
    global dic
    dicDB = open("dic.dat","rb")
    dic = pickle.load(dicDB)
    dicDB.close()
    return dic