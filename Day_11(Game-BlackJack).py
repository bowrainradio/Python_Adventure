import random
logo = '''
                                      .------.
                   .------.           |A .   |
                   |A_  _ |    .------; / \  |
                   |( \/ )|-----. _   |(_,_) |
                   | \  / | /\  |( )  |  I  A|
                   |  \/ A|/  \ |_x_) |------'
                   `-----+'\  / | Y  A|
                         |  \/ A|-----' 
                         `------'
'''
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def check_score(user):
    """Take the list of cards and return sum of int inside"""
    if sum(user) == 21 and len(user) == 2:
        return 0
    if 11 in user and sum(user) > 21:
        user.remove(11)
        user.append(1)
    return sum(user)

def compare(user_s, computer_s):
    if user_s == computer_s:
        return "It's a draw"
    elif computer_s == 0:
        return "You loose"
    elif user_s == 0:
        return "BlackJack"
    elif user_s > 21:
        return "You went over! You loose"
    elif computer_s > 21:
        return "Computer went over! You win"
    elif user_s > computer_s:
        return "you win"
    else:
        return "You loose"

def play_game():
    user_cards = []
    computer_cards = []

    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {computer_cards[0]} _")

    game_over = False

    while not game_over:
        user_score = check_score(user_cards)
        computer_score = check_score(computer_cards)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            answer = input("Type 'y' to get another card, type 'n' to pass: ")
            if answer == "y":
                user_cards.append(deal_card())
                print(f"Your current hand: {user_cards}")
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = check_score(computer_cards)

    print(f"My cards: {user_cards} with score of: {user_score}")
    print(f"Computer cards: {computer_cards} with score of: {computer_score}")
    print(compare(user_s=user_score, computer_s=computer_score))

print(logo)

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    play_game()