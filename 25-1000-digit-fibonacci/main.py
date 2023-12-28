a = 1
b = 1
index = 2
while len(str(b)) < 1000:
    c = a + b
    a = b
    b = c
    index += 1
print(f"The index of the first fib number with at least 1000 digits is:\n{index}")