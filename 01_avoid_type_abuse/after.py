from dataclasses import dataclass
from enum import Enum


class Role(Enum): # using auto() can be problematic for indexing in database
    EMPLOYEE = "employee"
    OWNER = "owner"
    ADMIN = "admin"
    MANAGER = "manager"


@dataclass
class User:
    first_name: str
    last_name: str
    role: Role


def main():
    lucy = User(first_name="Lucy", last_name="Smith", role=Role.ADMIN)
    tim = User(first_name="Tim", last_name="Green", role=Role.MANAGER)
    print(lucy)
    print(tim)


if __name__ == "__main__":
    main()
