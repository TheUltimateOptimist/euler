def sum_divisors(num: int) -> int:
    result = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result += i
    return result

abundant_numbers = []
for i in range(12, 28111):
    if sum_divisors(i) > i:
        abundant_numbers.append(i)

representable = set()
for i in range(len(abundant_numbers) - 1):
    if 2*abundant_numbers[i] > 28122:
        break
    for j in range(i, len(abundant_numbers)):
        if abundant_numbers[i] + abundant_numbers[j] > 28122:
            break
        representable.add(abundant_numbers[i] + abundant_numbers[j])

print(f"The sum of all integers that can not be written as a sum of two abundant numbers is:\n{28122*28123//2 - sum(representable)}")