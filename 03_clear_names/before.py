from dataclasses import dataclass


@dataclass
class Contract:
    amount: float # amount naming is too vague
    hourly_rate: int = 50_00

    def compute_pay(self):
        return self.amount * self.hourly_rate


def main():
    contract = Contract(amount=20)
    print(contract.compute_pay())


if __name__ == "__main__":
    main()
