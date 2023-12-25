# greatest common divisor
def gcd(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    if b > a:
        # switch a and b
        c = a
        a = b
        b = c
    while a % b != 0:
        rest = a % b
        a = b
        b = rest
    return b

def lcm(a: int, b: int) -> int:
    return int(abs(a*b)/gcd(a, b))

result = 2
for i in range(3, 21):
    result = lcm(result, i)
print(f"The smallest positive number that is evenly divisable by 1 - 20 is:\n{result}")