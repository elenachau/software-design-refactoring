class Payment:
    def __new__(cls, payment_type: str): # overwriting this method
        if payment_type == "paypal":
            return object.__new__(PaypalPayment) # returns new obj of subclass
        elif payment_type == "card":
            return object.__new__(StripePayment) # returns new obj of subclass

    def pay(self, amount: int) -> None:
        raise NotImplementedError


class PaypalPayment(Payment):
    def pay(self, amount: int) -> None:
        print(f"Paying {amount} using Paypal")


class StripePayment(Payment):
    def pay(self, amount: int) -> None:
        print(f"Paying {amount} using Stripe")


def main() -> None:
    my_payment = Payment("card") # Payment creates own subclasses but Payment shouldn't know anything about their subclasses
    my_payment.pay(100)


if __name__ == "__main__":
    main()
