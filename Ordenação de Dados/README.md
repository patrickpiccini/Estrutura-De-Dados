### Usando a estrutura de dados: DICIONÁRIO

Aplicativo Tabela Periódica

Definição: A tabela periódica é uma disposição sistemática dos elementos químicos ordenados
por seus números atômicos, configuração eletrônica, e recorrência das propriedades periódicas.
Base de Dados / Site de Apoio: https://ptable.com/

### DESCRIÇÃO

Crie uma aplicação em modo-texto usando Python que permita apresentar
informações sobre elementos da tabela periódica.
A aplicação deve conter, pelo menos, 10 elementos da tabela periódica, mas não é
necessário incluir todos os elementos, pois a tabela é enorme.

● Carregar os dados a partir de um arquivo CSV que deve ter todas as informações
listadas a seguir.
    1) Referência: http://aprenda-python.blogspot.com.br/2008/10/exemplo-3-ler-
    arquivo-csv-e-mostrar.html

    2) Exemplo CSV (para evitar problemas, não use acentos):
    simbolo;nome;atomico;linha;coluna;estado
    Hg;Mercurio;80;6;12;l

● Cada elemento deverá incluir as seguintes informações
    1) Símbolo (exemplo: Hg)
    2) Nome (exemplo: Mercúrio)
    3) Número Atômico (exemplo: 80)
    4) Linha (exemplo: 6)
    5) Coluna (exemplo: 12)
    6) Estado da Matéria: Líquido
        ▪ Criar um sub-dicionário que faça o seguinte mapeamento:
            ● s sólido
            ● l líquido
            ● g gasoso
            ● d desconhecido
● Criar um menu para o aplicativo que permita:
    1) Listar todos os elementos, porém mostrando apenas uma determinada
    propriedade
        ▪ Exemplo: Listar apenas o nome de todos os elementos cadastrados
    
    2) Listar todos os dados de determinado elemento, buscando através do seu
    símbolo [usar a busca por chave dos dicionários].
    
    3) Listar todos os dados de todos os elementos inseridos.