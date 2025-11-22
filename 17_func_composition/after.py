import functools
from typing import Callable

ComposableFunction = Callable[[float], float]


# helper function for composing functions
def compose(*functions: ComposableFunction) -> ComposableFunction:
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions) # reduce() calls functions in sequence


def add_three(x: float) -> float:
    return x + 3


def multiply_by_two(x: float) -> float:
    return x * 2


def add_n(x: float, n: float) -> float: # use functools.partial because function composition cannot call 2nd argument
    return x + n


def main():
    x = 12
    add_ten = functools.partial(add_n, n=10)
    my_func = compose(add_ten, add_three, add_three, multiply_by_two, multiply_by_two)
    result = my_func(x)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
