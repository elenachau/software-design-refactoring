def pay_card(amount: int, card_number: str) -> None:
    print(f"Paid ${amount/100:.2f} using card with number {card_number}")


def pay_paypal(amount: int, paypal_email: str) -> None:
    print(f"Paid ${amount/100:.2f} from paypal email {paypal_email}")


def main():
    pay_card(100_00, "1234-5678-9012-3456")
    pay_paypal(1000_00, paypal_email="hi@arjancodes.com")


if __name__ == "__main__":
    main()
