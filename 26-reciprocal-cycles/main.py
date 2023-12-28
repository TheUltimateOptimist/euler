def reciprocal_cycle_length(numerator: int, denominator: int, max_depth: int = 1000) -> int:
    assert denominator != 0
    if numerator == 0 or denominator == 1 or numerator % denominator == 0:
        return 0
    while numerator < denominator:
        numerator *= 10
    numerators: dict[int] = {}
    index = 0
    while index < max_depth:
        if numerator == 0:
            return 0
        if numerator < denominator:
            numerator *= 10
        if numerator in numerators:
            return index - numerators[numerator]
        numerators[numerator] = index
        numerator = numerator % denominator
        index += 1
    raise ValueError("No cycle could be found before the given max depth was exceeded!")

max_d = 7
max_val = 6
for i in range(11, 1000):
    cycle_length = reciprocal_cycle_length(1, i)
    if cycle_length > max_val:
        max_val = cycle_length
        max_d = i
print(f"The d with the max cycle length is:\n{max_d}")