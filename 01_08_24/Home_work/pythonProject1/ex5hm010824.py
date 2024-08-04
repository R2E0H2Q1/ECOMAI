# 5 Sort by key:
# "Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai":

cities_lst = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(f"The original list is: {cities_lst}")

# Next on the list, Use sort and lambda to sort by:
# a. The length of the city name

citieslencheck = sorted(cities_lst, key=lambda x: len(x)) #checks the length of each city name
for city in citieslencheck:
    print(f"The lenght of {city}, the length is: {len(city)}")

# b. The last letter of the city name

lastlet = sorted(cities_lst, key=lambda x: x[-1])
for city in lastlet:
    print(f"The last letter of {city} is: {city[-1]}")

# c. The name of the city is in reverse alphabetical order

reverse = sorted(cities_lst, key=lambda x: x[::-1])
for city in reverse:
    print(f"{city} in reverse is: {city[::-1]}")