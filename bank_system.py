class User():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def details(self):
        print("\nYour personal Details")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")


class Bank(User):  # child class
    def __init__(self, name, age, sex):
        super().__init__(name, age,sex)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"\nYour current balance: {self.balance}$")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"\nInsufficient Funds\nYour current balance: {self.balance}$")
        else:
            self.balance -= self.amount
            print(f"\nYou withdrawed: {self.amount}$\nYour current balance: {self.balance}$")

    def print_balance(self):
        self.details()
        print(f"\nYour current balance: {self.balance}")


user_01 = Bank("Filip", 24, "Male")
user_02 = Bank("Rainbow", 24, "Female")

user_01.details()
user_02.details()

user_01.deposit(400)
user_02.deposit(200)

user_01.withdraw(200)
user_02.withdraw(200)

user_02.withdraw(222)  # Error, insufficient Funds

user_01.print_balance()
user_02.print_balance()
