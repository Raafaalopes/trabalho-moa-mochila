import numpy as np


def calculate(cities):
    cidades_percorridas = []
    distancias_percorridas = []
    quantidade_de_cidades = len(cities)
    
    print("Escolha a cidade inicial (de 1 até {maximo})".format(maximo = quantidade_de_cidades))
    cidade_inicial = int(input()) - 1
    cidade_escolhida = cidade_inicial

    quantidade_de_cidades_percorridas = 1
    while quantidade_de_cidades_percorridas < quantidade_de_cidades + 1:
        cidade = cities[cidade_escolhida]     
        cidades_percorridas.append(cidade.id)

        indices_excluidos = []
        indices_excluidos.append(cidade.id)
        for cidade_percorrida in cidades_percorridas:
            indices_excluidos.append(cidade_percorrida)

        resultado = [item for i, item in enumerate(cidade.distancias) if i not in indices_excluidos]

        if len(resultado) == 0:
            break
        
        distancia_da_cidade = min(resultado)
        distancias_percorridas.append(distancia_da_cidade)
        
        distancias = np.array(cidade.distancias)
        ocorrencias = np.where(distancias == distancia_da_cidade)[0]
        
        ids_nao_usados = np.setdiff1d(ocorrencias, np.array(indices_excluidos))

        formatado = []
        for id in ids_nao_usados:
            formatado.append(id)
                    
        proxima_cidade = formatado[0]
        cidade_escolhida = proxima_cidade

        quantidade_de_cidades_percorridas = quantidade_de_cidades_percorridas + 1

    cidades_percorridas.append(cidade_inicial)
    cidade = cities[cidade_escolhida]
    distancia = cidade.distancias[cidade_inicial]
    distancias_percorridas.append(distancia)

    texto_cidades = ''          
    contador = 0
    print("Caminho perocrrido:")
    for cidade_percorrida in cidades_percorridas:
        if contador == quantidade_de_cidades:
            texto_cidades = texto_cidades + '{}'.format(cidade_percorrida + 1)    
        else:
            texto_cidades = texto_cidades + '{} -> '.format(cidade_percorrida + 1)
            contador = contador + 1

    print(texto_cidades)
    
    texto_distancias = "0 -> "
    contador = 0
    distancia_total = 0
    print("Distância total:")
    for distancia_percorrida in distancias_percorridas:
        if contador == len(distancias_percorridas) - 1:
            texto_distancias = texto_distancias + '{}'.format(distancia_total + distancia_percorrida)    
        else:
            texto_distancias = texto_distancias + '{} -> '.format(distancia_total + distancia_percorrida)
            contador = contador + 1
            distancia_total = distancia_total + distancia_percorrida

    print(texto_distancias)