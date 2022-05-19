print("Welcome to the tip calculator.")

total_bill_valid = False
while not total_bill_valid:
    try:
        total_bill = float(input("What was the total bill? ")) 
        total_bill_valid = True
    except:
        print("Total bill must be a float number.")
    else: #Si va bien el try:
        if total_bill <= 0:
            print("Total bill must be positive. ")
            total_bill_valid = False
        else:
            total_bill_valid = True

people_valid = False
while not people_valid: 
    try:
        people = int(input("How many people to split it? "))
        people_valid = True
    except:
        print("People must be an integer number.")
    else: #Si va bien el try:
        if people <= 0:
            print("Number of people must be positive.")
            people_valid = False
        else:
            people_valid = True

tip_percentage = input("Percentage tip? 10, 12 or 15? ")
while tip_percentage != "10" and tip_percentage != "12" and tip_percentage != "15":
    print("Percentage should be 10, 12 or 15")
    tip_percentage = input("Percentage tip? 10, 12 or 15? ")

bill_with_tip = float(total_bill) * ( 1 + int(tip_percentage) / 100)
individual_payment = bill_with_tip / int(people)
print("Each person should pay: {:.2f}€".format(individual_payment)) 




""" numero = input("Número: ")
numero_1 = numero[0]
numero_2 = numero[1]
suma = int(numero_1) + int(numero_2)
#print(f"{numero_1} + {numero_2} = {suma}")
#print("{} + {} = {}".format(numero_1, numero_2, suma)) """




