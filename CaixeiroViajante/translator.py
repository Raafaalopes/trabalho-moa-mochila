from math import sqrt
from main import calculate

# 
class Localization:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

class City:
    def __init__(self, id, distances):
        self.id = id
        self.distancias = distances

def read(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()

    localizations = []
    cities = []

    print("O arquivo ja vem formatado como matriz? (s/n)")
    answer = input().lower()
    
    if(answer == 'n'):
        for line in lines:
            infos = line.split()
            localization = Localization(int(infos[0])-1, int(infos[1]), int(infos[2]))
            localizations.append(localization)

        for localization in localizations:
            distances = []
            for near_city_localization in localizations:
                x_diff = abs(localization.x - near_city_localization.x)
                y_diff = abs(localization.y - near_city_localization.y)
                distance = int(abs(round(sqrt(pow(x_diff, 2) + pow(y_diff, 2)), 0)))
                distances.append(distance)

            cities.append(City(localization.id, distances))
    else:
        counter = 0
        for line in lines:
            distances = line.split()
            formatted_distances = []
            for distance in distances:
                formatted_distances.append(int(distance))

            cities.append(City(counter, formatted_distances))
            counter = counter + 1       
         
    return cities
    
print("Selecione o arquivo a ser lido:")

cities = read(input())
calculate(cities)