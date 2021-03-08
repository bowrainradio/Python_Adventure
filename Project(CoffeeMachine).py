MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.50,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'coffee': 24,
            'milk': 150,
        },
        'cost': 2.50,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'coffee': 24,
            'milk': 100,
        },
        'cost': 3.00,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

money = {
    'quarters': 0,
    'nickles': 0,
    'dimes': 0,
    'pennies': 0,
}


def getIngredients(dict_name):
    """Takes ingredients from MENU and subtracts from resources dict"""
    ingredients = MENU[dict_name]['ingredients']
    if 'water' and 'coffee' in ingredients:
        resources['water'] -= ingredients['water']
        resources['coffee'] -= ingredients['coffee']
    if 'milk' in ingredients:
        resources['milk'] -= ingredients['milk']


def resourceCheck():
    """Checks how much resources left"""
    for resource in resources:
        print(f"\nWe have: {resource} : {resources[resource]}\n")


def insertMoney():
    """Inserts coins to dict"""
    print("Please insert coins.")
    money['quarters'] = int(input("How many quarters?: "))
    money['nickles'] = int(input("How many nickles?: "))
    money['dimes'] = int(input("How many dimes?: "))
    money['pennies'] = int(input("How many pennies?: "))


def moneyCalculator():
    """Takes coins and calculates total sum"""
    sum = 0
    for coin in money:
        if coin == 'quarters':
            sum += money[coin]*0.25
        elif coin == 'nickles':
            sum += money[coin]*0.05
        elif coin == 'dimes':
            sum += money[coin]*0.1
        elif coin == 'pennies':
            sum += money[coin]*0.01
    print(f"Current balance: {round(sum, 2)}$")
    return round(sum, 2)


def coffeMachine():
    """Main Program"""
    quit_mode = False
    global cost
    while not quit_mode:
        choices_coffee = input("What would you like? (espresso/latte/cappuccino/status): ").lower()
        if choices_coffee == 'off':
            quit_mode = True
        elif choices_coffee == 'status':
            resourceCheck()
        else:
            for resource in resources:
                if resources[resource] <= MENU[choices_coffee]['ingredients'][resource]:
                    print(f"Sorry, not enough: {resource}.")
                    quit_mode = True
            getIngredients(choices_coffee)
            if cost >= MENU[choices_coffee]['cost']:
                cost -= MENU[choices_coffee]['cost']
                print(f"Current balance: {round(cost, 2)}$")
            else:
                print(f"You need: {round((cost-MENU[choices_coffee]['cost'])*-1, 2)}$ more!\nNot enough money. Money refunded")
                quit_mode = True



insertMoney()
cost = moneyCalculator()
coffeMachine()