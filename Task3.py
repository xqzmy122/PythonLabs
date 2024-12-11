class BankAccount:
    accounts_quantity = 0
    min_rest = 100

    def __init__(self, account_number = "none", balance = 0):
        self.account_number = account_number
        self.balance = balance   
        BankAccount.accounts_quantity += 1  

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if ((self.balance - amount) > BankAccount.min_rest):
            self.balance -= amount
        else:
            print("operation unavailable")
    
    def check_balance(self):
        print(f"balance {self.balance}")

    def show_atributes(self):
        print(f"account number: {self.account_number}, balance: {self.balance}$")
    
my_acc = BankAccount("5257892", 400)
my_acc.check_balance()
my_acc.deposit(300)
my_acc.show_atributes()
my_acc.withdraw(650)
    

