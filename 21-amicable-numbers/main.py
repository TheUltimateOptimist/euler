def sum_divisors(num: int) -> int:
    result = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result += i
    return result

result = 0
for i in range(2, 10000):
    divisors = sum_divisors(i)
    if divisors != i and sum_divisors(divisors) == i:
        result += i
print(f"The sum of amicalble numbers till 10000 is:\n{result}")
