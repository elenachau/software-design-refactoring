from dataclasses import dataclass
from datetime import datetime

# daily_rate and cost_per_day asymmetrical
# compute_rent has different parameters

@dataclass
class PowerDrill:
    daily_rate: int = 25_00
    is_hammer: bool = True

    def compute_rent(self, days: int) -> int:
        return days * self.daily_rate


@dataclass
class CementMixer:
    cost_per_day: int = 80_00
    capacity_litres: int = 1000

    def compute_rental_price(self, from_date: datetime, to_date: datetime) -> int:
        days = (to_date - from_date).days + 1
        return days * self.cost_per_day


def main():
    drill = PowerDrill()
    mixer = CementMixer()
    print(f"Renting a drill for 3 days: ${drill.compute_rent(3)/100:.2f}")
    from_date = datetime(2020, 1, 1)
    to_date = datetime(2020, 1, 5)
    print(
        f"Renting a mixer for 5 days: ${mixer.compute_rental_price(from_date, to_date)/100:.2f}"
    )


if __name__ == "__main__":
    main()
