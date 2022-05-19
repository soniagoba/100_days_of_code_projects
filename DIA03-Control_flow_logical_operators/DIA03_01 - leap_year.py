""" number = int(input("Number: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd. ") """

year = int(input("Year: "))
if year % 4 != 0:
    print(f"{year} is not a leap year. ")
else:
    if year % 100 == 0:
        if year % 400 == 0: 
            print(f"{year} is a leap year. ")
        else:
            print(f"{year} is not a leap year. ")
    else:
        print(f"{year} is a leap year. ")


""" year = int(input("Year: "))
if year % 4 != 0:
    print("Not a leap year.")
else:
    if year % 100 == 0 and year % 400 == 0:
        print(f"{year} is a leap year. ")
    elif year % 100 == 0 and year % 400 != 0:
        print(f"{year} is not a leap year. ")
    else:
        print(f"{year} is a leap year. ")

#Se puede poner así:
year = int(input("Year: "))
if year % 4 != 0:
    print("Not a leap year.")
else:
    if year % 100 == 0 and year % 400 != 0:
        print(f"{year} is not a leap year. ")
    else:
        print(f"{year} is a leap year. ") """

    

    