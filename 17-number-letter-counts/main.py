counts = {
    0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
    11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6,
    30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7
}

def letter_count(number: int) -> int:
    if number == 1000:
        return 11
    count = 0
    tens = number % 100
    number = number // 100
    if tens > 20:
        count += counts[tens % 10]
        count += counts[(tens // 10)*10]
    else: count += counts[tens]
    if number > 0 and tens > 0:
        count += 3
    if number > 0:
        count += counts[100]
        count += counts[number]
    return count

result = 0
for i in range(1, 1001):
    result += letter_count(i)
print(result)