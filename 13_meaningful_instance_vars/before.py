from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class LineItem:
    name: str
    price: int
    quantity: int = 1
    tax_rate: float = 0.21


@dataclass
class Invoice:
    items: list[LineItem] = field(default_factory=list)
    customer: str = ""
    date: datetime = datetime.now()

    def add_line_item(self, item: LineItem):
        self.items.append(item)

    def print(self):
        # create too many temporary variables, but store as part of object with self
        self._subtotals: list[int] = [] # unnecessary instance variables
        self._taxes: list[int] = [] # unnecessary instance variables
        self._total_taxes = 0
        self._total = 0

        print(f"Invoice for {self.customer}")
        print(f"Printed on {self.date}")
        print("-" * 50)
        print("{:<20}{:>10}{:>10}{:>10}".format("Item", "Price", "Qty", "Total"))
        print("-" * 50)
        for i, item in enumerate(self.items):
            self._subtotals.append(item.price * item.quantity)
            self._taxes.append(
                int(item.price * item.quantity / (1 + item.tax_rate) * item.tax_rate)
            )
            print(
                "{:<20}{:>10.2f}{:>10}{:>10.2f}".format(
                    item.name, item.price / 100, item.quantity, self._subtotals[i] / 100
                )
            )
        self._total_taxes = sum(self._taxes)
        self._total = sum(self._subtotals)
        print("-" * 50)
        print("{:<20}{:>10}{:>10}{:>10.2f}".format("Total", "", "", self._total / 100))
        print(
            "{:<20}{:>10}{:>10}{:>10.2f}".format(
                "Taxes", "", "", self._total_taxes / 100
            )
        )
        print("=" * 50)


def main():
    invoice = Invoice(customer="John Doe")
    invoice.add_line_item(LineItem(name="Apple", price=50, quantity=4))
    invoice.add_line_item(LineItem(name="Orange", price=30, quantity=10))
    invoice.print()


if __name__ == "__main__":
    main()
