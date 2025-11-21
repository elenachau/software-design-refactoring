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

    def place_order(self, amount: int, sell: bool = False) -> None: # sell flag indicates low cohesion
        if sell:
            if amount > self.balance:
                raise NotEnoughFundsError(amount, self.balance)
            print(f"Selling {amount * SATOSHI_TO_BTC_RATE} BTC.")
            self.balance -= amount
        else:
            print(f"Buying {amount * SATOSHI_TO_BTC_RATE} BTC.")
            self.balance += amount


def main():
    wallet = BitcoinWallet()
    wallet.place_order(100_000)  # buy some Bitcoin
    wallet.place_order(50_000, True)  # sell some Bitcoin
    print(wallet)


if __name__ == "__main__":
    main()
