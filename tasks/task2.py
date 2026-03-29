class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposite(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостатньо коштів")

    def get_balance(self):
        return self.__balance

owner = input("Ім'я: ")
balance = float(input("Початковий баланс: "))

acc = BankAccount(owner, balance)

acc.deposite(float(input("Сума поповнення: ")))
acc.withdraw(float(input("Сума зняття: ")))

print("Баланс =", acc.get_balance())