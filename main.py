# class car:
#     def __init__(self,model,make, year):
#         self.model = model
#         self.make = make
#         self.year = year
# car1 = car(911,"porche", 2001)
    
    
# print(car1.make)
# print(car1.model)
# print(car1.year)


class bank_account:
    def __init__(self, money, sort_code, account_number, account_name):
        self.money = money
        self.sort_code = sort_code
        self.account_number = account_number
        self.account_name = account_name
        
    def withdraw(self, amount):
        if amount_to_withdraw > self.money:
            print("you dont have that much broke boy")
        else:
            self.money -= amount

    
my_bank_account = bank_account(500,549383,86307275,"William Hall")

print(my_bank_account.account_name)
print(my_bank_account.account_number)
print(my_bank_account.sort_code)
print(my_bank_account.money)
    
amount_to_withdraw = int(input("how much do you want to withdraw"))

my_bank_account.withdraw(amount_to_withdraw)
print(my_bank_account.money)
    

