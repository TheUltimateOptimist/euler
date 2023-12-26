import math
from util import timing

@timing
def naive_brute_foce() -> tuple[int, int, int]:
    for i in range(1, 333):
        for j in range(i + 1, math.ceil((1000 - i) / 2)):
            for k in range(j + 1, 1000 - i - j + 1):
                if i + j + k == 1000 and i*i + j*j == k*k:
                    return (i, j, k)

@timing
def optimized_brute_force() -> tuple[int, int, int]:
    for i in range(1, 333):
        for j in range(i + 1, math.ceil((1000 - 1) / 2)):
            c  = 1000 - i - j
            if i*i + j*j == c*c:
                return (i, j, c)

@timing
def max_optimized() -> tuple[int, int, int]:
    a = 32 # a*a >= 1000-a => a >= 32
    while True:
        # print(f"{(500_000-1000*a)%(1000-a) + (500_000+a*a-1000*a)%(1000-a)}")
        if a*a % (1000-a) == 0:
            b = (500_000-1000*a)//(1000-a)
            c = (500_000+a*a-1000*a)//(1000-a)
            return (a, b, c)
        else: a += 1

triplet = max_optimized()
print(f"The product of the pythagorean triplet {triplet} is:\n{triplet[0]*triplet[1]*triplet[2]}")