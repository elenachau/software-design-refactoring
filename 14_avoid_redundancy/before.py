from dataclasses import dataclass


@dataclass
class BankAccount:
    checking_balance: int = 0
    savings_balance: int = 0
    _total_balance: int = 0

    # redundant where every method call has to update total_balance
    def deposit_checking(self, amount: int):
        self.checking_balance += amount
        self._total_balance += amount

    def deposit_savings(self, amount: int):
        self.savings_balance += amount
        self._total_balance += amount

    def withdraw_checking(self, amount: int):
        self.checking_balance -= amount
        self._total_balance -= amount

    def withdraw_savings(self, amount: int):
        self.savings_balance -= amount
        self._total_balance -= amount

    def total_balance(self):
        return self._total_balance


def main():
    account = BankAccount()
    account.deposit_checking(100)
    account.deposit_savings(200)
    account.checking_balance += 100 # redundancy leads to bugs, doesn't update total_balance
    print(account.total_balance())


if __name__ == "__main__":
    main()
