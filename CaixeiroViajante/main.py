import numpy as np

# Function that does all the calculation
def mochileiro(cities):    
    past_cities = []
    past_distances = []
    number_of_cities = len(cities)
    
    # Asking for the initial city
    print("Escolha a cidade inicial (de 1 até {})".format(number_of_cities))
    initial_city = int(input()) - 1
    chosen_city = initial_city

    amount_past_cities = 1
    # If all the cities have been visited, the while loop ends 
    while amount_past_cities < number_of_cities + 1:
        city = cities[chosen_city]     
        past_cities.append(city.id)

        # All the cities the guy already visited
        excluded_indexes = []
        excluded_indexes.append(city.id)
        for past_city in past_cities:
            excluded_indexes.append(past_city)

        # All the distances where the cities have not been visited
        result = [item for i, item in enumerate(city.distances) if i not in excluded_indexes]

        # If result is null, it means all the cities have been visited
        if len(result) == 0:
            break
        
        # Gets the nearest city
        city_distance = min(result)
        past_distances.append(city_distance)
        
        # Verification if there is two cities with the same distance
        distances = np.array(city.distances)
        occurrences = np.where(distances == city_distance)[0]
        
        unused_ids = np.setdiff1d(occurrences, np.array(excluded_indexes))

        formatted = []
        for unused_id in unused_ids:
            formatted.append(unused_id)
                    
        # We get the first nearest city 
        next_city = formatted[0]
        chosen_city = next_city

        amount_past_cities = amount_past_cities + 1

    # After going out the loop, we add the return to the initial city and get the distance
    past_cities.append(initial_city)
    city = cities[chosen_city]
    distancia = city.distances[initial_city]
    past_distances.append(distancia)

    # Just a printer that shows all the road that we past 
    city_text = ''          
    counter = 0
    print("Caminho percorrido:")
    for past_city in past_cities:
        if counter == number_of_cities:
            city_text = city_text + '{}'.format(past_city + 1)    
        else:
            city_text = city_text + '{} -> '.format(past_city + 1)
            counter = counter + 1

    print(city_text)
    
    # And here a printer that shows the total distance
    distances_text = "0 -> "
    counter = 0
    total_distance = 0
    print("\nDistância total:")
    for past_distance in past_distances:
        if counter == len(past_distances) - 1:
            distances_text = distances_text + '{}'.format(total_distance + past_distance)    
            total_distance = total_distance + past_distance
        else:
            distances_text = distances_text + '{} -> '.format(total_distance + past_distance)
            counter = counter + 1
            total_distance = total_distance + past_distance

    print(distances_text)
    print("Distância total: %d" % total_distance)