class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance=self.balance-amount
        else:
            print("sorry,Insufficient Funds")

    def printstatement(self):
        print("Account Balance:",self.balance)

class Currentaccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
    def __str__(self):
        return"{}'s Current Account with Balance :{}".format(self.name,self.balance)

class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
    def __str__(self):
        return"{}'s Savings Account with Balance :{}".format(self.name,self.balance)

c=Savings("SRK",10000)
print(c)
c.deposit(5000)
c.withdraw(17000)
print(c)

c2=Currentaccount("saud",20000)
c2.deposit(3500)
print(c2)
c2.withdraw(27000)
print(c2)
