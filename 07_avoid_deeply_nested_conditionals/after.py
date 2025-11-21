from enum import Enum


# use Enum to represent message priority
class MsgPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


def get_message_priority(message: str) -> MsgPriority:
    # solved nested conditional with if statement
    if message.startswith("!"):
        return MsgPriority.HIGH
    elif message.startswith("#"):
        return MsgPriority.MEDIUM
    else:
        return MsgPriority.LOW


def main():
    message1 = "Please do the dishes"
    message2 = "# I really want you to do the dishes"
    message3 = "! Aaaaargh do the dishes now you lazy bastard!"
    print(f"Priority of message1: {get_message_priority(message1).name}") # .name prints str value instead of the Enum
    print(f"Priority of message2: {get_message_priority(message2).name}")
    print(f"Priority of message3: {get_message_priority(message3).name}")


if __name__ == "__main__":
    main()
