class Bank:
    def __init__(self, owner = input(), balance = int(input())):
        self.owner = owner
        self.balance = balance
    def deposit(self, percentage = float(input())):
        self.percentage = percentage
        self.balance = self.balance * self.percentage
        return self.balance
    def withdrawals(self, money = int(input())):
        self.money = money
        if (self.money <= self.balance):
            self.balance -= self.money
            return self.balance
a = Bank()
print(a.deposit())
print(a.withdrawals())