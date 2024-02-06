class My_bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        print(f"Your name : {name} balance {balance}")
        pass
    def deposit(self, money):
        self.balance += money
        print(f"Deposit: {self.balance}")
        
    def withdraw(self, money):
        if self.balance - money >= 0:
            self.balance -= money
            print(f"Your balance:{self.balance}")
            return
        else: 
            print("Your balance don't enough{self.balance}")
            return
        
        
client = My_bank(input("Your name:"),int(input("Your balance")))
client.__init__
client.deposit(int(input("deposit:")))
client.deposit
client.withdraw(int(input("withdraw:")))
client.withdraw


            
    