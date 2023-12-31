def find_unique(start: int, end: int) -> int:
    powers = set()
    for a in range(start, end + 1):
        for b in range(start , end + 1):
            powers.add(a**b)
    return len(powers)

print(f"The number of distinct powers is:\n{find_unique(2, 100)}")

