from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RoomNotFoundError(Exception):
    """Custom error that is raised when a room is not found."""

    room_id: str
    message: str = "Room with the given id not found."


@dataclass
class Room:
    id: str
    size: int  # in square meters
    price: int  # in dollars


@dataclass
class Reservation:
    room_id: str
    customer_first_name: str
    customer_last_name: str
    customer_email_address: str
    from_date: datetime
    to_date: datetime
    price: int


@dataclass
class Hotel:
    rooms: dict[str, Room] = field(default_factory=dict)
    reservations: list[Reservation] = field(default_factory=list)

    def add_room(self, room: Room):
        self.rooms[room.id] = room

    # convoluted arguments
    def reserve_room(
        self,
        room_id: str,
        customer_first_name: str,
        customer_last_name: str,
        customer_email_address: str,
        from_date: datetime,
        to_date: datetime,
    ) -> None:
        if not self.rooms[room_id]:
            raise RoomNotFoundError(room_id)

        # compute the price
        price = (to_date - from_date).days * self.rooms[room_id].price

        # create a reservation
        self.reservations.append(
            Reservation(
                room_id,
                customer_first_name,
                customer_last_name,
                customer_email_address,
                from_date,
                to_date,
                price,
            )
        )


def main():
    hotel = Hotel()
    hotel.add_room(Room(id="1A", size=20, price=200_00))
    hotel.add_room(Room(id="12", size=10, price=150_00))
    hotel.add_room(Room(id="14B", size=40, price=700_00))

    # too many parameters
    hotel.reserve_room(
        "1A",
        "Arjan",
        "Codes",
        "hi@arjancodes.com",
        datetime(2022, 7, 15),
        datetime(2022, 7, 17),
    )

    print(hotel.reservations)


if __name__ == "__main__":
    main()
