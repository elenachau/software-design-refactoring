from __future__ import annotations # for roll() method
from dataclasses import dataclass, field
import random


def constrained_sum_sample_pos(n: int, total: int) -> list[int]:
    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


@dataclass
class CharacterTraits:
    strength: int = 0
    constitution: int = 0
    dexterity: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0

    @staticmethod
    def roll() -> CharacterTraits:
        # return CharacterTraits instance and pass it an unpacked version of the constraints_sum_sample_pos
        return CharacterTraits(*constrained_sum_sample_pos(6, 100))


@dataclass
class Player:
    name: str

    # add roll method to create traits
    traits: CharacterTraits = field(default_factory=CharacterTraits.roll)
    health: int = 100
    xp: int = 0
    inventory: list[str] = field(default_factory=list)


def main():
    player = Player(
        name="ArjanCodes",
    )
    print(player)


if __name__ == "__main__":
    main()
