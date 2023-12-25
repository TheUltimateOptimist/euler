def prime_factors(number: int) -> list[int]:
    assert number >= 0
    assert number % 1 == 0
    if number == 0:
        return []
    if number == 1:
        return [1]
    factors = []
    factor = 2
    while True:
        if number == factor:
            factors.append(number)
            return factors
        if number % factor == 0:
            factors.append(factor)
            number = number // factor
            factor = 2
        else:
            factor += 1

def largest_prime_factor(number: int) -> int:
    factor = 2
    while True:
        if number == factor:
            return number
        if number % factor == 0:
            number //= factor; factor = 2
        else: factor += 1

print(f"The largest prime factor of 600851475143 is:\n{largest_prime_factor(600851475143)}")