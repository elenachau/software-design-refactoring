from dataclasses import dataclass


@dataclass
class BankAccount:
    checking_balance: int = 0
    savings_balance: int = 0

    def deposit_checking(self, amount: int):
        self.checking_balance += amount

    def deposit_savings(self, amount: int):
        self.savings_balance += amount

    def withdraw_checking(self, amount: int):
        self.checking_balance -= amount

    def withdraw_savings(self, amount: int):
        self.savings_balance -= amount

    @property # because compute value
    def total_balance(self):
        return self.checking_balance + self.savings_balance


def main():
    account = BankAccount()
    account.deposit_checking(100)
    account.deposit_savings(200)
    print(account.total_balance)


if __name__ == "__main__":
    main()
