
def indexar(arq, listaFinal, dic):
    # doc: list | arq: str (nome do arquivo)
    for palavra in listaFinal:
        if palavra in dic:
            lista_docs = dic[palavra]
            lista_docs.append(arq)
        else:
            dic[palavra] = [arq]
