from util import read

# read grid
grid = read("grid.txt").split("\n")
for i in range(len(grid)):
    grid[i] = list(map(lambda x: int(x), grid[i].split(" ")))

result = 0
for i in range(len(grid)):
    for k in range(len(grid[0]) - 3):
        lastInd = len(grid[0]) - 1
        productA = grid[i][k] * grid[i][k + 1] * grid[i][k + 2] * grid[i][k + 2]
        productB = grid[i][lastInd - k] * grid[i][lastInd - k - 1] * grid[i][lastInd - k - 2] * grid[i][lastInd - k - 3]
        diagonalA = 0
        diagonalB = 0
        if i < len(grid) - 3:
            diagonalA = grid[i][k] * grid[i + 1][k + 1] * grid[i + 2][k + 2] * grid[i + 3][k + 2]
            diagonalB = grid[i][lastInd - k] * grid[i + 1][lastInd - k - 1] * grid[i + 2][lastInd - k - 2] * grid[i + 3][lastInd - k - 3]
        result = max(result, productA, productB, diagonalA, diagonalB)
    for k in range(len(grid[0])):
        if i < len(grid) - 3:
            result = max(result, grid[i][k] * grid[i + 1][k] * grid[i + 2][k] * grid[i + 3][k])

print(f"The largest grid product is:\n{result}")
        