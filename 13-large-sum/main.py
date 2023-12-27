from util import read

numbers = list(map(lambda x: int(x), read("number.txt").split("\n")))
print(f"The large sum is:\n{sum(numbers)}")