from util import read
from dataclasses import dataclass

@dataclass
class Vertex:
    value: int
    distance: int
    connects_to: list[int]

def longest_path(filename: str) -> int:
    lines = read(filename).split("\n")
    verteces: list[Vertex] = []
    # create verteces
    for i, line in enumerate(lines):
        for j, number in enumerate(map(lambda x: int(x), line.split(" "))):
            new_row_index = (i + 1) * (i + 2) // 2 # gauss sum formula
            connects_to: list[int] = []
            if i < len(lines) - 1:
                connects_to.append(new_row_index + j) # left
                connects_to.append(new_row_index + j + 1) # right
            else: connects_to.append(new_row_index)
            verteces.append(Vertex(number, number, connects_to))
    verteces.append(Vertex(0, 0, []))

    # calculate longest path
    for vertex in verteces:
        for connection in vertex.connects_to:
            if vertex.distance + verteces[connection].value > verteces[connection].distance:
                verteces[connection].distance = vertex.distance + verteces[connection].value
    return verteces[-1].distance

print(f"The longest path for problem 18 is:\n{longest_path('18.txt')}")
print(f"The longest path for problem 67 is:\n{longest_path('67.txt')}")