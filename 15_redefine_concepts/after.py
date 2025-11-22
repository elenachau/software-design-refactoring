from enum import Enum
from typing import Protocol


class Payment(Protocol):
    def pay(self, amount: int) -> None: ...


class PaypalPayment:  # remove inheritance relationship
    def pay(self, amount: int) -> None:
        print(f"Paying {amount} using Paypal")


class StripePayment:  # remove inheritance relationship
    def pay(self, amount: int) -> None:
        print(f"Paying {amount} using Stripe")


class PaymentMethod(Enum):
    PAYPAL = "paypal"
    CARD = "card"


# str is too generic
PAYMENT_METHODS: dict[PaymentMethod, type[Payment]] = {
    PaymentMethod.CARD: StripePayment,
    PaymentMethod.PAYPAL: PaypalPayment,
}


def create_payment_handler(payment_method: PaymentMethod) -> Payment:
    return PAYMENT_METHODS[payment_method]()  # don't forget to call initializer


def main() -> None:
    # my_payment = PAYMENT_METHODS[PaymentMethod.CARD]()
    my_payment = create_payment_handler(PaymentMethod.CARD)
    my_payment.pay(100)


if __name__ == "__main__":
    main()
