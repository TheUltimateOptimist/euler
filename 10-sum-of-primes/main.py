import math

def sum_of_primes(below: int) -> int:
    result = 0
    num = 2
    while num < below:
        is_prime = True
        for i in range(2, math.ceil(math.sqrt(below))):
            if num == i:
                break
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result += num
        num += 1
    return result

print(f"the sum of all primes below 2_000_000 is:\n{sum_of_primes(2_000_000)}")