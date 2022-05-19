print("Welcome to the Band Name Generator.")


city = input("City you grew up in?\n")
#Validar entrada solo letras y al menos un caracter:
while city.isalpha() == False or len(city) <= 0:
    print("Debes indicar una ciudad.")
    city = input("City you grew up in?\n")

pet = input("Your pet's name?\n")
#Validar entrada alfanumércia y al menos un caracter:
while pet.isalnum() == False or len(pet) <= 0:
    print("Debes indicar nombre mascota. ")
    pet = input("Your pet's name?\n")

#Tres formas de imprimir string con variables:
print("Your band name could be " + city + " " + pet)
print("Your band name could be {} {}".format(city, pet))
print(f"Your band name could be {city} {pet}")

