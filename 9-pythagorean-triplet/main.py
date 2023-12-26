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

# copied solution
@timing
def another_optimized() -> tuple[int, int, int]:
    a = 3
    while True :
        if a % 2 == 0:
            b = ((a ** 2) / 4) - 1
            c = ((a ** 2) / 4) + 1
        else : 
            b = ((a ** 2) - 1) // 2
            c = ((a ** 2) + 1) // 2
        if 1000 % (a + b + c) == 0 :
            new_a = a * 1000 / (a + b + c)
            new_b = b * 1000 / (a + b + c)
            new_c = c * 1000 / (a + b + c)
            break
        else :
            a += 1
    return (new_a, new_b, new_c)


triplet = another_optimized()
print(f"The product of the pythagorean triplet {triplet} is:\n{triplet[0]*triplet[1]*triplet[2]}")