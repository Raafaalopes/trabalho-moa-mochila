def mochila(nome_do_arquivo):
    # Abrir o arquivo
    with open(nome_do_arquivo, 'r') as file:
        linhas = file.readlines()

    # Processar cada linha
    pesos = []
    utilidades = []
    n = None

    # Separando em listas cada parte do arquivo texto
    # n é apenas um inteiro entao nao precisa de lista
    for linha in linhas:
        if linha.startswith('peso:'):
            pesos = list(map(int, linha.split()[1:]))
        elif linha.startswith('utilidade:'):
            utilidades = list(map(int, linha.split()[1:]))
        elif linha.startswith('n ='):
            n = int(linha.split('=')[1])


    # Lista para armazenar as divisões
    medias = [peso / utilidade for peso, utilidade in zip(pesos, utilidades)]

    # Exibindo a lista de divisões
    print("Médias de peso por utilidade:", medias)

    # Lista para armazenar os elementos selecionados
    mochila = []

    # Ordenar os elementos com base nas divisões em ordem decrescente
    # key=lambda x: x[2] serve para ordenar os elementos com base nas medias(terceiro elemento da tupla)    
    # reverse= true para ser feito em ordem decrescente
    elementos_ordenados = sorted(zip(pesos, utilidades, medias), key=lambda x: x[2], reverse=True)
    # Selecionar os elementos para a mochila
    # Seleciona aqueles com maior valor de média
    # Segue colocando na lista mochila enquanto o soma_pesos + peso seja
    # Quando chegar a ser maior para de colocar na lista
    soma_pesos = 0
    for peso, utilidade, media in elementos_ordenados:
        if soma_pesos + peso <= n:
            mochila.append((peso, utilidade, media))
            soma_pesos += peso


    # Verificar se todas as informações foram lidas corretamente
    if pesos and utilidades and n is not None:
        print("\nPesos:", pesos)
        print("\nUtilidades:", utilidades)
        print("\nn:", n)
    else:
        print("Erro: Alguma informação está faltando no arquivo.")

    # Exibir a lista de elementos na mochila
    print("\nElementos na mochila (peso, utilidade, média):", mochila)
    
print("Selecione o arquivo a ser lido:")
mochila(input())