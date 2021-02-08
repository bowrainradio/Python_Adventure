# How many days until 90

age = input("How old are you?\n")
age_int = int(age)
years_rem = 90 - age_int
days = int(years_rem * 365)
weeks = int(years_rem * 52)
months = int(years_rem * 12)
#
print(f"You have {days},\n{weeks} weeks,\n{months} months left till your 90 bday!")


# Tip calculator

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?\n"))
tip_perc = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))

tip_amount = (total_bill * tip_perc) / 100
final_price = round(((total_bill + tip_amount) / people), 2)

print(f"Each person should pay: {final_price}$")