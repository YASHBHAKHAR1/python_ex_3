# Create an empty list to store the city names
cities = []

# Loop to ask the user to enter the names of five cities
for i in range(5):
    city = input(f"Enter the name of city {i + 1}: ")
    cities.append(city)

# Print the names of the cities one by one
print("\nThe cities you entered are:")
for city in cities:
    print(city)
