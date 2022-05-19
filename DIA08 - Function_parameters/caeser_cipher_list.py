import string

alphabet_str = string.ascii_lowercase
alphabet = []
for letter in alphabet_str:
    alphabet.append(letter)

#Habría que poner dos veces el alfabeto para que no saltara una excepción si nuestras letras están al final del alfabeto
def encoder(message, shift_number):
    encoded_message = ""
    for letter in message:
        if letter in alphabet:
            indice = alphabet.index(letter)
            encoded_message += alphabet[indice + shift_number]
        else:
            encoded_message += letter
    return encoded_message
    

def decoder(message, shift_number):
    decoded_message = ""
    for letter in message:
        if letter in alphabet:
            indice = alphabet.index(letter)
            decoded_message += alphabet[indice - shift_number]
        else:
            decoded_message += letter
    return decoded_message
    
continuar = True
while continuar:
    selection = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    while selection != "encode" and selection != "decode":
        print("Wrong selection.")
        selection = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))

    if selection == "encode":
        print(f"Here's the encoded message: {encoder(message, shift_number)}")
    else:
        print(f"Here's the decoded message: {decoder(message, shift_number)}")
            
    new_game = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if new_game == "no":
        continuar = False

