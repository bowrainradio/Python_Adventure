# Rock, Paper, Sissors
import.random

human_choice = input("What do you chose? Type Rock, Paper or Scissors\n").lower()
rps = ["rock", "paper", "scissors"]
computer_choice = random.choice(rps)
hasha_power = "i'm hasha"
magic_power = "abrakadabra"
dog_power = "bean"

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

magic = """
         ,/   *
      _,'/_   |
      `(")' ,'/
   _ _,-H-./ /
   \_\_\.   /
    /" / \  /
  _/  /   \  \_
  \_.'( ) (`._/
       ) (
        )
"""

bean = """

     -----------------------------/ ^^^^^^^ /
   /                             |  | * * |  |
  / |   )                   |  ||\__/  @  \__/
\/   \ / /----------\______/ \ //     '-'
      ||=|=                   ||=|=

"""


ascii_hands = [rock, paper, scissors]

if computer_choice == "rock":
    print(ascii_hands[0])
elif computer_choice == "paper":
    print(ascii_hands[1])
elif computer_choice == "scissors":
    print(ascii_hands[2])

print(f"Computer chose: {computer_choice}")

if human_choice == "rock":
    print(ascii_hands[0])
elif human_choice == "paper":
    print(ascii_hands[1])
elif human_choice == "scissors":
    print(ascii_hands[2])
elif human_choice == magic_power or human_choice == hasha_power:
    print(magic)
elif human_choice == dog_power:
    print(bean)
print(f"You chose: {human_choice}")



if computer_choice == human_choice:
    print("It's a draw")
elif human_choice == "rock" and computer_choice == "paper":
    print("You lose!")
elif human_choice == "paper" and computer_choice == "rock":
    print("You lose!")
elif human_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif human_choice == "paper" and computer_choice == "scissors":
    print("You lose!")
elif human_choice == "scissors" and computer_choice == "rock":
    print("You lose!")
elif human_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif human_choice == magic_power or human_choice == hasha_power or human_choice == dog_power:
    print("You win!")
else:
    print("You lose!")