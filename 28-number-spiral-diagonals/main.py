from util import timing

@timing
def diagonal_sum(width: int) -> int:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    assert width >= 3
    assert width % 2 == 1
    diagonal = 0
    row = width // 2
    col = width // 2
    steps = 0
    number = 1
    while True:
        for _ in range(steps // 2 + 1):
            number += 1
            row += directions[steps % 4][0]
            col += directions[steps % 4][1]
            if row == col or col == width - 1 - row:
                diagonal += number
            if row == 0 and col == width - 1:
                return diagonal + 1
        steps += 1

@timing
def analytical(width: int) -> int:
    return (4*width**3 + 3*width**2 + 8*width - 15) // 6 + 1

diagonal_sum(1001)
print(f"The diagonal sum with a width of 1001 is:\n{analytical(1001)}")
