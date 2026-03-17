class bank_account :
    def __init__ (self , owner , balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, interest):
        self.balance = self.balance * interest
        return self.balance 
        
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance



owner1 = bank_account("alex", 1000)
print(owner1.deposit(2))
print(owner1.withdraw(200))
print(owner1)