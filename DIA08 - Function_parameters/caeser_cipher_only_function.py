import string

alphabet_str = string.ascii_lowercase
alphabet = []
for letter in alphabet_str:
    alphabet.append(letter)

#Habría que poner dos veces el alfabeto para que no saltara una excepción si nuestras letras están al final del alfabeto
def caesar(direction, message, shift_number):
    new_message = ""
    for letter in message:
        if letter in alphabet:
            indice = alphabet.index(letter)
            if direction == "encode":
                new_message += alphabet[indice + shift_number]
            elif direction == "decode":
                new_message += alphabet[indice - shift_number]
        #else:
         #   encoded_message += letter
    return new_message
        
continuar = True
while continuar:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    while direction != "encode" and direction != "decode":
        print("Wrong selection.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))

    print(f"The new message is {caesar(direction, message, shift_number)}")
    
    new_game = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if new_game == "no":
        continuar = False


#Solución de única función profesora:

""" def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}") """
