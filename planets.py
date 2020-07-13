import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))
print('Random list:', my_randoms)
# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False

    for rand_num in my_randoms:
        if number == rand_num:
            the_numbers_match = True

    # Iterate your random number list here

    # Does my_randoms contain number? Change the boolean.
    if the_numbers_match == True:
        print(f'my_randoms list contains {number}')
    elif the_numbers_match == False:
        print(f'my_randoms does not contain {number}')

planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")

rocky_planets = planet_list[:4]

del planet_list[8]

print('Planet List:', planet_list)
print('Rocky planets:', rocky_planets)

spacecraft = [
    ("MESSENGER", "Mercury"),
    ("Venera 5", "Venus"),
    ("Venera 6", "Venus"),
   ("Cassini", "Saturn"),
   ("Voyager 1", "Saturn"),
   ("Voyager 2", "Saturn"),
   ("Viking", "Mars"),
   ("Mars Observer", "Mars"),
   ("Mars Pathfinder", "Mars"),
   ("Galileo", "Jupiter"),
   ("Juno", "Jupiter"),
   ("Akatsuki", "Jupiter"),
   ("Voyager 2", "Neptune"),
]

for planet in planet_list:
    planet_voyage_dict = dict()
    planet_voyage_dict["planet"] = planet
    planet_voyage_dict["voyages"] = list()
    for craft in spacecraft:
        if craft[1] == planet:
            planet_voyage_dict["voyages"].append(craft[0])
    print(planet_voyage_dict)
