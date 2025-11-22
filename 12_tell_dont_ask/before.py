from dataclasses import dataclass


@dataclass
class Vector:
    x: float
    y: float


def normalize(vector: Vector) -> None:
    length = (vector.x**2 + vector.y**2) ** 0.5
    vector.x /= length
    vector.y /= length


def main():
    vector = Vector(10, 5)
    normalize(vector)
    print(vector)


if __name__ == "__main__":
    main()
