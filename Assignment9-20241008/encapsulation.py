# Using Encapsulation where some fuctions and classes are private

class Bank_Account:
    def __init__(self, name, balance):
        self.__name = name 
        self.__balance = balance

    def get_info(self):
        return f"Information about account holder. Name: {self.__name}, Balance: {self.__balance}"
    
    def deposit(self, amount):
        if(amount > 0):
            self.__balance += amount
            print(f"Amount {amount} has been deposited.")
        else:
            print("Invalid amount. Can't be deposited.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Amount {amount} has been withdrawn.")
            print(f"After withdraw {self.__balance} amount is left.")
        else:
            print("Invalid Amount.")

account = Bank_Account("Kusum", 1000)
print(account.get_info())
account.deposit(500)
account.withdraw(200)
print(account.get_info())




