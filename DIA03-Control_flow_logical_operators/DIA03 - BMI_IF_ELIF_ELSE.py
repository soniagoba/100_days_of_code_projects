# ๐จ Don't change the code below ๐
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# ๐จ Don't change the code above ๐

#Write your code below this line ๐
bmi = round(weight / height ** 2)


if bmi < 18.5:
    resultado = "You are underweight"
elif bmi < 25:
    resultado = "You have a normal weight"
elif bmi < 30:
    resultado = "You are slightly overweight"
elif bmi < 35:
    resultado = "You are obese"
else:
    resultado = "You are clinically obese"

print(f"{weight} รท ({height} x {height}) = {bmi}")
print("Your BMI is {}, {}".format(bmi, resultado))
