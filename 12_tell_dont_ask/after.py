from dataclasses import dataclass


@dataclass
class Vector:
    x: float
    y: float


    def normalize(self) -> None:
        length = (self.x**2 + self.y**2) ** 0.5
        self.x /= length
        self.y /= length


def main():
    vector = Vector(10, 5)
    vector.normalize()
    print(vector)


if __name__ == "__main__":
    main()
