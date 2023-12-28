from util import read

names = read("names.txt").split(",")
names.sort()

result = 0
for i, name in enumerate(names, start=1):
    value = 0
    for k in range(1, len(name) - 1):
        value += ord(name[k]) - 64
    result += i*value

print(f"the value of all words is:\n{result}")