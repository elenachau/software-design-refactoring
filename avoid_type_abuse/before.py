from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    role: str # role should be a constrained value, use enum instead; avoid broad types


def main():
    lucy = User(first_name="Lucy", last_name="Smith", role="admin")
    tim = User(first_name="Tim", last_name="Green", role="manager")
    print(lucy)
    print(tim)


if __name__ == "__main__":
    main()
