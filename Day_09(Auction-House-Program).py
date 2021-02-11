logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction bid")

end_of_auction = False
bidders_list = []
def create_dict(name_user, bid_amount):
    bidder = {
        "Name": name_user,
        "Bid": bid_amount,
    }
    bidders_list.append(bidder)

def find_heighest_bid(bidders_record):
    heighest_bid = 0
    name_of_winner = ""
    for bidder in bidders_record:
        bid = bidder["Bid"]
        if heighest_bid < bid:
            heighest_bid = bid
            name_of_winner = bidder["Name"]
    print(f"End the winner is: {name_of_winner}! With bid of: {heighest_bid}$")

while not end_of_auction:
    name = input("What's your name?\n")
    bid = int(input("What's your bid: "))
    create_dict(name, bid)
    user_choice = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if user_choice == "no":
        find_heighest_bid(bidders_list)
        end_of_auction = True