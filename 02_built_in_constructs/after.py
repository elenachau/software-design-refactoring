import random
from dataclasses import dataclass, field


@dataclass
class DiceGame:
    dice_count: int = 5
    roll: list[int] = field(default_factory=list)

    def roll_dice(self):
        # use list comprehension instead
        self.roll = [self.roll_die() for _ in range(self.dice_count)]

    def roll_die(self) -> int:
        return random.randint(1, 6)

    def total(self) -> int:
        return sum(self.roll)  # rely on built-in func to make code shorter and maintable e.g. sum func


def main():
    my_game = DiceGame()
    my_game.roll_dice()
    print(f"Total: {my_game.total()}")


if __name__ == "__main__":
    main()
