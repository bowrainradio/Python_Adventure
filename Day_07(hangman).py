import random

# from hangman_art import logo, stages

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')
print("Welcome to Hangman")

word_list = ["Apple", "Rasberry", "President"]
random_word = random.choice(word_list).lower()

display_word = []
word_split = []
game_over = False
lives = len("hangman")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

for letter in range(len(random_word)):
    display_word += "_"


while not game_over:
    print(f"Your word for today: {display_word}")
    user_guess = input("Please guess a letter: ")
    if user_guess == "help":
        print(f"Little help for you: {random_word[random.randint(0, len(display_word)-1)]}")
    if user_guess in display_word:
        print(f"You already guess this letter: {user_guess}")
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == user_guess:
            display_word[position] = letter
    if "_" not in display_word:
        game_over = True
        print("You won!")
    if user_guess not in random_word and user_guess != "help":
        lives -= 1
        print(stages[lives])
        print(f"Upss....!!!\nYour letter - {user_guess} - is not in the word. Try again!")
        if lives == 0:
            game_over = True
            print("You lose")

    # if user_guess == "help":
        # print(f"Let me help you! There is: {random_word[random.randint(0, len(random_word))]} letter in this word")