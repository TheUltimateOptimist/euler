def armstrong_numbers() -> list[int]:
    numbers: list[int] = []
    for number in range(10, 1_000_000):
        a = number
        b = 0
        while number > 0:
            b += (number % 10)**5
            number = number // 10
        if a == b:
            numbers.append(a)
    return numbers

print(f"The sum of the armstrong numbers with 5 digits is:\n{sum(armstrong_numbers(5))}\nP.S. not really armstrong numbers since non 5 digit numbers are included.")
        