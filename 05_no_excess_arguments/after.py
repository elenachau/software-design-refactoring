from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RoomNotFoundError(Exception):
    """Custom error that is raised when a room is not found."""

    room_id: str
    message: str = "Room with the given id not found."


@dataclass
class CustomerNotFoundError(Exception):
    """Custom error that is raised when a customer is not found."""

    customer_id: str
    message: str = "Customer with the given id not found."


@dataclass
class Room:
    id: str
    size: int  # in square meters
    price: int  # in dollars


# create separate Customer class to reduce complexity of Reservation class
@dataclass
class Customer:
    first_name: str
    last_name: str
    email_address: str


@dataclass
class Reservation:
    room_id: str
    customer: Customer  # reference Customer class
    from_date: datetime
    to_date: datetime
    price: int


@dataclass
class Hotel:
    rooms: dict[str, Room] = field(default_factory=dict)
    reservations: list[Reservation] = field(default_factory=list)

    # create data structure to contain Customer
    customers: dict[str, Customer] = field(default_factory=dict)

    def add_room(self, room: Room):
        self.rooms[room.id] = room

    def add_customer(self, customer: Customer):
        self.customers[customer.email_address] = customer

    def reserve_room(
        self,
        room_id: str,
        customer_id: str,  # instead of passing customer data
        from_date: datetime,
        to_date: datetime,
    ) -> None:
        if not self.rooms[room_id]:
            raise RoomNotFoundError(room_id)
        if not self.customers[customer_id]:
            raise CustomerNotFoundError(customer_id)

        # compute the price
        price = (to_date - from_date).days * self.rooms[room_id].price

        # create a reservation
        customer = self.customers[customer_id]  # retrieve customer from dict
        self.reservations.append(
            Reservation(
                room_id,
                customer,
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
    hotel.add_customer(Customer("Arjan", "Codes", "hi@arjancodes.com"))

    hotel.reserve_room(
        "1A",
        "hi@arjancodes.com",  # email is customer_id
        datetime(2022, 7, 15),
        datetime(2022, 7, 17),
    )

    print(hotel.reservations)


if __name__ == "__main__":
    main()
