import csv

tabela_periodica = {}
estados = {'l': 'Líquido', 'g': 'Gasoso', 's': 'Solido', 'd':'Desconhecido'}

arq = csv.reader(open('tabela.txt'), delimiter=';')
for i,dado_linha in enumerate(arq):
    if i == 0: # pula linha do cabecalho (1a linha do arquivo)
        continue

    dados = {}
    dados['simbolo'] = dado_linha[0] # simbolo
    dados['nome'] = dado_linha[1] # nome    
    dados['valor'] = dado_linha[2]
    dados['linha'] = dado_linha[3]
    dados['coluna']= dado_linha[4]
    dados['estado'] = estados[dado_linha[5]]
    
    # insere os dados na tabela periodica
    tabela_periodica[dados['simbolo'].upper()] = dados


#--------------------------------------------- Escolhas -------------------------------------------------

while True:
    print('[ 1 ] - Listar todos os elementos, porém mostrando apenas uma determinada propriedade')
    print('[ 2 ] - Listar todos os dados de determinado elemento, buscando através do seu símbolo')
    print('[ 3 ] - Listar todos os dados de todos os elementos inseridos')
    print('[ 4 ] - Sair')
    escolha = int(input("Qual opção você deseja?\n"))
  
    if escolha == 1:
        while True:
            print('[ 1 ] - Nome')
            print('[ 2 ] - Símbolo')
            print('[ 3 ] - Valor')
            print('[ 4 ] - Linha')
            print('[ 5 ] - Coluna')

            propriedade = int(input("Qual propriedade você deseja?\n"))
            if propriedade == 1:
                for i  in tabela_periodica.values():
                    print(i['nome'], end= ", ")
                break

            elif propriedade == 2:
                for j in tabela_periodica.keys():
                    print(j, end = ', ')
                break

            elif propriedade == 3:
                for h in tabela_periodica.values():
                    print(h['valor'], end= ", ")
                break

            elif propriedade == 4:
                for l in tabela_periodica.values():
                    print(l['linha'], end= ", ")
                break

            elif propriedade == 5:
                for k in tabela_periodica.values():
                    print(k['coluna'], end= ", ")
                break

            elif propriedade == 6:
                for m in tabela_periodica.values():
                    print(m['estado'], end= ", ")
                break

            else:
                print("Numero invalido!\n Tente novamente.\n")  
                continue


    elif escolha == 2:
        while True:
            simbolo_escolha = input("Qual elemento deseja visualizar?\n").upper()
            if simbolo_escolha in tabela_periodica:
                elemento_escolha = tabela_periodica[simbolo_escolha]

                print("--------")
                print(elemento_escolha['simbolo'])
                print(elemento_escolha['nome'])
                print(elemento_escolha['valor'])
                print(elemento_escolha['linha'])
                print(elemento_escolha['coluna'])
                print(elemento_escolha['estado'])
                break
            
            else:
                print("ERROU!")
                continue

    elif escolha == 3:
        print("Lista com todos os elementos:\n")
        for x, v in tabela_periodica.items():
            print("Elemento: ",x)
            print("Características:")
            print("Símbolo: ", v['simbolo'])
            print("Nome: ", v['nome'])
            print("Valor Atômico: ", v['valor'])
            print("Linha: ", v['linha'])
            print("Coluna: ", v['coluna'])
            print("Estado: ", v['estado'],"\n")

    elif escolha == 4:
        print("Obrigado, volte sempre! :) ")
        break

    else:
        print("Valor invalido, Tente novamente uma das opcoes!\n")
        continue


