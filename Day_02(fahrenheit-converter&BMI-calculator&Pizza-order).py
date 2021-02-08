#Fahrenheit converter


f_temp = int(input("Temperature outside in Farenhite?\n"))
c_temp = round(((f_temp - 32) * 5/9), 2)

print(f"Your temperature in Celsius is: {c_temp}")

height = float(input("What's your height in m(for example: 1.4)\n"))
weight = float(input("What's your weight in kg\n"))

#BMI
bmi = round(weight / (height ** 2))
print(f"Your bmi is: {bmi}")
if bmi < 18.5:
    print("You're underweight")
elif bmi < 25:
    print("You have a normal weight")
elif bmi < 30:
    print("You're overwight")
elif bmi < 35:
    print("You're obese")
else:
    print("You're clinically obese!")

# Pizza order program

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25


if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is {bill}")