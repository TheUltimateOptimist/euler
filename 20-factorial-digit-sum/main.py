def factorial(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(f"The sum of the digits is:\n{sum(map(lambda x: int(x), list(str(factorial(100)))))}")