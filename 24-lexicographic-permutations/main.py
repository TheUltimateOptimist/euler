from typing import Any, TypeVar

T = TypeVar("T")

def factorial(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def nth_permutation(elements: list[T], n: int) -> list[T]:
    permutation: list[T] = []
    while len(elements) > 0:
        fac = factorial(len(elements) - 1) if n > 0 else 1
        element = elements.pop(n // fac)
        permutation.append(element)
        n = n % fac
    return permutation

print(f"The 1_000_000th permutation is:\n{''.join(map(lambda x: str(x), nth_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 999_999)))}")


