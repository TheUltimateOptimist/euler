result = 0
for i in range(0, 1000, 3):
    if i % 5 != 0:
        result += i
for i in range(0, 1000, 5):
    result += i
print(f"The sum of all multiples of 3 and 5 smaller than 1000 is:\n{result}")