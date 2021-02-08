# PyPassword Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPasswordGenerator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_number = int(input("How many number would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))


password_list = []

for char in range(1, nr_letters +1):
    password_list.append(random.choice(letters))


for num in range(1, nr_number+1):
    password_list.append(random.choice(number))

for sym in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char


print(f"Your password is: {password}.\nYour password length is: {len(password)}")