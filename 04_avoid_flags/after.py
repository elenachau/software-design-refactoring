from dataclasses import dataclass

SATOSHI_TO_BTC_RATE = 0.00000001


@dataclass
class NotEnoughFundsError(Exception):
    """Custom error that is raised when there are not enough funds in the account."""

    amount: int
    available_balance: int
    message: str = "Not enough funds in wallet."


@dataclass
class BitcoinWallet:
    balance: int = 0  # in satoshi

    # create separate buy and sell method
    def sell(self, amount: int) -> None:
        if amount > self.balance:
                raise NotEnoughFundsError(amount, self.balance)
        print(f"Selling {amount * SATOSHI_TO_BTC_RATE} BTC.")
        self.balance -= amount

    def buy(self, amount: int) -> None: # remove sell flag
        print(f"Buying {amount * SATOSHI_TO_BTC_RATE} BTC.")
        self.balance += amount


def main():
    wallet = BitcoinWallet()
    wallet.buy(100_000)
    wallet.sell(50_000)
    print(wallet)


if __name__ == "__main__":
    main()
