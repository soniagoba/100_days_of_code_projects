# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
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

print(f"{weight} ÷ ({height} x {height}) = {bmi}")
print("Your BMI is {}, {}".format(bmi, resultado))
