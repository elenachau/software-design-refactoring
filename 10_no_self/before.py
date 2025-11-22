import random
import string
from dataclasses import dataclass, field


@dataclass
class Room:
    number: str  # room number
    size: int  # in square meters
    price: int  # in dollars


@dataclass
class Hotel:
    rooms: dict[str, Room] = field(default_factory=dict)

    def add_room(self, room: Room) -> str:
        room_id = self.generate_room_id()
        self.rooms[room_id] = room
        return room_id

    def generate_room_id(self) -> str: # doesn't use self
        return "".join(random.choices(string.ascii_uppercase, k=8))


def main():
    hotel = Hotel()
    hotel.add_room(Room(number="1A", size=20, price=200_00))
    hotel.add_room(Room(number="12", size=10, price=150_00))
    hotel.add_room(Room(number="14B", size=40, price=700_00))

    print(hotel)


if __name__ == "__main__":
    main()
