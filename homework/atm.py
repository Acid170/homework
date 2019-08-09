account_name = "Eliezer Gyan"
balance = 4500
account_number = 1122
my_pin = 1234
max_withdrawal = 10000

class bank_services:
     #account_name = "Eliezer Gyan"
     #balance = 4500
     #account_number = 1122
     #my_pin = 1234
     #max_withdrawal = 10000

     def __init__(self, account_number, account_name):
            self.account_number = account_number
            self.account_name = account_name

     def deposit(self,deposit_amount):
            #deposit_amount = input("Please enter deposit amount:")
            #balance = 4500
            current_total = (deposit_amount + balance)
            print("Your current balance is:GHC", current_total)
            return current_total

     def withdraw(self,withdraw_amount):
            #withdraw_amount = input("Please enter withdrawal amount:")
            #balance = 4500
            current_total = (balance - withdraw_amount)
            print("Your current balance is:GHC", current_total)
            return current_total

     def check_pin(self):
            #my_pin = 1234
            print("Your pin is:", my_pin)

Eliezer = bank_services("0011","Eli")
Eliezer.deposit(1000)
Eliezer.withdraw(200)
Eliezer.check_pin()
