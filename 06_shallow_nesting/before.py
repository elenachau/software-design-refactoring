# pay method has low cohesion
def pay(
    payment_method: str, amount: int, card_number: str = "", paypal_email: str = ""
):
    # nested if statements not ideal
    if payment_method == "card": # card_number argument only used in this case, indication to split func
        if card_number:
            print(f"Paid ${amount/100:.2f} using card with number {card_number}")
    elif payment_method == "paypal": # paypal_email argument only used in this case, indication to split func
        if paypal_email:
            print(f"Paid ${amount/100:.2f} from paypal email {paypal_email}")
    else:
        print(f"Unknown payment method {payment_method}")


def main():
    pay("card", 100_00, "1234-5678-9012-3456")
    pay("paypal", 1000_00, paypal_email="hi@arjancodes.com")


if __name__ == "__main__":
    main()
