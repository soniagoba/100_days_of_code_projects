import string

from scipy.fftpack import shift 

alphabet = string.ascii_lowercase

def encoder(message, shift_number):
    encoded_message = ""
    for i in range(len(message)):
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                encoded_message += alphabet[j + shift_number]
            #else:
             #   encoded_message += message[i]
    return encoded_message
    
def decoder(message, shift_number):
    decoded_message = ""
    for i in range(len(message)):
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                decoded_message += alphabet[j - shift_number]
            # else:
            #     decoded_message += message[i]

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

