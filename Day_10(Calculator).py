
logo = '''
 _____________________
|  _________________  |
| | Py_Calculator   | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

print(logo)
print("Welcome to Py_Calculator")

#add

def add(n1, n2):
    """Adding two numbers"""
    return n1 + n2

#subtact
def subtract(n1, n2):
    """Subtracting two numbers"""
    return n1 - n2

#Multiply
def multiply(n1, n2):
    """Multiplying two numbers"""
    return n1 * n2

#divid
def divid(n1, n2):
    """Dividing two numbers"""
    return n1 / n2

def round_my_num(my_num, decimal):
    return round(my_num, int(decimal))

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divid,
    "≈": round_my_num,
}

def print_symbols():
    for operation in operations:
        print(operation)

def calculator():
    finish = False
    first_number = float(input("What's the first number?: "))
    while not finish:
        print_symbols()
        operation_symbol = input("Pick an operation: ")
        function = operations[operation_symbol]
        if operation_symbol == "≈":
            second_number = float(input("Number of decimals?: "))
        else:
            second_number = float(input("What's the next number?: "))
        result = function(first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {result}")
        user_choice = input(f"Continue calculating with: {result} ?\nType 'y' for yes or 'restart' to start new calculation or type 'stop' to end for today: ")
        if user_choice == "stop":
            finish = True
            print(f"You ended with: {result}. Bye Bye")
        elif user_choice == "y":
            first_number = result
        else:
            finish = True
            print(f"You ended with: {result}. Let's start again!")
            calculator()


calculator()