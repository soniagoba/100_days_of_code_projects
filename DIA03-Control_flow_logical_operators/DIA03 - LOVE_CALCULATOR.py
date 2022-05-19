# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
name_min = name.lower()

for letra in range(len(name)):
   name_min = name_min.replace(" ", "")

#print(name_min)

t = int(name_min.count("t"))
r = int(name_min.count("r"))
u = int(name_min.count("u"))
e = int(name_min.count("e"))

#print(f"T occurs {t} times")
#print(f"R occurs {r} times")
#print(f"U occurs {u} times")
#print(f"E occurs {e} times")

digito1 = t + r + u + e
#print(f"Digito1 = {digito1}")


l = int(name_min.count("l"))
o = int(name_min.count("o"))
v = int(name_min.count("v"))
e = int(name_min.count("e"))

#print(f"L occurs {l} times")
#print(f"O occurs {o} times")
#print(f"V occurs {v} times")
#print(f"E occurs {e} times")

digito2 = l + o + v + e
#print(f"Digito2 = {digito2}")

Love_Score = str(digito1) + str(digito2)
Love_Score_int = int(Love_Score)

if Love_Score_int < 10 or Love_Score_int > 90:
   print("'Your score is " + Love_Score + ", you go together like coke and mentos.'")
elif Love_Score_int > 40 and Love_Score_int < 50:
   print("'Your score is " + Love_Score + ", you are alright together.'")
else:
   print("'Your score is " + Love_Score + ".'")
