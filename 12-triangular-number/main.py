import math
from util import timing

@timing
def first_num(more_than: int) -> int:
    number = 0
    delta = 1
    while True:
        number += delta
        delta += 1
        count = 0
        num_sqrt = math.sqrt(number)
        for i in range(1, math.ceil(num_sqrt)):
            if number % i == 0:
                count += 1
        count *= 2
        if num_sqrt % 1 == 0:
            count += 1 
        if count > more_than:
            return number

print(f"The first triangle number with over 500 divisors is:\n{first_num(500)}")
