# doesn't clearly show which message type corresponds to which priority type
def get_message_priority(message: str) -> str: # returning str which is a broad type to represent message priority
    # this is a nested conditional
    return (
        "high"
        if message.startswith("!")
        else "medium"
        if message.startswith("#")
        else "low"
    )


def main():
    message1 = "Please do the dishes"
    message2 = "# I really want you to do the dishes"
    message3 = "! Aaaaargh do the dishes now you lazy bastard!"
    print(f"Priority of message1: {get_message_priority(message1)}")
    print(f"Priority of message2: {get_message_priority(message2)}")
    print(f"Priority of message3: {get_message_priority(message3)}")


if __name__ == "__main__":
    main()
