import numpy as np

def calculate(cities):
    past_cities = []
    past_distances = []
    number_of_cities = len(cities)
    
    print("Escolha a cidade inicial (de 1 até {})".format(number_of_cities))
    initial_city = int(input()) - 1
    chosen_city = initial_city

    amount_past_cities = 1
    while amount_past_cities < number_of_cities + 1:
        city = cities[chosen_city]     
        past_cities.append(city.id)

        excluded_indexes = []
        excluded_indexes.append(city.id)
        for past_city in past_cities:
            excluded_indexes.append(past_city)

        result = [item for i, item in enumerate(city.distances) if i not in excluded_indexes]

        if len(result) == 0:
            break
        
        city_distance = min(result)
        past_distances.append(city_distance)
        
        distances = np.array(city.distances)
        occurrences = np.where(distances == city_distance)[0]
        
        unused_ids = np.setdiff1d(occurrences, np.array(excluded_indexes))

        formatted = []
        for unused_id in unused_ids:
            formatted.append(unused_id)
                    
        next_city = formatted[0]
        chosen_city = next_city

        amount_past_cities = amount_past_cities + 1

    past_cities.append(initial_city)
    city = cities[chosen_city]
    distancia = city.distances[initial_city]
    past_distances.append(distancia)

    city_text = ''          
    counter = 0
    print("Caminho perocrrido:")
    for past_city in past_cities:
        if counter == number_of_cities:
            city_text = city_text + '{}'.format(past_city + 1)    
        else:
            city_text = city_text + '{} -> '.format(past_city + 1)
            counter = counter + 1

    print(city_text)
    
    distances_text = "0 -> "
    counter = 0
    total_distance = 0
    print("Distância total:")
    for past_distance in past_distances:
        if counter == len(past_distances) - 1:
            distances_text = distances_text + '{}'.format(total_distance + past_distance)    
        else:
            distances_text = distances_text + '{} -> '.format(total_distance + past_distance)
            counter = counter + 1
            total_distance = total_distance + past_distance

    print(distances_text)