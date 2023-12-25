result = 2
fib_a = 1
fib_b = 2
while fib_a + fib_b < 4_000_000:
    new_fib = fib_a + fib_b
    fib_a = fib_b
    fib_b = new_fib 
    if fib_b % 2 == 0:
        result += fib_b
print(f"The sum of all even fibonacci numbers smaller than 4_000_000 is:\n{result}")