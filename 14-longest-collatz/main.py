def count_collatz(start: int) -> int:
    count = 1
    while start :
        count += 1
        if start % 2 == 0:
            start = start // 2
        else: start = 3*start + 1
    return count

def potenz_von_2(number: int) -> bool:
    compare_to = 1
    while compare_to < number:
        compare_to *= 2
    return compare_to == number

def count_collatz(start: int) -> tuple[int, int]:
    count = 1
    while start % 2 == 1 or not potenz_von_2(start):
        count += 1
        if start % 2 == 0:
            start = start // 2
        else: start = 3*start + 1
    return (count, start) 

# max_length = 0
# number = 0
# for i in range(1, 1_000_000):
#     length = count_collatz(i)
#     if length > max_length:
#         max_length = length
#         number = i
# print(f"The starting number producing the longest collatz sequence is:\n{number}")
for i in range(1, 100):
    print(count_collatz(i))
