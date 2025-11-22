from dataclasses import dataclass
from datetime import datetime


@dataclass
class PowerDrill:
    daily_rate: int = 25_00
    is_hammer: bool = True

    def compute_rent(self, days: int) -> int:
        return days * self.daily_rate


@dataclass
class CementMixer:
    daily_rate: int = 80_00  # change naming
    capacity_litres: int = 1000

    def compute_rent(
        self, days: int
    ) -> int:  # change naming, parameter now expects days
        return days * self.daily_rate


def main():
    drill = PowerDrill()
    mixer = CementMixer()
    print(f"Renting a drill for 3 days: ${drill.compute_rent(3)/100:.2f}")
    from_date = datetime(2020, 1, 1)
    to_date = datetime(2020, 1, 5)
    days = (to_date - from_date).days + 1
    print(f"Renting a mixer for 5 days: ${mixer.compute_rent(days)/100:.2f}")


if __name__ == "__main__":
    main()
