from math import sqrt


class Localizacao:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

class Cidade:
    def __init__(self, id, distancias):
        self.id = id
        self.distancias = distancias

with open('1002_cidade.txt', 'r') as file:
    linhas = file.readlines()

localizacoes = []
cidades = []

for linha in linhas:
    infos = linha.split()
    localizacao = Localizacao(int(infos[0])-1, int(infos[1]), int(infos[2]))
    localizacoes.append(localizacao)

for localizacao in localizacoes:
    distancias = []
    for localizacao_cidade_vizinha in localizacoes:
        x_diff = abs(localizacao.x - localizacao_cidade_vizinha.x)
        y_diff = abs(localizacao.y - localizacao_cidade_vizinha.y)
        distance = int(abs(round(sqrt(pow(x_diff, 2) + pow(y_diff, 2)), 0)))
        distancias.append(distance)
    
    cidades.append(Cidade(localizacao.id, distancias))