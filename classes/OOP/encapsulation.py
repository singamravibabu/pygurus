# Encapsulation: Attributes prefixed with __ are considered private
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance

my_account = BankAccount("123456", 1000)

# get balance
print(my_account.get_balance()) # 1000

# set balance attribute
my_account.__balance = 1000000            # This is not a good practice
print(my_account.get_balance()) # 1000000