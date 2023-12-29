def f(n: int, a: int, b: int):
    assert abs(a) < 1000
    assert abs(b) <= 1000
    return n*n + a*n + b

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

max_primes = 0
max_combo = (0, 0)

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        count = 0
        n = 0
        while is_prime(f(n, a, b)):
            count += 1
            n += 1
        if count > max_primes:
            max_primes = count
            max_combo = (a, b)

print(f"The combo product of a and b with the max number of consecutive primes is:\n{max_combo[0]*max_combo[1]}")