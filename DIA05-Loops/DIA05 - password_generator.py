import random
import string

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters?\n"))
number_symbols = int(input("How many symbols?\n"))
number_numbers = int(input("How many numbers?\n"))
#Hay que validar que son enteros positivos

alphabet_string = string.ascii_letters
#alphabet_string = string.ascii_lowercase + string.ascii_uppercase
#alphabet_string = list(map(chr, range(97, 123)))
alphabet_list = list(alphabet_string)
symbols_list = list(map(chr, range(33, 48)))

characters = []
for i in range(1, number_letters + 1):
    letter = random.choice(alphabet_list)
    characters.append(letter)

symbols = random.choices(symbols_list, k=number_symbols)
for item in symbols:
    characters.append(item)

for number in range(1, number_numbers + 1):
    characters.append(random.randint(0, 9))

random.shuffle(characters)
print(characters)

#VER CON ALEJANDRO POR QUÉ FUNCIONA EL SEGUNDO Y NO LA FORMA "NORMAL" CON EL FOR
""" password = ''
for item in characters:
    password.join(str(item)) """
#SEGUNDA OPCIÓN: 
# password = ''.join(str(item) for item in characters)
password = ''.join(map(str, characters))
print(password)


""" SOLUCION PROFESORA:
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}") """

