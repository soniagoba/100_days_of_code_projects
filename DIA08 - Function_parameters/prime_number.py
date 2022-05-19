def is_prime(selected_number):
    is_prime = True
    for number in range(2, selected_number):
        #if selected_number == 2:
         #   is_prime = True    
        if selected_number % number == 0:
            is_prime = False
    if is_prime:
        print( f"{selected_number} is a prime number")
    elif not is_prime:
        print(f"{selected_number} is not a prime number")
    else:
        print("Wrong data. It's not a number.")
    

number = int(input("Number to check: "))
is_prime(number)
