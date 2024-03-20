from math import sqrt
from main import calculate

# Classes Localization and City to organize 
class Localization:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

class City:
    def __init__(self, id, distances):
        self.id = id
        self.distances = distances

# Function that reads the file
def read(fileName):
    # File reader
    with open(fileName, 'r') as file:
        lines = file.readlines()

    localizations = []
    cities = []

    # Question it if the file is already a matrix or came with ids + coordinates
    print("O arquivo ja vem formatado como matriz? (s/n)")
    answer = input().lower()
    
    # If not, reads every line and makes the distances one by one
    if(answer == 'n'):
        print("\nFormulando matriz...")
        # Gets all the cities
        for line in lines:
            infos = line.split()
            localization = Localization(int(infos[0])-1, int(infos[1]), int(infos[2]))
            localizations.append(localization)

        # Distance calculator for every city (rounded to make it easier)
        for localization in localizations:
            distances = []
            for near_city_localization in localizations:
                x_diff = abs(localization.x - near_city_localization.x)
                y_diff = abs(localization.y - near_city_localization.y)
                distance = int(abs(round(sqrt(pow(x_diff, 2) + pow(y_diff, 2)), 0)))
                distances.append(distance)

            cities.append(City(localization.id, distances))
        print("Matriz formulada!\n")
    # If yes, reads every line and just make the cities
    else:
        counter = 0
        for line in lines:
            distances = line.split()
            formatted_distances = []
            for distance in distances:
                formatted_distances.append(int(distance))

            cities.append(City(counter, formatted_distances))
            counter = counter + 1       
         
    # Return the array with cities 
    return cities
    
print("Selecione o arquivo a ser lido:")

# Call to function read
cities = read(input())
# Call to function calculate (main.py)
calculate(cities)