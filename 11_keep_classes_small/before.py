from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    strength: int
    constitution: int
    dexterity: int
    intelligence: int
    wisdom: int
    charisma: int
    health: int = 100
    xp: int = 0
    inventory: list[str] = field(default_factory=list)


def main():
    player = Player(
        name="ArjanCodes",
        strength=10,
        constitution=10,
        dexterity=10,
        intelligence=10,
        wisdom=10,
        charisma=10,
    )
    print(player)


if __name__ == "__main__":
    main()
