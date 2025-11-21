from dataclasses import dataclass


@dataclass
class Contract:
    hours_worked: float
    hourly_rate: int = 50_00

    def compute_pay(self):
        return self.hours_worked * self.hourly_rate


def main():
    contract = Contract(hours_worked=20)
    print(contract.compute_pay())


if __name__ == "__main__":
    main()
