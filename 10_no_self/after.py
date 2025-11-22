import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:  # turn into generic function
    return "".join(random.choices(string.ascii_uppercase, k=8))


@dataclass
class Room:
    number: str  # room number
    size: int  # in square meters
    price: int  # in dollars


@dataclass
class Hotel:
    rooms: dict[str, Room] = field(default_factory=dict)

    def add_room(self, room: Room) -> str:
        room_id = generate_id()  # remove self
        self.rooms[room_id] = room
        return room_id


def main():
    hotel = Hotel()
    hotel.add_room(Room(number="1A", size=20, price=200_00))
    hotel.add_room(Room(number="12", size=10, price=150_00))
    hotel.add_room(Room(number="14B", size=40, price=700_00))

    print(hotel)


if __name__ == "__main__":
    main()
