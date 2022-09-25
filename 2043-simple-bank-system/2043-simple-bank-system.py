class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
    def is_acc_valid(self, acc):
        return acc >= 1 and acc <= len(self.balance)
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_acc_valid(account1) or not self.is_acc_valid(account2):
            return False
        if self.balance[account1-1] >= money:
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        return False
    def deposit(self, account: int, money: int) -> bool:
        if not self.is_acc_valid(account):
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_acc_valid(account) or self.balance[account-1] < money:
            return False
        self.balance[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)