#Write your code below this row 👇

suma = 0
for numero in range (1, 101):
    if numero % 2 == 0:
        suma += numero

print(suma)

""" Otra opción es:
for numero in range (1, 101, 2):
    suma += numero
print(suma)
"""
