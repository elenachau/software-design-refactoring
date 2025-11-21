import random
from dataclasses import dataclass, field


@dataclass
class DiceGame:
    dice_count: int = 5
    roll: list[int] = field(default_factory=list)

    def roll_dice(self):
        self.roll = []
        for _ in range(self.dice_count):
            self.roll.append(self.roll_die())

    def roll_die(self) -> int:
        return random.randint(1, 6)

    def total(self) -> int:
        dice_sum = 0
        for die in self.roll:
            dice_sum += die
        return dice_sum


def main():
    my_game = DiceGame()
    my_game.roll_dice()
    print(f"Total: {my_game.total()}")


if __name__ == "__main__":
    main()
