#Love Calculator

print("Welcome to the Love Calculator")

name1 = input("What is your name \n").lower()
name2 = input("What is their name? \n").lower()

true = str(name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e"))
love = str(name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e"))

result = int(true + love)

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")


#Adventure Game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

end_message = ('''

         \  _---_  /
          \/     \/
           |() ()|
            \ + /
           / HHH \
          /  \_/  \
      {}{}{}{}{}{}{}{}{}
''')
score = 0
answer_1 = input("You're at a crossroad, where do you want to go? Type \"Left\" or \"Right?\"\n").lower()
if answer_1 == "right":
    print("You felt in to the hole!\n" + end_message)
if answer_1 == "left":
    score += 1
    answer_2 = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "Swim" to swim across. Type "Wait to wait for a boat."\n').lower()
    if answer_2 == "swim":
        print(end_message)
    if answer_2 == "wait":
        score += 1
        answer_3 = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne Red, one blue and one yellow. Which colour do you choose?\n").lower()
        if answer_3 == "blue" or answer_3 == "red":
            print(end_message)
        elif answer_3 == "yellow":
            score += 1
            print(f"You Win!\nYour score is: {score}")
        else:
            print(end_message)
    else:
        print(end_message)
else:
    print(end_message)