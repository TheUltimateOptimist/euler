def factorial(number: int) -> int:
    result = 1
    while number > 1:
        result *= number
        number-=1
    return result

# Kombination ohne Wdh => n ueber k => n! / k!*(n-k)!
print(f"The number of ways through a 20X20 grid is:\n{factorial(40) // (factorial(20)*factorial(20))}")